from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'

M = loadtxt("03_sparams.csv", skiprows=3).T
f = M[0]/1e6
s12 = 20*log10(abs(M[1] + 1j*M[2]))
s21 = 20*log10(abs(M[3] + 1j*M[4]))
s22 = 20*log10(abs(M[5] + 1j*M[6]))
s11 = 20*log10(abs(M[7] + 1j*M[8]))

figure(1), clf()
plot(f, s11, label="S11")
plot(f, s12, label="S12")
plot(f, s21, label="S21")
plot(f, s22, label="S22")

ylim(-24,0)
yticks([-24,-18,-12,-6,0])

xlim(f.min(), f.max())
xticks([700, 960, 1710, 2650])
grid(1)

legend(fontsize=10)
