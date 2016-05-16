from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

# Measurement
m = loadtxt("meas/henrik-top-0.3-pF.s2p", skiprows=5).T
f = m[0]
S11 = m[1] + 1j*m[2]
S21 = m[3] + 1j*m[4]
S12 = m[5] + 1j*m[6]
S22 = m[7] + 1j*m[8]

aauplot.sparam(f, 20*log10(abs(S11)), "-b", label="S11 meas")
aauplot.sparam(f, 20*log10(abs(S21)), "-g", label="S21 meas")
aauplot.sparam(f, 20*log10(abs(S22)), "-r", label="S22 meas")

# Simulation
fS11,S11s = loadtxt("sim/S1,1", skiprows=2).T
fS21,S21s = loadtxt("sim/S2,1", skiprows=2).T
fS12,S12s = loadtxt("sim/S1,2", skiprows=2).T
fS22,S22s = loadtxt("sim/S2,2", skiprows=2).T

aauplot.sparam(fS11,S11s, "--b", label="S11 sim")
aauplot.sparam(fS21,S21s, "--g", label="S21 sim")
aauplot.sparam(fS22,S22s, "--r", label="S22 sim")

xlim(500, 3000)
aauplot.end_sparam(loc=8, ncol=2)

savefig("sparams.pdf")
show()
