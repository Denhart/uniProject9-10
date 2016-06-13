from numpy import *
from matplotlib.pyplot import *
import paperplot
from glob import glob

files = sort(glob("vna/*.s2p"))

paperplot.figure(figsize=(3.5, 3.5))
f_min = array([])
s11_min = array([])
s22_min = array([])
for i in range(len(files)):
    m = loadtxt(files[i], skiprows=5).T
    f = m[0]
    s11 = 20*log10(abs(m[1] + 1j*m[2]))
    s21 = 20*log10(abs(m[3] + 1j*m[4]))
    s12 = 20*log10(abs(m[5] + 1j*m[6]))
    s22 = 20*log10(abs(m[7] + 1j*m[8]))
    if (i == 0):
        f_min = f
        s11_min = s11
        s22_min = s22
        subplot(211)
        paperplot.sparam(f/1e6, s11, '-k',  label="$S_{11}[0]$")
        subplot(212)
        paperplot.sparam(f/1e6, s22, '-k', label="$S_{22}[0]$")
    else:
        s11_min = minimum(s11_min, s11)
        s22_min = minimum(s22_min, s22)

subplot(211)
paperplot.sparam(f_min/1e6, s11_min, color=[0.6,0.6,0.6], linestyle='-',
        label="$\min(S_{11})$")
paperplot.end_sparam(loc=4, ncol=1, handlelength=1)

subplot(212)
paperplot.sparam(f_min/1e6, s22_min, color=[0.6,0.6,0.6], linestyle='-',
        label="$\min(S_{22})$")
paperplot.end_sparam(loc=4, ncol=1, handlelength=1)

savefig("sparams.pdf")
show()

