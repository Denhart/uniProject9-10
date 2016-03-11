from numpy import *
from matplotlib.pyplot import *
import satimo

reffiles = ["calib/SD2450-43.ref"]
calfiles = ["calib/ff_sweep_SPM.trx"]

f,e = satimo.efficiency("SPM_sweep.trx", calfiles, reffiles)
print(f,e)

M = loadtxt("eff_sweep_satenv.txt", skiprows=2).T

S = loadtxt("SamanthaScriptEff/effDataSam", delimiter=",").T

plot(f,e, label="Our")
plot(M[0], M[1], label="SatEnv")
plot(S[0]*1e6, 10**(S[1]/10), label="Samantha")

legend()
show()
