from numpy import *
from matplotlib.pyplot import *
import aauplot

m = loadtxt("Csh1_09_Csh2_11.csv", skiprows=3).T

aauplot.figure()
aauplot.sparam(m[0], m[1], label="S11")
aauplot.sparam(m[0], m[3], label="S21")
aauplot.sparam(m[0], m[5], label="S22")

aauplot.end_sparam()
savefig("sparams.pdf")
show()
