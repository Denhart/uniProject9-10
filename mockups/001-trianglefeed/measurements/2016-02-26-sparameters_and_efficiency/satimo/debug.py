import satimo
import aauplot
from numpy import *
from matplotlib.pyplot import *
from scipy.io import loadmat

# Calibration measurements
calfiles = [
        "calib/600RefDipole.trx",
        "calib/740RefDipole.trx",
        "calib/850RefDipole.trx",
        "calib/900RefDipole.trx",
        ]

# Reference files
reffiles = [
        "calib/HomeRef600.ref",
        "calib/SD740-70.ref",
        "calib/SD850-02.ref",
        "calib/SD900-51.ref",
        "calib/SD1900-49.ref",
        "calib/SD2050-36.ref",
        "calib/SD2450-43.ref",
        ]

f_tot1,P_tot1 = satimo.totalpower_table(calfiles, reffiles)

M = loadmat("../Sam-eff/SAtimo/Cal_tableLB.mat")
f2 = M["Cal_tableLB"].T[1]*1e6
x2 = 10**(M["Cal_tableLB"].T[2]/10)

P_tot2 = 1/x2 # Sams
f_tot2 = f2 # Sams

f,h,v = satimo.loadtrx("Triag-LB-Top-H.trx") # Ours
P_rad = satimo.radiatedpower(h,v)  # Ours

P_tot1 = interp(f, f_tot1, P_tot1)
P_tot2 = interp(f, f_tot2, P_tot2)

eff1 = P_rad/P_tot1
eff2 = P_rad/P_tot2

plot(f, 10*log10(eff1), label="Our P_tot table")
plot(f, 10*log10(eff2), label="Sams P_tot table")

f_sam,eff_sam = loadtxt("../Sam-eff/Triag-LB-Top-H.csv", delimiter=",").T
plot(f_sam*1e6, eff_sam, label="Correct")
legend()

show()


# savetxt("debug_py.txt",x)
