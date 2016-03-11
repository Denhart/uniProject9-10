from numpy import *
from matplotlib.pyplot import *
import aauplot

vnadir = "data/VNA/"
top = ["triag-0.3-pF.s2p",
        "triag-0.7-pF.s2p",
        "triag-1.1-pF.s2p",
        "triag-1.5-pF.s2p",
        "triag-2.0-pF.s2p",
        "triag-2.7-pF.s2p",
        "triag-3.0-pF.s2p",
        ]

side = ["triag-side-0.3-pF.s2p",
        "triag-side-0.7-pF.s2p",
        "triag-side-1.1-pF.s2p",
        "triag-side-1.5-pF.s2p",
        "triag-side-2.0-pF.s2p",
        "triag-side-2.7-pF.s2p",
        "triag-side-3.0-pF.s2p",
        ]

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
savefig("s22_csh2.pdf")
show()
