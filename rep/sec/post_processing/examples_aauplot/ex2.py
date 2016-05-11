from numpy import *
from matplotlib.pyplot import *
import aauplot
import satimo

reffiles = [
        "satimo/ref/HomeRef600.ref",
        "satimo/ref/SD740-70.ref",
        "satimo/ref/SD850-02.ref",
        "satimo/ref/SD900-51.ref",
        "satimo/ref/SD1800-45.ref",
        "satimo/ref/SD2050-36.ref",
        "satimo/ref/SD2450-43.ref",
        ]

calfiles = [
        "satimo/cal/665RefDipole.trx",
        "satimo/cal/740RefDipole.trx",
        "satimo/cal/850RefDipole.trx",
        "satimo/cal/900RefDipole.trx",
        "satimo/cal/1800RefDipole.trx",
        "satimo/cal/2050RefDipole.trx",
        "satimo/cal/2450RefDipole.trx",
        ]

# Compute calibration table for measurement
f_tot,P_tot = satimo.totalpower_table(calfiles, reffiles)

# Load low and high band measurement
f_L,eff_L = satimo.efficiency("satimo/antenna/ant_lb.trx", f_tot=f_tot, P_tot=P_tot)
f_H,eff_H = satimo.efficiency("satimo/antenna/ant_hb.trx", f_tot=f_tot, P_tot=P_tot)

# Combine the low and high band
f = hstack((f_L,f_H))
eff = hstack((eff_L,eff_H))

# Plot the results
aauplot.figure()
aauplot.efficiency(f,eff)
aauplot.end_efficiency(loc=4);

savefig("ex2_efficiency.pdf")
show()

