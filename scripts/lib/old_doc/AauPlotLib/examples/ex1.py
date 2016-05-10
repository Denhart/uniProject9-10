from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()
m = loadtxt("ex1_sparams.csv", skiprows=3).T

aauplot.sparam(m[0], m[1], label="S11")
aauplot.sparam(m[0], m[3], label="S21")
aauplot.sparam(m[0], m[5], label="S22")
aauplot.end_sparam(loc=1)

savefig("ex1_sparams.pdf")
show()
