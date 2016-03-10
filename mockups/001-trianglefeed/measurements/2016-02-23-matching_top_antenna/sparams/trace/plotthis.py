from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'
#
# rcParams['font.family'] = "Times New Roman"
# rcParams['font.size'] = "8"

x = loadtxt('b.csv', delimiter=',', skiprows=1).T
plot(x[0], x[1])
show()
