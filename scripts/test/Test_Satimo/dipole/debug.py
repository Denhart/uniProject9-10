from numpy import *
from matplotlib.pyplot import *
import satimo

reffiles = ["SD2450-43.ref"]
calfiles = ["dipole.trx"]

f,e = satimo.efficiency("dipole.trx", calfiles, reffiles)

M = loadtxt(reffiles[0], skiprows=5).T
f_,eff_ = M[0]*1e6, 10**(M[3]/10)

M = loadtxt("Eff_ref2450_satEnv.txt", skiprows=2).T

plot(f,e, label="Our")
plot(f_,eff_, label="Reference file")
plot(M[0], M[1], label="SatEnv")
# plot(S[0]*1e6, 10**(S[1]/10), label="Samantha")

legend()
show()
