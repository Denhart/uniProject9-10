from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

m1 = loadtxt("sar1.txt", delimiter=",", skiprows=1).T
m2 = loadtxt("sar2.txt", delimiter=",", skiprows=1).T
aauplot.sar(m1[0], m1[1], label="Top")
aauplot.sar(m2[0], m2[1], label="Side")

aauplot.end_sar()

show()
