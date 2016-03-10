import satimo
import aauplot
from numpy import *
from matplotlib.pyplot import *


# Calibration measurements
calfiles = [
        "calib/600RefDipole.trx",
        "calib/740RefDipole.trx",
        "calib/850RefDipole.trx",
        "calib/900RefDipole.trx",
        "calib/1800RefDipole.trx",
        "calib/2050RefDipole.trx",
        "calib/2450RefDipole.trx",
        ]

# Reference files
reffiles = [
        "calib/HomeRef600.ref",
        "calib/SD740-70.ref",
        "calib/SD850-02.ref",
        "calib/SD900-51.ref",
        "calib/SD1800-45.ref",
        "calib/SD2050-36.ref",
        "calib/SD2450-43.ref",
        ]

f_tot,P_tot = satimo.totalpower_table(calfiles, reffiles)

aauplot.figure()
for x in [
        ["triag_top_horiz_lb.trx","triag_top_horiz_hb.trx","Top horizontal"],
        ["triag_side_horiz_lb.trx","triag_side_horiz_hb.trx","Side horizontal"],
        ]:

    f_L,eff_L = satimo.efficiency(x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((f_L,f_H))
    eff = hstack((eff_L,eff_H))

    aauplot.efficiency(f,eff,label=x[2])

# Simulations for comparison
M1 = loadtxt("sim/top_09pf.txt", skiprows=2).T
M2 = loadtxt("sim/side_03pf.txt", skiprows=2).T

aauplot.efficiency(f, interp(f, M1[0], M1[1]), label="Top, simulated")
aauplot.efficiency(f, interp(f, M2[0], M2[1]), label="Side, simulated")

aauplot.end_efficiency(loc=4);

savefig("efficiency.pdf")
show()
