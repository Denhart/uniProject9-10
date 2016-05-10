from numpy import *
from matplotlib.pyplot import *
import cst
import l3d

T,P = cst.loadff("cst_farfield.txt")

E = sqrt(abs(T)**2 + abs(P)**2)

figure()
l3d.plot3d(E, stride=10)
savefig("ex3_3dfarfield.pdf")

figure()
l3d.plotflat(E)
savefig("ex3_2dfarfield.pdf")
show()
