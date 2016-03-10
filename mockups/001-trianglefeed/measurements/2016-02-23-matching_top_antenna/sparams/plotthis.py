from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'
#
# rcParams['font.family'] = "Times New Roman"
# rcParams['font.size'] = "8"

files = ["05", "07", "09", "11"]

for f in files:
    m = loadtxt("%s.csv"%f, delimiter=",").T
    plot(m[0], m[1], label="%c.%c pF"%(f[0],f[1]))

legend(fontsize=12, loc=3)
xlim(500, 3000)
ylim(-24, 0)
yticks([-24,-18,-12,-6,0])
xticks([500,690,960,1710,2650,3000])
xlabel("Frequency [MHz]")
ylabel("S11")
grid()

savefig("s11.pdf")
show()
