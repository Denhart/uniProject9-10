from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'

# Measurements
M = loadtxt("03_sparams.csv", skiprows=3).T
f_m = M[0]/1e6
s12_m = 20*log10(abs(M[1] + 1j*M[2]))
s21_m = 20*log10(abs(M[3] + 1j*M[4]))
s22_m = 20*log10(abs(M[5] + 1j*M[6]))
s11_m = 20*log10(abs(M[7] + 1j*M[8]))

# Simulations
s11data = genfromtxt("03_sparams_cst.txt", skip_header=2, max_rows=1000).T
s12data = genfromtxt("03_sparams_cst.txt", skip_header=1006, max_rows=1000).T
s21data = genfromtxt("03_sparams_cst.txt", skip_header=2010, max_rows=1000).T
s22data = genfromtxt("03_sparams_cst.txt", skip_header=3014, max_rows=1000).T
f_s = s11data[0]
s11_s = s11data[1]
s12_s = s12data[1]
s21_s = s21data[1]
s22_s = s22data[1]

figure(1), clf()
plot(f_m, s11_m, '-b', label="S11 meas")
plot(f_m, s12_m, '-g', label="S12 meas")
plot(f_m, s21_m, '-r', label="S21 meas")
plot(f_m, s22_m, '-c', label="S22 meas")

plot(f_s, s11_s, '--b', label="S11 sim")
plot(f_s, s12_s, '--g', label="S12 sim")
plot(f_s, s21_s, '--r', label="S21 sim")
plot(f_s, s22_s, '--c', label="S22 sim")

ylim(-24,0)
yticks([-24,-18,-12,-6,0])

xlim(f_m.min(), f_m.max())
xticks([700, 960, 1710, 2650])
grid(1)

legend(fontsize=10)
show(1)
