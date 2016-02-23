import satimo
import l3d
from numpy import *
from matplotlib.pyplot import *

# Calibration measurements
calfiles = [
        "calib/600RefDipole.trx",
        "calib/700RefDipole.trx",
        "calib/800RefDipole.trx",
        "calib/900RefDipole.trx",
]

# Reference files
reffiles = [
        "calib/HomeRef600.ref",
        "calib/SD740-70.ref",
        "calib/SD850-02.ref",
        "calib/SD900-51.ref",
]
f,eff = satimo.efficiency("003-top-ant.trx", calfiles, reffiles)

figure(1)
plot(f/1e6, eff)
grid()
xlabel("Frequency [MHz]")
ylabel("Efficiency [.]")
savefig("003-top-ant_eff.pdf")

f,h,v = satimo.loadtrx("003-top-ant.trx")
E = sqrt(abs(h[-1])**2 + abs(v[-1])**2)
th_max = pi/180 * (180-22.5)
figure(2)
l3d.plot3d(E, th_lim=(0, th_max))

figure(3)
l3d.plotflat(E, th_lim=(0, th_max))

show()
