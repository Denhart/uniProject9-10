from numpy import *
from matplotlib.pyplot import *
from glob import glob
from os import system
import presplot

c = ['b', 'g', 'r', 'c']
# fs = (4.5, 1.1)
fs = (2.4, 1.55)

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

###
S = g("stop/*.s2p")
presplot.figure(1, figsize=fs)
for s in S:
    m = loadtxt(s, skiprows=5).T
    presplot.sparam(m[0], 20*log10(abs(m[1] + 1j*m[2])))

presplot.end_sparam()
savefig("s11.pdf")
system("pdfcrop s11.pdf s11.pdf")

###
S = g("sside/*.s2p")
presplot.figure(2, figsize=fs)
for s in S:
    m = loadtxt(s, skiprows=5).T
    presplot.sparam(m[0], 20*log10(abs(m[7] + 1j*m[8])))

presplot.end_sparam()
savefig("s22.pdf")
system("pdfcrop s22.pdf s22.pdf")

###
S = g("efftop/*.txt")
presplot.figure(3, figsize=fs)
for s in S:
    m = loadtxt(s).T
    presplot.efficiency(m[0], m[1])

presplot.end_efficiency()
savefig("efftop.pdf")
system("pdfcrop efftop.pdf efftop.pdf")

###
S = g("effside/*.txt")
presplot.figure(4, figsize=fs)
for s in S:
    m = loadtxt(s).T
    presplot.efficiency(m[0], m[1])

presplot.end_efficiency()
savefig("effside.pdf")
system("pdfcrop effside.pdf effside.pdf")

