import satimo
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
plot(f/1e6, eff)
grid()
xlabel("Frequency [MHz]")
ylabel("Efficiency [.]")
savefig("003-top-ant_eff.pdf")
show()
