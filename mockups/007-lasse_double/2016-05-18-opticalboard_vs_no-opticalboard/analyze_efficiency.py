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
avg = 25
aauplot.figure()

# TOP ANTENNA ##################################################################
print("Processing top antenna...")

f_L,eff_L = satimo.efficiency("satimo/antenna/wonder_top_horiz_0_0-LB.trx", f_tot=f_tot, P_tot=P_tot)
f_H,eff_H = satimo.efficiency("satimo/antenna/wonder_top_horiz_0_0-HB.trx", f_tot=f_tot, P_tot=P_tot)
f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))
aauplot.efficiency(f,eff, '-b', label="Top $+$ RFFE")

f_L,eff_L = satimo.efficiency("satimo/antenna/wonder-top-noOptical--LB-H.trx", f_tot=f_tot, P_tot=P_tot)
f_H,eff_H = satimo.efficiency("satimo/antenna/wonder-top-noOptical--HB-H.trx", f_tot=f_tot, P_tot=P_tot)
f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))
aauplot.efficiency(f,eff, '--c', label="Top $-$ RFFE")

# SIDE ANTENNA #################################################################
print("Processing side antenna...")

f_L,eff_L = satimo.efficiency("satimo/antenna/wonder_side_horiz_0_0_0_0-LB.trx", f_tot=f_tot, P_tot=P_tot)
f_H,eff_H = satimo.efficiency("satimo/antenna/wonder_side_horiz_0_0_0_0-HB.trx", f_tot=f_tot, P_tot=P_tot)
f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))
aauplot.efficiency(f,eff, '-g', label="Side $+$ RFFE")

f_L,eff_L = satimo.efficiency("satimo/antenna/wonder-side-noOptical--LB-H.trx", f_tot=f_tot, P_tot=P_tot)
f_H,eff_H = satimo.efficiency("satimo/antenna/wonder-side-noOptical--HB-H.trx", f_tot=f_tot, P_tot=P_tot)
f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))
aauplot.efficiency(f,eff, '--y', label="Side $-$ RFFE")

aauplot.end_efficiency(loc=8, ncol=2);
savefig("efficiency.pdf")

show()
