from numpy import *
from matplotlib.pyplot import *
rcParams['font.family'] = "serif" 
rcParams['font.size'] = "8" 
rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
rcParams['text.usetex'] = 'true'
#
# rcParams['font.family'] = "Times New Roman"
# rcParams['font.size'] = "8"

m = loadtxt("Csh1_09_Csh2_11.csv", skiprows=3).T
figure(figsize=(3.5,3))
plot(m[0]/1e6, m[1], label="S11")
plot(m[0]/1e6, m[3], label="S21")
plot(m[0]/1e6, m[5], label="S22")

xlim(500, 3000)
ylim(-24, 0)
xticks([690,960,1710,2650])
yticks([-24,-18,-12,-6,0])
grid()
legend(fontsize=8)
savefig("sparams.pdf")
show()
