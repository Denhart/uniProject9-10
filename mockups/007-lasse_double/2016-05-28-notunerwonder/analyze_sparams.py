from numpy import *
from matplotlib.pyplot import *
import aauplot

# With optical board
m = loadtxt("vna/sparamsCh1.csv", skiprows=3).T
f = m[0]
s11 = m[7]
s22 = m[6]
s21 = m[8]

aauplot.figure()
aauplot.sparam(f, s11, "-b", label="S11")
aauplot.sparam(f, s22, "-g", label="S22")
aauplot.sparam(f, s21, "-r", label="S21")

aauplot.end_sparam(ncol=3, loc=8)
savefig("sparams.pdf")


show()
