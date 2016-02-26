from numpy import *
from matplotlib.pyplot import *
import aauplot

m = loadtxt("sparams.csv", skiprows=3).T
aauplot.figure()
aauplot.sparam(m[0], m[1], "S11")
aauplot.sparam(m[0], m[3], "S21")
aauplot.sparam(m[0], m[5], "S22")
aauplot.legend()
savefig("sparams.pdf")

m2 = loadtxt("../2016-02-25-sparameters_good_vna/Csh1_09_Csh2_11.csv", skiprows=3).T
aauplot.figure()
aauplot.sparam(m[0]  , m[1]  , "$S_{11}$, $C_{\mathrm{sh}2} =$ 0.3 pF")
aauplot.sparam(m2[0] , m2[1] , "$S_{11}$, $C_{\mathrm{sh}2} =$ 0.9 pF")
aauplot.sparam(m[0]  , m[5]  , "$S_{22}$, $C_{\mathrm{sh}2} =$ 0.3 pF")
aauplot.sparam(m2[0] , m2[5] , "$S_{22}$, $C_{\mathrm{sh}2} =$ 0.9 pF")
aauplot.legend(loc=4)
savefig("sparam_comparison.pdf")

show()
