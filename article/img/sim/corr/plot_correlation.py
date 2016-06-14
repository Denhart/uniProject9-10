from numpy import *
from matplotlib.pyplot import *
import paperplot
from glob import glob

files_top  = sort(glob("top/C1*"))
files_side = sort(glob("side/run*"))

paperplot.figure(figsize=(3.5, 3.5))
f_max = array([])

# Top
subplot(211)
eff_top_max = array([])
for i in range(len(files_top)):
    m = loadtxt(files_top[i], skiprows=2).T
    f = m[0]*1e6
    eff = m[1]
    if (i == 0):
        f_max = f
        eff_top_max = eff
        paperplot.correlation(f/1e6, eff, '-k',  label="$\mathrm{ECC}[0]$")
    else:
        eff_top_max = maximum(eff_top_max, eff)

# Side
subplot(212)
eff_side_max = array([])
for i in range(len(files_side)):
    m = loadtxt(files_side[i], skiprows=2).T
    f = m[0]*1e6
    eff = m[1]
    if (i == 0):
        f_max = f
        eff_side_max = eff
        paperplot.correlation(f/1e6, eff, '-k',  label="$\mathrm{ECC}[0]$")
    else:
        eff_side_max = maximum(eff_side_max, eff)

subplot(211)
title("Top antenna", fontsize=8)
paperplot.correlation(f_max/1e6, eff_top_max, color=[0.6,0.6,0.6], linestyle='-',
                      label="$\max(\mathrm{ECC})$")
paperplot.end_correlation(loc=1, ncol=2, handlelength=1)

subplot(212)
title("Side antenna", fontsize=8)
paperplot.correlation(f_max/1e6, eff_side_max, color=[0.6,0.6,0.6], linestyle='-',
                      label="$\max(\mathrm{ECC})$")
paperplot.end_correlation(loc=1, ncol=2, handlelength=1)

savefig("correlation.pdf")
show()

