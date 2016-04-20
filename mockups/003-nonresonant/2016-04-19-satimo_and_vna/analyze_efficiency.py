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

f_tot,P_tot = satimo.totalpower_table(calfiles, reffiles)
datadir = "satimo/antenna/"
avg = 20

# TOP ANTENNA ##################################################################
aauplot.figure()
for x in [
        ["henrik-0.3--LB-Top-H.trx", "henrik-0.3--HB-Top-H.trx"],
        ["henrik-0.7--LB-Top-H.trx", "henrik-0.7--HB-Top-H.trx"],
        ["henrik-1.1--LB-Top-H.trx", "henrik-1.1--HB-Top-H.trx"],
        ["henrik-1.5--LB-Top-H.trx", "henrik-1.5--HB-Top-H.trx"],
        ["henrik-2.0--LB-Top-H.trx", "henrik-2.0--HB-Top-H.trx"],
        ["henrik-2.7--LB-Top-H.trx", "henrik-2.7--HB-Top-H.trx"],
        ["henrik-3.0--LB-Top-H.trx", "henrik-3.0--HB-Top-H.trx"],
        ]:

    f_L,eff_L = satimo.efficiency(datadir + x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(datadir + x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff)

aauplot.end_efficiency(loc=4);
savefig("efficiency_top.pdf")

# SIDE ANTENNA #################################################################
aauplot.figure()
for x in [
        ["henrik-side--LB-Side-H.trx", "henrik-side--HB-Side-H.trx"],
        ]:

    f_L,eff_L = satimo.efficiency(datadir + x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(datadir + x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff)

aauplot.end_efficiency(loc=4);
savefig("efficiency_side.pdf")

show()