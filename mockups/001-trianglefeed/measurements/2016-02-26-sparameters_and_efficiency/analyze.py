from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()
m = loadtxt("sim/top_09pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--b", label="S11 sim")
m = loadtxt("sim/s21_09pf_03pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--g", label="S21 sim")
m = loadtxt("sim/side_03pf.txt", skiprows=2).T
aauplot.sparam(m[0], m[1], "--r", label="S22 sim")

m = loadtxt("sparams.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], "-b", label="S11")
aauplot.sparam(m[0], m[3], "-g", label="S21")
aauplot.sparam(m[0], m[5], "-r", label="S22")

aauplot.legend(ncol=2, loc=0)
savefig("sparams.pdf")

m2 = loadtxt("../2016-02-25-sparameters_good_vna/Csh1_09_Csh2_11.csv", skiprows=3).T
aauplot.figure()
aauplot.sparam(m[0]  , m[1]  , label="$S_{11}$, $C_{\mathrm{sh}2} =$ 0.3 pF")
aauplot.sparam(m2[0] , m2[1] , label="$S_{11}$, $C_{\mathrm{sh}2} =$ 0.9 pF")
aauplot.sparam(m[0]  , m[5]  , label="$S_{22}$, $C_{\mathrm{sh}2} =$ 0.3 pF")
aauplot.sparam(m2[0] , m2[5] , label="$S_{22}$, $C_{\mathrm{sh}2} =$ 0.9 pF")
aauplot.legend(loc=4)
savefig("sparam_comparison.pdf")

show()
