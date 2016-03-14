from numpy import *
from matplotlib.pyplot import *
import aauplot
import satimo

reffiles = [
        "ref/HomeRef600.ref",
        "ref/SD740-70.ref",
        "ref/SD850-02.ref",
        "ref/SD900-51.ref",
        "ref/SD1800-45.ref",
        "ref/SD2050-36.ref",
        "ref/SD2450-43.ref",
        ]

calfiles = [
        "data/Satimo/665RefDipole.trx",
        "data/Satimo/740RefDipole.trx",
        "data/Satimo/850RefDipole.trx",
        "data/Satimo/900RefDipole.trx",
        "data/Satimo/1800RefDipole.trx",
        "data/Satimo/2050RefDipole.trx",
        "data/Satimo/2450RefDipole.trx",
        ]

f_tot,P_tot = satimo.totalpower_table(calfiles, reffiles)
datadir = "data/Satimo/"
avg = 20

# TOP ANTENNA ##################################################################
aauplot.figure()
for x in [
        ["triag-0.3--LB-Top-H.trx", "triag-0.3--HB-Top-H.trx"],
        ["triag-0.7--LB-Top-H.trx", "triag-0.7--HB-Top-H.trx"],
        ["triag-1.1--LB-Top-H.trx", "triag-1.1--HB-Top-H.trx"],
        ["triag-1.5--LB-Top-H.trx", "triag-1.5--HB-Top-H.trx"],
        ["triag-2.0--LB-Top-H.trx", "triag-2.0--HB-Top-H.trx"],
        ["triag-2.7--LB-Top-H.trx", "triag-2.7--HB-Top-H.trx"],
        ["triag-3.0--LB-Top-H.trx", "triag-3.0--HB-Top-H.trx"],
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
        ["triag-0.3--LB-Side-H.trx", "triag-0.3--HB-Side-H.trx"],
        ["triag-0.7--LB-Side-H.trx", "triag-0.7--HB-Side-H.trx"],
        ["triag-1.1--LB-Side-H.trx", "triag-1.1--HB-Side-H.trx"],
        ["triag-1.5--LB-Side-H.trx", "triag-1.5--HB-Side-H.trx"],
        ["triag-2.0--LB-Side-H.trx", "triag-2.0--HB-Side-H.trx"],
        ["triag-2.7--LB-Side-H.trx", "triag-2.7--HB-Side-H.trx"],
        ["triag-3.0--LB-Side-H.trx", "triag-3.0--HB-Side-H.trx"],
        ]:

    f_L,eff_L = satimo.efficiency(datadir + x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(datadir + x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff)

aauplot.end_efficiency(loc=4);
savefig("efficiency_side.pdf")

show()
