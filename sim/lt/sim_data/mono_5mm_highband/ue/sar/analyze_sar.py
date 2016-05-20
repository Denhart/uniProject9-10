from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

m1 = loadtxt("SarSide.csv", delimiter=",", skiprows=1).T
m2 = loadtxt("SarTop.csv", delimiter=",", skiprows=1).T
aauplot.sar(m1[0], m1[1], label="Top")
aauplot.sar(m2[0], m2[1], label="Side")

aauplot.end_sar()

savefig("sar.pdf")
show()
