from numpy import *
from matplotlib.pyplot import *
import aauplot

# Top antenna = S22
# Side antenna = S11
f,S22,S22_,S11,S21 = loadtxt("sparams/lasse_03_03.csv", skiprows=3).T

aauplot.figure()
aauplot.sparam(f,S11,label="S11 meas")
aauplot.sparam(f,S22,label="S22 meas")
aauplot.sparam(f,S21,label="S21 meas")

m = loadtxt("sim/s11.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--b", label="S11 sim")
m = loadtxt("sim/s22.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--g", label="S22 sim")
m = loadtxt("sim/s21.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--r", label="S21 sim")


aauplot.end_sparam(ncol=2, loc=8)

savefig("sparams.pdf")
show()
