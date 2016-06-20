from numpy import *
from matplotlib.pyplot import *
from glob import glob
from os import system
import presplot
import re

c = ['b', 'g', 'r', 'c', 'm']
# fs = (4.5, 1.1)
fs = (2.4, 1.55)

def plotextreme(S, minmax="min", tp="sparam", nfiles=3):
    presplot.figure(figsize=fs)
    for i in range(nfiles):
        f0 = array([])
        s0 = array([])
        f_ = array([])
        s_ = array([])

        for j in range(len(S[i])):
            skiprows = 0
            if ("sim" in S[i][j]):
                skiprows = 2

            # S2P files
            if tp == "sparam" and (".s2p" in S[i][j]):
                m = loadtxt(S[i][j], skiprows=5).T
                f_tmp = m[0]
                if "stop" in S[i][j]:
                    s_tmp = 20*log10(abs(m[1] + 1j*m[2]))
                elif "sside" in S[i][j]:
                    s_tmp = 20*log10(abs(m[7] + 1j*m[8]))

            # 2-column txt files
            else:
                m = loadtxt(S[i][j], skiprows=skiprows).T
                f_tmp = m[0]
                s_tmp = m[1]

            if (j == 0):
                f0 = f_tmp
                s0 = s_tmp
                f_ = f0
                s_ = s0
            else:
                if (minmax == "min"):
                    s_ = minimum(s_, s_tmp)
                elif (minmax == "max"):
                    s_ = maximum(s_, s_tmp)

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

# C = [ g("1-fs/corrtop/Csh*"), g("2-data/corrtop/Csh*"), g("3-play/corrtop/run*"), g("4-talk/corrtop/run*") ]
# plotextreme(C, "min", "correlation")
# savecrop("corrtop.pdf")
# 
# C = [ g("1-fs/corrside/Csh*"), g("2-data/corrside/Csh*"), g("3-play/corrside/Csh*"), g("4-talk/corrside/run*") ]
# plotextreme(C, "min", "correlation")
# savecrop("corrside.pdf")


# 001 ##########################################################################
# S11
S = [ g("minimized_monopole/sim/s11top/S1*"), g("minimized_monopole/meas/stop/*.s2p"), g("triangle_feed/meas/stop/*.s2p")]
plotextreme(S, "min", "sparam")
savecrop("001_s11top.pdf")

# S22
S = [ g("minimized_monopole/sim/s22side/S2*"), g("minimized_monopole/meas/sside/*.s2p"), g("triangle_feed/meas/sside/*.s2p") ]
plotextreme(S, "min", "sparam")
savecrop("001_s11side.pdf")

# Efficiency
E = [ g("minimized_monopole/sim/efftop/*.txt"),  g("minimized_monopole/meas/efftop/*.txt"), g("triangle_feed/meas/efftop/*.txt") ]
plotextreme(E, "max", "efficiency")
savecrop("001_efftop.pdf")

E = [ g("minimized_monopole/sim/effside/*.txt"),  g("minimized_monopole/meas/effside/*.txt"), g("triangle_feed/meas/effside/*.txt") ]
plotextreme(E, "max", "efficiency")
savecrop("001_effside.pdf")

# 002 ##########################################################################
# S11
S = [ g("modified_monopole/sim/s11top/S1*"), g("modified_monopole/meas/stop/*.s2p")]
plotextreme(S, "min", "sparam", nfiles=2)
savecrop("002_s11top.pdf")

S = [ g("modified_monopole/sim/s22side/S2*"), g("modified_monopole/meas/sside/*.s2p")]
plotextreme(S, "min", "sparam", nfiles=2)
savecrop("002_s22side.pdf")

E = [ g("modified_monopole/sim/efftop/*.txt"), g("modified_monopole/meas/efftop/*.txt") ]
plotextreme(E, "max", "efficiency", nfiles=2)
savecrop("002_efftop.pdf")

E = [ g("modified_monopole/sim/effside/*.txt"), g("modified_monopole/meas/effside/*.txt") ]
plotextreme(E, "max", "efficiency", nfiles=2)
savecrop("002_effside.pdf")

show()
# exit()
