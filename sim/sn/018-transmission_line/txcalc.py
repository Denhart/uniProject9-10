from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'

def mm2in(mm):
    return mm/25.4

def in2mm(mm):
    return mm*25.4

h = mm2in(1.6)
w = mm2in(2.9)
t = mm2in(0.035)
eps = 4.5

Zin = 87/sqrt(eps+1.41) * log(5.98*h/(0.8*w + t))

print("0.1 < w/h < 2.0?", (w/h))
print("1 < eps_r < 15?", eps)
print("Zin:", Zin)
print("")
print("Dimensions: h="+str(in2mm(h))+" w="+str(in2mm(w)))


