from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()

m1 = loadtxt("sar_top.csv", delimiter=",").T
m2 = loadtxt("sar_side.csv", delimiter=",").T
aauplot.sar(m1[0], m1[1], label="Top")
aauplot.sar(m2[0], m2[1], label="Side")

aauplot.end_sar()

savefig("Top_antenna.pdf")
show()