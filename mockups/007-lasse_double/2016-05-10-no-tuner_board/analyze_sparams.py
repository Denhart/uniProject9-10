from numpy import *
from matplotlib.pyplot import *
import aauplot

m = loadtxt("sparams_best_match.csv", skiprows=3).T
aauplot.figure()
aauplot.sparam(m[0], m[1], label="S11")
aauplot.sparam(m[0], m[2], label="S22")
aauplot.sparam(m[0], m[3], label="S21")
aauplot.end_sparam(loc=4)
savefig("sparams_best_match.pdf")
