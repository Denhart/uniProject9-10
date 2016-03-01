from numpy import *
from matplotlib.pyplot import *
import aauplot

m = loadtxt("Csh1_09_Csh2_11.csv", skiprows=3).T

aauplot.figure()
aauplot.sparam(m[0], m[1], "S11")
aauplot.sparam(m[0], m[3], "S21")
aauplot.sparam(m[0], m[5], "S22")

aauplot.legend()
savefig("sparams.pdf")
show()
