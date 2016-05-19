from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

m = loadtxt("withboard_withbatteryCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], '-b', label="S11 $+$ RFFE")
aauplot.sparam(m[0], m[2], '-g', label="S22 $+$ RFFE")
aauplot.sparam(m[0], m[3], '-r', label="S21 $+$ RFFE")

m = loadtxt("noboard_nobatteryCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], '--c', label="S11 $-$ RFFE")
aauplot.sparam(m[0], m[2], '--y', label="S22 $-$ RFFE")
aauplot.sparam(m[0], m[3], '--m', label="S21 $-$ RFFE")

aauplot.end_sparam(loc=8, ncol=2)
savefig("sparams2.pdf")
show()
