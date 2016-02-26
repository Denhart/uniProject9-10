from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()
m = loadtxt("ex1_sparams.csv", skiprows=3).T

aauplot.sparam(m[0], m[1], "S11")
aauplot.sparam(m[0], m[3], "S21")
aauplot.sparam(m[0], m[5], "S22")
aauplot.legend(loc=1)

savefig("ex1_sparams.pdf")
show()
