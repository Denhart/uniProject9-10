from numpy import *
from matplotlib.pyplot import *
import aauplot
import satimo

datadir = "satimo/antenna/"

aauplot.figure()
for x in [
        ["henrik-0.3--HB-Top-H.trx", "henrik-side--HB-Side-H", "henrik-0.3--LB-Top-H.trx", "henrik-side--LB-Side-H", "Horizontal"],
        #["lasse-LB-Top-V.trx", "lasse-LB-Side-V.trx", "lasse-HB-Top-V.trx", "lasse-HB-Side-V.trx", "Vertical"],
        ]:

    

    f_L1,h_L1,v_L1 = satimo.loadtrx(datadir + x[0])
    f_L2,h_L2,v_L2 = satimo.loadtrx(datadir + x[1])
    f_H1,h_H1,v_H1 = satimo.loadtrx(datadir + x[2])
    f_H2,h_H2,v_H2 = satimo.loadtrx(datadir + x[3])

    ecc_L = satimo.ecc(h_L1,h_L2, v_L1,v_L2)
    ecc_H = satimo.ecc(h_H1,h_H2, v_H1,v_H2)

    f = hstack((f_L1, f_H1))
    ecc = hstack((ecc_L, ecc_H))

    aauplot.correlation(f,ecc, label=x[4])

aauplot.end_correlation(loc=4);
savefig("correlation.pdf")


show()
