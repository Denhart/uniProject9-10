import satimo
import aauplot
from numpy import *
from matplotlib.pyplot import *

# Low band
f1,h1,v1 = satimo.loadtrx("triag_top_horiz_lb.trx")
f2,h2,v2 = satimo.loadtrx("triag_side_horiz_lb.trx")

f_lb = f1
ecc_lb = satimo.ecc(h1,h2,v1,v2)

# High band
f1,h1,v1 = satimo.loadtrx("triag_top_horiz_hb.trx")
f2,h2,v2 = satimo.loadtrx("triag_side_horiz_hb.trx")

f_hb = f1
ecc_hb = satimo.ecc(h1,h2,v1,v2)

f_meas = hstack((f_lb, f_hb))
ecc_meas = hstack((ecc_lb, ecc_hb))

# Simulated
f_sim,ecc_sim = loadtxt("sim/corr.txt", skiprows=2).T

aauplot.figure()
aauplot.correlation(f_meas, ecc_meas, "-b", label="Measured")
aauplot.correlation(f_sim, ecc_sim, "--b", label="Simulated")
aauplot.end_correlation()

savefig("correlation.pdf")

show()
