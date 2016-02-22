import satimo
from matplotlib.pyplot import *
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = "8"

# Calibration measurements
calfiles = [
        "calib/calib2450.trx",
]

# Reference files
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

figure(figsize=(3.5, 3)) # Figure size.
plot(f/1e9, eff)
grid()
xlabel("Frequency [GHz]")
ylabel("Efficiency [.]")
tight_layout() # Clean up figure.
savefig("ex5_efficiency.pdf")
show()

