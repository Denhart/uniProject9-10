from numpy import *
from matplotlib.pyplot import *
import paperplot
from glob import glob

files_top  = sort(glob("eff_ac1/*.txt"))
files_side = sort(glob("eff_ac2/*.txt"))

paperplot.figure(figsize=(3.5, 3.5))
f_max = array([])

# Top
subplot(211)
eff_top_max = array([])
for i in range(len(files_top)):
    m = loadtxt(files_top[i], skiprows=2).T
    f = m[0]*1e6
    eff = pow(10,(m[1]/10))


    if (i == 0):
        f_max = f
        eff_top_max = eff
        paperplot.efficiency(f/1e6, eff, '-k',  label="$\eta_0[0]$")
    else:
        eff_top_max = maximum(eff_top_max, eff)

# Side
subplot(212)
eff_side_max = array([])
for i in range(len(files_side)):
    m = loadtxt(files_side[i], skiprows=2).T
    f = m[0]*1e6
    eff = pow(10,(m[1]/10))
    if (i == 0):
        f_max = f
        eff_side_max = eff
        paperplot.efficiency(f/1e6, eff, '-k',  label="$\eta_0[0]$")
    else:
        eff_side_max = maximum(eff_side_max, eff)

subplot(211)
title("Top antenna", fontsize=8)
paperplot.efficiency(f_max/1e6, eff_top_max, color=[0.6,0.6,0.6], linestyle='-',
        label="$\max(\eta_0)$")
paperplot.end_efficiency(loc=8, ncol=2, handlelength=1)

subplot(212)
title("Side antenna", fontsize=8)
paperplot.efficiency(f_max/1e6, eff_side_max, color=[0.6,0.6,0.6], linestyle='-',
        label="$\max(\eta_0)$")
paperplot.end_efficiency(loc=8, ncol=2, handlelength=1)

savefig("efficiency.pdf")
show()

