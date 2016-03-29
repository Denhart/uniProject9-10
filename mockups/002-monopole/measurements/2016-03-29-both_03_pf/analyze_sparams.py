from numpy import *
from matplotlib.pyplot import *
import aauplot

# Top antenna = S22
# Side antenna = S11
f,S22,S22_,S11,S21 = loadtxt("sparams/lasse_03_03.csv", skiprows=3).T

aauplot.figure()
aauplot.sparam(f,S11,label="S11")
aauplot.sparam(f,S21,label="S21")
aauplot.sparam(f,S22,label="S22")

aauplot.end_sparam(loc=4)

savefig("sparams.pdf")
show()
