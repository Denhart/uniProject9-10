from numpy import *
from matplotlib.pyplot import *

rcParams['font.family'] = "serif" 
rcParams['font.size'] = "8" 
rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
rcParams['text.usetex'] = 'true'

m = loadtxt("avr_rffe_reg1_0x00.csv", delimiter=",", skiprows=1).T
plot(m[0], m[1])
plot(m[0], m[2])
show()
