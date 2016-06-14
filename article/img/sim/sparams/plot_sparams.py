from numpy import *
from matplotlib.pyplot import *
import paperplot
from glob import glob

files = sorted(glob("top/S1,1*"),key=lambda name: int(name[10:-1]))
filesSide = sorted(glob("side/S2,2*"),key=lambda name: int(name[11:-1]))
paperplot.figure(figsize=(3.5, 3.5))
f_min = array([])
s11_min = array([])

f_minSide = array([])
s22_min = array([])

for i in range(len(files)):
    print(files[i])
    m = loadtxt(files[i], skiprows=2, delimiter=None, usecols=(0,1))
    f = m[:,0].T
    s11 = m[:,1].T
    print(f)
    print(s11)
    if (i == 0):
        f_min = f
        s11_min = s11
        subplot(211)
        paperplot.sparam(f, s11, '-k',  label="$S_{11}[0]$")
    else:
        s11_min = minimum(s11_min, s11)


for i in range(len(filesSide)):
    print(filesSide[i])
    m = loadtxt(filesSide[i], skiprows=2, delimiter=None, usecols=(0,1))
    f = m[:,0].T
    s22 = m[:,1].T
    if (i == 0):
        f_minSide = f
        s22_min = s11
        subplot(212)
        paperplot.sparam(f, s22, '-k',  label="$S_{22}[0]$")
    else:
        s22_min = minimum(s22_min, s22)
        

        
subplot(211)
paperplot.sparam(f_min, s11_min, color=[0.6,0.6,0.6], linestyle='-',
        label="$\min(S_{11})$")
paperplot.end_sparam(loc=4, ncol=1, handlelength=1)

subplot(212)
paperplot.sparam(f_minSide, s22_min, color=[0.6,0.6,0.6], linestyle='-',
        label="$\min(S_{22})$")
paperplot.end_sparam(loc=4, ncol=1, handlelength=1)


savefig("sparams.pdf")
show()


