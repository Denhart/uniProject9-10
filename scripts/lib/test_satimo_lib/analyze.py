from numpy import *
from matplotlib.pyplot import *
import aauplot
import satimo
import l3d

aauplot.figure(figsize=(7,6))

# MEASUREMENT 1 ################################################################
M = loadtxt("meas1/meas1_satenv.txt", skiprows=2).T
calfiles = ["meas1/850RefDipole.trx"]
reffiles = ["ref/SD850-02.ref"]
f,e = satimo.efficiency("meas1/meas1.trx", calfiles, reffiles)

subplot(221)
aauplot.efficiency(f,10*log10(e), label="SBN")
aauplot.efficiency(M[0], 10*log10(M[1]), label="SatEnv")
title("Measurement 1")
aauplot.end_efficiency(f)

# MEASUREMENT 2 ################################################################
M = loadtxt("meas2/meas2_satenv.txt", skiprows=2).T
calfiles = ["meas2/740RefDipole.trx"]
reffiles = ["ref/SD740-70.ref"]
f,e = satimo.efficiency("meas2/meas2.trx", calfiles, reffiles)

subplot(222)
aauplot.efficiency(f,10*log10(e), label="SBN")
aauplot.efficiency(M[0], 10*log10(M[1]), label="SatEnv")
title("Measurement 2")
aauplot.end_efficiency(f)

# MEASUREMENT 3 ################################################################
M = loadtxt("meas3/meas3_satenv.txt", skiprows=2).T
calfiles = ["meas3/2450RefDipole.trx"]
reffiles = ["ref/SD2450-43.ref"]
f,e = satimo.efficiency("meas3/meas3.trx", calfiles, reffiles)

subplot(223)
aauplot.efficiency(f,10*log10(e), label="SBN")
aauplot.efficiency(M[0], 10*log10(M[1]), label="SatEnv")
title("Measurement 3")
aauplot.end_efficiency(f)

savefig("efficiency.pdf")
# show()
