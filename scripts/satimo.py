from numpy import *

# Load a text file, output from Satimo.
#
# @param f File name
# @return Matrix of file rows/columns
def loadfile(f):
    return loadtxt(f, skiprows=4)

# Convert a Satimo-exported column to a matrix with phi the 
# x-axis and theta on the y-axis.
#
# @param column Column from a Satimo export.
# @param ntheta Number of rows in the output (theta in the input).
# @param nphi Number of columns in the output (phi in the input).
# @return Matrix with phi on the x-axis and theta on the y-axis.
def col2mat(column, ntheta=127, nphi=64):
    d = resize(column, (nphi, ntheta))
    M1 = d[ix_(range(0,nphi), range(0,int(ntheta/2)+1))]  # Include 0 deg
    M2 = d[ix_(range(0,nphi), range(int(ntheta/2), ntheta))]  # Include 0 deg
    M2 = fliplr(M2)
    d = vstack((M2, M1)).T
    d = flipud(d)
    return d

# Create a farfield matrix (theta x phi) from the imported data
# of a CSV file.
#
# @param data Rows/column-matrix, as exported by loadfile().
# @param column_abs Column of data containing the real part of the farfield.
# @param column_phase Column of data containing the imaginary  part of the
# farfield.
# @return Matrix (phi x theta) like col2mat().
def ff2mat(data, column_real, column_imag):
    re = data[:,column_real]
    im = data[:,column_imag]
    return col2mat(re + 1j*im)
