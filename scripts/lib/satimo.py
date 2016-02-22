from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import *
import re
import l3d
import satenv
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'

TRX_NUM_HEADER_LINES = 36
SATIMO_NUM_ELEVATION = 15
SATIMO_NUM_AZIMUTH = 8
SATIMO_NUM_SAMPLES = SATIMO_NUM_ELEVATION * SATIMO_NUM_AZIMUTH

# Convert a Satimo-exported column to a matrix with phi the 
# x-axis and theta on the y-axis.
#
# @param column Column from a Satimo export.
# @param ntheta Number of rows in the output (theta in the input).
# @param nphi Number of columns in the output (phi in the input).
# @return Matrix with phi on the x-axis and theta on the y-axis.
def col2mat(column, ntheta=SATIMO_NUM_ELEVATION, nphi=SATIMO_NUM_AZIMUTH):
    d = resize(column, (nphi, ntheta))
    M1 = d[ix_(range(0,nphi), range(0,int(ntheta/2)+1))]  # Include 0 deg
    M2 = d[ix_(range(0,nphi), range(int(ntheta/2), ntheta))]  # Include 0 deg
    M2 = fliplr(M2)
    d = vstack((M2, M1)).T
    d = flipud(d)

    return d

# Load a trx measurement file from Satimo PM into memory. 
#
# @return [f, list_horiz, list_vert] where
#     f = [f1, f2, f3, ...]
#     list_horiz = [E_horiz_f1, E_horiz_f2, E_horiz_f3, ...]
#     list_vert  = [E_vert_f1,  E_vert_f2,  E_vert_f3,  ...]
# and each "E" is a complex matrix, (theta x phi), containing the received fields.
def loadtrx(f):
    print("Loading trx file:", f)
    with open(f) as thisfile:
        header = [next(thisfile) for x in range(TRX_NUM_HEADER_LINES)]
    header = "".join(header)

    # Extract frequency sweep from header
    frequency = re.findall(r'Frequency\s*\n(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\w+)', header)[0]
    f_num,f_min,f_max = int(frequency[1]), float(frequency[2]), float(frequency[3])
    f_step = (f_max - f_min) / (f_num-1)
    freq = linspace(f_min, f_max, f_num)

    # Extract header lines from header
    header_lines = re.findall(r'Elevation\s*\n.*?\n(.*?)\n.*?\n(.*?)\n.*?\n(.*?)\n.*?\n(.*?)\n', header)[0]

    # Extract and format data (horizontal and vertical polarization, a matrix for each freq)
    data = loadtxt(f, skiprows=TRX_NUM_HEADER_LINES).T

    list_horiz = []
    list_vert = []
    N = SATIMO_NUM_SAMPLES
    for n in range(f_num):
        list_horiz.append(col2mat(data[0, n*N:(n+1)*N] + 1j*data[1, n*N:(n+1)*N]))
        list_vert.append(col2mat(data[2, n*N:(n+1)*N] + 1j*data[3, n*N:(n+1)*N]))

    return [freq, list_horiz, list_vert]

# Radiated power from a (theta x phi) total E-field matrix.
#
# @param Etot Matrix (theta x phi) from Satimo PM to compute the radiate power
#        of (surface integration).
def radiatedpower_single(Etot):
    ntheta,nphi = Etot.shape

    # TODO: Figure out whether to start from 22.5 or 12 (or 15)
    theta = pi/180 * linspace(0, 180-12, ntheta)
    phi   = pi/180 * linspace(0, 360, nphi)

    I = l3d.intsphere(Etot, theta, phi)
    return I

# Compute the radiated power for each frequency in the h and v list.
#
# @param h List of complex (theta x phi) matrices -- one for each frequency.
#        Horizontal polarization.
# @param v List of complex (theta x phi) matrices -- one for each frequency.
#        Vertical polarization.
def radiatedpower(h,v):
    N = len(h)
    P_rad = zeros(N)
    for i in range(N):
        P_rad[i] = radiatedpower_single( abs(h[i])**2 + abs(v[i])**2 )

    return P_rad

