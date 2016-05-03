from numpy import *
from matplotlib.pyplot import *
from glob import glob
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
avg = 20

# TOP ANTENNA ##################################################################
print("Processing top antenna...")
lb = sort(glob("satimo/antenna/*top*-LB.trx"))
hb = sort(glob("satimo/antenna/*top*-HB.trx"))

if len(lb) != len(hb):
    print("Number of LB measurements != number of HB measurements")
    exit()

aauplot.figure()
for i in range(len(lb)):
    f_L,eff_L = satimo.efficiency(lb[i], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(hb[i], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff)

aauplot.end_efficiency(loc=4);
savefig("efficiency_top.pdf")

# SIDE ANTENNA #################################################################
print("Processing side antenna...")
lb = sort(glob("satimo/antenna/*side*-LB.trx"))
hb = sort(glob("satimo/antenna/*side*-HB.trx"))

if len(lb) != len(hb):
    print("Number of LB measurements != number of HB measurements")
    exit()

aauplot.figure()
for i in range(len(lb)):
    f_L,eff_L = satimo.efficiency(lb[i], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(hb[i], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff)

aauplot.end_efficiency(loc=4);
savefig("efficiency_side.pdf")

show()
