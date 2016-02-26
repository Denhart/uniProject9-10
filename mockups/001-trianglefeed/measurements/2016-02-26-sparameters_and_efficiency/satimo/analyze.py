import satimo
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

for x in [
        ["Triag-LB-Top-H.trx","Triag-HB-Top-H.trx","Top horizontal",221],
        ["Triag-LB-Top-V.trx","Triag-HB-Top-V.trx","Top vertical",222],
        ["Triag-LB-Side-H.trx","Triag-HB-Side-H.trx","Side horizontal",223],
        ["Triag-LB-Side-V.trx","Triag-HB-Side-V.trx","Side vertical",224],
        ]:

    f_L,eff_L = satimo.efficiency(x[0], calfiles, reffiles)
    f_H,eff_H = satimo.efficiency(x[1], calfiles, reffiles)

    f = hstack((f_L,f_H))
    eff = hstack((eff_L,eff_H))

    subplot(x[3])
    plot(f/1e6, eff)
    title(x[2])
    grid()
    xlabel("Frequency [MHz]")
    ylabel("Efficiency [.]")
    tight_layout()

savefig("efficiency.pdf")
show()