# Load a reference file containing S11, Gain, and Efficiency of a
# reference/calibration antenna.
# 
# @param f File name.
# @return M[0]=frequency(Hz), M[1]=S11(.), M[2]=Gain(.), M[3]=Eff(.)
def loadref(f):
    print("Loading reference file:", f)
    M = loadtxt(f, skiprows=5, comments="#").T
    M[0] *= 1e6
    M[1] = 10**(M[1]/20)
    M[2] = 10**(M[2]/10)
    M[3] = 10**(M[3]/10)
    return M

# Make a table of calibrated "total power" for each frequency.
# Having (1) the total power and (2) the radiated power for a given antenna,
# makes it possible to compute the total efficiency of the antenna.
#
# @param calfiles List of calibration measurement files (trx files) (order:
#        lowest to highest frequency).
# @param reffiles List of reference files relating to the calibration
#        measurements (order: lowest to highest frequency).
def totalpower_table(calfiles, reffiles):
    # Get Efficiency from reference files
    f_ref = array([0]) # Must be initialize to use max()
    eff_ref = array([])
    for i in range(len(reffiles)):
        m       = loadref(reffiles[i])
        eff_ref = append(eff_ref, m[3, m[0]>max(f_ref)])
        f_ref   = append(f_ref, m[0, m[0]>max(f_ref)])
    f_ref = delete(f_ref, 0) # Remove initial element

    # Get Radiated Power from calibration measurement files
    f_cal = array([0])
    P_rad_cal = array([])
    for i in range(len(calfiles)):
        f,h,v     = loadtrx(calfiles[i])
        P_rad     = radiatedpower(h,v)
        P_rad_cal = append(P_rad_cal, P_rad[f>max(f_cal)])
        f_cal     = append(f_cal, f[f>max(f_cal)])
    f_cal = delete(f_cal, 0)

    # Compute Total Power from the two above. Interpolation is made.
    f_min  = min([min(f_ref),       min(f_cal)])
    f_max  = max([max(f_ref),       max(f_cal)])
    f_step = min([min(diff(f_ref)), min(diff(f_cal))])
    f = arange(f_min, f_max, f_step)

    eff = interp(f, f_ref, eff_ref)
    P_rad = interp(f, f_cal, P_rad_cal)
    P_tot = P_rad/eff

    return [f, P_tot]

# Get the total efficiency of a trx file, exported from Satimo.
#
# @param trxfile File, exported from Satimo PM, to compute the efficiency of.
# @param calfiles List of calibration measurement files (trx files).
# @param reffiles List of reference files relating to the calibration
#        measurements.
def efficiency(trxfile, calfiles, reffiles):
    f,h,v = loadtrx(trxfile)
    P_rad = radiatedpower(h,v) 

    f_tot,P_tot = totalpower_table(calfiles, reffiles)
    P_tot = interp(f, f_tot, P_tot)

    eff = P_rad/P_tot
    return [f, eff]

if __name__ == "__main__":
    calfiles = ["data/more/patch/calib/ff_sweep_SPM.trx"]
    reffiles = [
            "data/more/patch/calib/SD740-70.ref",
            "data/more/patch/calib/SD850-02.ref",
            "data/more/patch/calib/SD900-51.ref",
            "data/more/patch/calib/SD1800-45.ref",
            "data/more/patch/calib/SD1900-49.ref",
            "data/more/patch/calib/SD2050-36.ref",
            "data/more/patch/calib/SD2450-43.ref",
            "data/more/patch/calib/SD2600-28.ref",
            ]

    subplot(211)
    f,e = efficiency("data/more/patch/SPM_sweep.trx", calfiles, reffiles)
    plot(f,e, '-', label="Our implementation")

    m = loadtxt('data/more/patch/eff_sweep_satenv.txt', skiprows=2).T
    plot(m[0], m[1], '--', label="Exported from SatEnv")

    ylabel("Efficiency [.]")
    xlabel("Frequency [Hz]")
    legend(fontsize=12)
    ylim(0,1)

    subplot(212)
    hist(e-interp(f,m[0],m[1]))
    xlabel("Error/difference [.]")
    # xlabel("Frequency [Hz]")
    xlim(-0.05, 0.05)
    tight_layout()
    show()
