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
        "calib/1900RefDipole.trx",
        "calib/2050RefDipole.trx",
        "calib/2450RefDipole.trx",
        ]

# Reference files
reffiles = [
        "calib/HomeRef600.ref",
        "calib/SD740-70.ref",
        "calib/SD850-02.ref",
        "calib/SD900-51.ref",
        "calib/SD1900-49.ref",
        "calib/SD2050-36.ref",
        "calib/SD2450-43.ref",
        ]

f_tot,P_tot = satimo.totalpower_table(calfiles, reffiles)

aauplot.figure()
for x in [
        ["Triag-LB-Top-H.trx","Triag-HB-Top-H.trx","Top horizontal"],
        ["Triag-LB-Top-V.trx","Triag-HB-Top-V.trx","Top vertical"],
        ["Triag-LB-Side-H.trx","Triag-HB-Side-H.trx","Side horizontal"],
        ["Triag-LB-Side-V.trx","Triag-HB-Side-V.trx","Side vertical"],
        ]:

    f_L,eff_L = satimo.efficiency(x[0], f_tot=f_tot, P_tot=P_tot)
    f_H,eff_H = satimo.efficiency(x[1], f_tot=f_tot, P_tot=P_tot)

    f = hstack((f_L,f_H))
    eff = hstack((eff_L,eff_H))

    aauplot.efficiency(f,eff,label=x[2])

aauplot.end_efficiency(f, loc=4);

savefig("efficiency.pdf")
# show()
