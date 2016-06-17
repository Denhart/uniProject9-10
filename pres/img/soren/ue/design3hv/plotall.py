from numpy import *
from matplotlib.pyplot import *
from glob import glob
from os import system
import presplot

c = ['b', 'g', 'r', 'c']
fs = (4.5, 1.1)

def plotextreme(S, minmax="min", tp="sparam"):
    presplot.figure(figsize=fs)
    for i in range(4):
        f0 = array([])
        s0 = array([])
        f_ = array([])
        s_ = array([])

        for j in range(len(S[i])):
            m = loadtxt(S[i][j], skiprows=2).T
            if (j == 0):
                f0 = m[0]
                s0 = m[1]
                f_ = f0
                s_ = s0
            else:
                if (minmax == "min"):
                    s_ = minimum(s_, m[1])
                elif (minmax == "max"):
                    s_ = maximum(s_, m[1])


        if (tp == "sparam"):
            presplot.sparam(f_, s_, c[i])
            # presplot.sparam(f0, s0, c[i], linewidth=0.1)
        elif (tp == "efficiency"):
            presplot.efficiency(f_, s_, c[i])
            # presplot.efficiency(f0, s0, c[i])
        elif (tp == "correlation"):
            presplot.correlation(f_, s_, c[i])

    if (tp == "sparam"):
        presplot.end_sparam()
    elif (tp == "efficiency"):
        presplot.end_efficiency()
    elif (tp == "correlation"):
        presplot.end_correlation()

def g(s):
    return sort(glob(s))

def savecrop(f):
    savefig(f)
    system("pdfcrop %s %s"%(f,f))


# S11
S = [ g("1-fs/s11top/S1*"), g("2-data/s11top/S1*"), g("3-play/s11top/S1*"), g("4-talk/s11top/S1*") ]
plotextreme(S, "min", "sparam")
savecrop("s11top.pdf")

# S22
S = [ g("1-fs/s22side/S2*"), g("2-data/s22side/S2*"), g("3-play/s22side/S2*"), g("4-talk/s22side/S2*") ]
plotextreme(S, "min", "sparam")
savecrop("s22side.pdf")

# S21 top
S = [ g("1-fs/s21top/S1*"), g("2-data/s21top/S1*"), g("3-play/s21top/S1*"), g("4-talk/s21top/S1*") ]
plotextreme(S, "min", "sparam")
savecrop("s21top.pdf")

# S21 side
S = [ g("1-fs/s21side/S2*"), g("2-data/s21side/S2*"), g("3-play/s21side/S2*"), g("4-talk/s21side/S2*") ]
plotextreme(S, "min", "sparam")
savecrop("s21side.pdf")

# Efficiency
E = [ g("1-fs/efftop/*.txt"), g("2-data/efftop/*.txt"), g("3-play/efftop/*.txt"), g("4-talk/efftop/*.txt") ]
plotextreme(E, "max", "efficiency")
savecrop("efftop.pdf")

E = [ g("1-fs/effside/*.txt"), g("2-data/effside/*.txt"), g("3-play/effside/*.txt"), g("4-talk/effside/*.txt") ]
plotextreme(E, "max", "efficiency")
savecrop("effside.pdf")

# Correlation
C = [ g("1-fs/corrtop/C_*"), g("2-data/corrtop/run_*"), g("3-play/corrtop/C_*"), g("4-talk/corrtop/C_*") ]
plotextreme(C, "min", "correlation")
savecrop("corrtop.pdf")

C = [ g("1-fs/corrside/s_*"), g("2-data/corrside/s_*"), g("3-play/corrside/s_*"), g("4-talk/corrside/s_*") ]
plotextreme(C, "min", "correlation")
savecrop("corrside.pdf")

# show()
