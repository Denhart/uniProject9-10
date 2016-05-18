from numpy import *
from matplotlib.pyplot import *
import aauplot
from glob import glob

vnadir = "vna/"

# With optical board
m = loadtxt("vna/wonderant_0_0_0_0.s2p", skiprows=5).T
f = m[0]
s11 = 20*log10(m[1] + 1j*m[2])
s21 = 20*log10(m[3] + 1j*m[4])
s12 = 20*log10(m[5] + 1j*m[6])
s22 = 20*log10(m[7] + 1j*m[8])

aauplot.figure()
aauplot.sparam(f, s11, "-b", label="S11 $+$ RFFE")
aauplot.sparam(f, s22, "-g", label="S22 $+$ RFFE")
aauplot.sparam(f, s21, "-r", label="S21 $+$ RFFE")

# No optical board
m = loadtxt("vna/wonder_no_opticalCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[7], '--c', label="S11 $-$ RFFE")
aauplot.sparam(m[0], m[6], '--y', label="S22 $-$ RFFE")
aauplot.sparam(m[0], m[8], '--m', label="S21 $-$ RFFE")

aauplot.end_sparam(ncol=2, loc=8)
savefig("sparams.pdf")


show()
