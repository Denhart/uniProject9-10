from numpy import *

THETA_ABS_COLUMN   = 3
THETA_PHASE_COLUMN = 4
PHI_ABS_COLUMN     = 5
PHI_PHASE_COLUMN   = 6

# Convert a CST-exported column to a matrix with phi the 
# x-axis and theta on the y-axis.
#
# @param column Column from a Satimo export.
# @param nx Number of columns in the output (phi in the input).
# @param ny Number of rows in the output (theta in the input).
# @return Matrix with phi on the x-axis and theta on the y-axis.
def col2mat(column, nx=360, ny=181):
    d = resize(column, (nx, ny)).T
    d = flipud(d)
    return d

# Load a CST exported file to two (theta x phi) matrices -- one for theta and
# one for phi plarization.
#
# @param f File to load.
# @return [T,P] where T and P are each a (theta x phi) matrix.
def loadff(f):
    data = loadtxt(f, skiprows=2)

    A = 10**(data[:,THETA_ABS_COLUMN]/20)
    phase = data[:,THETA_PHASE_COLUMN] * pi/180
    T = col2mat(A*exp(1j*phase))

    A = 10**(data[:,PHI_ABS_COLUMN]/20)
    phase = data[:,PHI_PHASE_COLUMN] * pi/180
    P = col2mat(A*exp(1j*phase))

    return [T,P]

