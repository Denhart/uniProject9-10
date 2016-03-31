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
avg = 80

# TOP ANTENNA ##################################################################
aauplot.figure()
for x in [
        #["lasse-LB-Top-H.trx", "lasse-HB-Top-H.trx", "Top H"],
        ["lasse-LB-Top-V.trx", "lasse-HB-Top-V.trx", "Top V"],
        #["lasse-LB-Side-H.trx", "lasse-HB-Side-H.trx", "Side H"],
        ["lasse-LB-Side-V.trx", "lasse-HB-Side-V.trx", "Side V"],
        ]:

    f_L,eff_L = satimo.efficiency(datadir + x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(datadir + x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((satimo.ma(f_L,avg),satimo.ma(f_H,avg)))
    eff = hstack((satimo.ma(eff_L,avg), satimo.ma(eff_H,avg)))

    aauplot.efficiency(f,eff,label=x[2])
    
#Simulation
M1 = loadtxt("sim/eff_top.txt", skiprows=2).T
M2 = loadtxt("sim/eff_side.txt", skiprows=2).T

aauplot.efficiency(f, interp(f, M1[0]*1000, M1[1]), "--b", label="Top, sim")
aauplot.efficiency(f, interp(f, M2[0]*1000, M2[1]), "--g", label="Side, sim")
  
aauplot.end_efficiency(loc=4);
savefig("efficiency.pdf")

show()
