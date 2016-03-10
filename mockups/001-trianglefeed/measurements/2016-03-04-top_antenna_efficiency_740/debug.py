from numpy import *
from matplotlib.pyplot import *
import satimo

reffiles = ["SD740-70.txt"]
calfiles = ["740RefDipole.trx"]

f,e = satimo.efficiency("Triag-Top-740-H.trx", calfiles, reffiles)

M = loadtxt("satenv_efficiency.txt", skiprows=2).T

plot(f,e, label="Our")
plot(M[0], M[1], label="SatEnv")

ylim(0,1)
legend()
show()
