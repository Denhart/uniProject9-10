from numpy import *
from matplotlib.pyplot import *
import aauplot
from glob import glob

vnadir = "vna/"
filelist = sort(glob(vnadir + "*.s2p"))

for i in [1,2,3]:
    aauplot.figure(i)

for fil in filelist:
    m = loadtxt(fil, skiprows=5).T
    f = m[0]
    s11 = 20*log10(m[1] + 1j*m[2])
    s21 = 20*log10(m[3] + 1j*m[4])
    s12 = 20*log10(m[5] + 1j*m[6])
    s22 = 20*log10(m[7] + 1j*m[8])

    figure(1)
    aauplot.sparam(f, s11)

    figure(2)
    aauplot.sparam(f, s22)

    figure(3)
    aauplot.sparam(f, s21)

for i in [[1,"S11"],[2,"S22"],[3,"S21"]]:
    figure(i[0])
    aauplot.end_sparam()
    savefig(i[1] + ".pdf")

show()
