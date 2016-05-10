import satimo
from numpy import *

calfiles = ["calib/calib2450.trx"]
reffiles = [
        "calib/SD740-70.ref",
        "calib/SD850-02.ref",
        "calib/SD900-51.ref",
        "calib/SD1800-45.ref",
        "calib/SD1900-49.ref",
        "calib/SD2050-36.ref",
        "calib/SD2450-43.ref",
        "calib/SD2600-28.ref",
        ]

f,eff = satimo.efficiency("antenna_meas.trx", calfiles, reffiles)
savetxt("ex4_efficiency.txt", transpose([f, eff]))
