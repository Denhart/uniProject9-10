from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

m = loadtxt("withboard_withbatteryCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], '-b', label="S11$+$board$+$ bat")
aauplot.sparam(m[0], m[2], '-g', label="S22$+$board$+$ bat")
#aauplot.sparam(m[0], m[3], '-r', label="S21 $+$ board $+$ bat")

m = loadtxt("withboard_nobatteryCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], '--b', label="S11$+$board$-$ bat")
aauplot.sparam(m[0], m[2], '--g', label="S22$+$board$-$ bat")
#aauplot.sparam(m[0], m[3], '--r', label="S21 $+$ board $-$ bat")

m = loadtxt("noboard_nobatteryCh1.csv", skiprows=3).T
aauplot.sparam(m[0], m[1], '-.b', label="S11 $-$board$-$ bat")
aauplot.sparam(m[0], m[2], '-.g', label="S22 $-$board$-$ bat")
#aauplot.sparam(m[0], m[3], '-.r', label="S21 $-$ board $-$ bat")

aauplot.end_sparam(loc=8, ncol=2)
savefig("sparam_comparison.pdf")
show()
# savefig("sparams_best_match.pdf")
