from numpy import *
from matplotlib.pyplot import *
import aauplot

vnadir = "sparams/"
top = ["henrik-top-0.3-pF.s2p",
        "henrik-top-0.7-pF.s2p",
        "henrik-top-1.1-pF.s2p",
        "henrik-top-1.5-pF.s2p",
        "henrik-top-2.0-pF.s2p",
        "henrik-top-2.7-pF.s2p",
        "henrik-top-3.0-pF.s2p",
        ]

side = ["henrik-top-0.3-pF.s2p",
        "henrik-top-0.7-pF.s2p",
        "henrik-top-1.1-pF.s2p",
        "henrik-top-1.5-pF.s2p",
        "henrik-top-2.0-pF.s2p",
        "henrik-top-2.7-pF.s2p",
        "henrik-top-3.0-pF.s2p",
        ]

#S11
aauplot.figure()
for s in top:
    m = loadtxt(vnadir + s, skiprows=5).T
    f = m[0]
    S11 = m[1] + 1j*m[2]
    S21 = m[3] + 1j*m[4]
    S12 = m[5] + 1j*m[6]
    S22 = m[7] + 1j*m[8]

    aauplot.sparam(f, 20*log10(abs(S11)))

aauplot.end_sparam()
savefig("s11_csh1.pdf")

#S21
aauplot.figure()
for s in top:
    m = loadtxt(vnadir + s, skiprows=5).T
    f = m[0]
    S11 = m[1] + 1j*m[2]
    S21 = m[3] + 1j*m[4]
    S12 = m[5] + 1j*m[6]
    S22 = m[7] + 1j*m[8]

    aauplot.sparam(f, 20*log10(abs(S21)))

aauplot.end_sparam()
savefig("s21_csh1.pdf")

#S12
aauplot.figure()
for s in side:
    m = loadtxt(vnadir + s, skiprows=5).T
    f = m[0]
    S11 = m[1] + 1j*m[2]
    S21 = m[3] + 1j*m[4]
    S12 = m[5] + 1j*m[6]
    S22 = m[7] + 1j*m[8]

    aauplot.sparam(f, 20*log10(abs(S12)))

aauplot.end_sparam()
savefig("s12_csh1.pdf")

#S22
aauplot.figure()
for s in side:
    m = loadtxt(vnadir + s, skiprows=5).T
    f = m[0]
    S11 = m[1] + 1j*m[2]
    S21 = m[3] + 1j*m[4]
    S12 = m[5] + 1j*m[6]
    S22 = m[7] + 1j*m[8]

    aauplot.sparam(f, 20*log10(abs(S22)))

aauplot.end_sparam()
savefig("s22_csh1.pdf")
show()
