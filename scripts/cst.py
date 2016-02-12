from numpy import *

# Load a CST exported file.
#
# @param f File to load.
# @return Matrix with the files rows/columns.
def loadfile(f):
    return loadtxt(f, skiprows=2)

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

# Create a farfield matrix (theta x phi) from the imported data
# of a CSV file.
#
# @param data Rows/column-matrix, as exported by loadfile().
# @param column_abs Column of data containing the abs value of the farfield.
# @param column_phase Column of data containing the phase value of the farfield.
# @return Matrix (phi x theta) like col2mat().
def ff2mat(data, column_abs, column_phase):
    A = 10**(data[:,column_abs]/20)
    phi = data[:,column_phase] * pi/180
    return col2mat(A*exp(1j*phi))
