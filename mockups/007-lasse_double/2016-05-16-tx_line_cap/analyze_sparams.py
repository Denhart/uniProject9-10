from numpy import *
from matplotlib.pyplot import *
import aauplot

S11 = []
S22 = []
S21 = []

m = loadtxt("lasse_03_03_03_03Ch1.csv", skiprows=3).T
f = m[0]
S11.append(m[7])
S22.append(m[6])
S21.append(m[8])

m = loadtxt("lasse_30_03_03_03Ch1.csv", skiprows=3).T
S11.append(m[7])
S22.append(m[6])
S21.append(m[8])

m = loadtxt("lasse_30_30_03_03Ch1.csv", skiprows=3).T
S11.append(m[7])
S22.append(m[6])
S21.append(m[8])

m = loadtxt("lasse_30_30_30_03Ch1.csv", skiprows=3).T
S11.append(m[7])
S22.append(m[6])
S21.append(m[8])

m = loadtxt("lasse_30_30_30_30Ch1.csv", skiprows=3).T
S11.append(m[7])
S22.append(m[6])
S21.append(m[8])

aauplot.figure()
for s in S11:
    aauplot.sparam(m[0], s)

aauplot.end_sparam()
savefig("S11.pdf")

aauplot.figure()
for s in S22:
    aauplot.sparam(m[0], s)

aauplot.end_sparam()
savefig("S22.pdf")

aauplot.figure()
for s in S21:
    aauplot.sparam(m[0], s)

aauplot.end_sparam()
savefig("S21.pdf")

show()
