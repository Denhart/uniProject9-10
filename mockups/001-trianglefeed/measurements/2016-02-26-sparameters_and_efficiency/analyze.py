from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()
# Measurements
m = loadtxt("sparams.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], "-b", label="S11 meas")
aauplot.sparam(m[0], m[5], "-g", label="S22 meas")
aauplot.sparam(m[0], m[3], "-r", label="S21 meas")

# Simulations
m = loadtxt("sim/top_09pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--b", label="S11 sim")
m = loadtxt("sim/side_03pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--g", label="S22 sim")
m = loadtxt("sim/s21_09pf_03pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--r", label="S21 sim")

aauplot.end_sparam(ncol=2, loc=8)
savefig("sparams.pdf")
show()
