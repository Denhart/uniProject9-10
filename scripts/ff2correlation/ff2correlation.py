from numpy import *
from matplotlib.pyplot import *
import l3d
import satimo
import cst


if __name__ == "__main__":
    # CST Example ##############################################################
    # M1 = cst.loadfile("cst_870_top.txt")
    # M2 = cst.loadfile("cst_870_side.txt")

    # Ft1 = cst.ff2mat(M1, 3, 4)
    # Fp1 = cst.ff2mat(M1, 5, 6)

    # Ft2 = cst.ff2mat(M2, 3, 4)
    # Fp2 = cst.ff2mat(M2, 5, 6)

    # ECC = l3d.ecc(Ft1, Ft2, Fp1, Fp2)
    # print(ECC)
    ############################################################################

    # SATIMO Example ###########################################################
    M1 = satimo.loadfile("satimo_ifa.txt")
    M2 = satimo.loadfile("satimo_slot.txt")

    Ft1 = satimo.ff2mat(M1, 4, 5)
    Fp1 = satimo.ff2mat(M1, 2, 3)
    Ft2 = satimo.ff2mat(M2, 4, 5)
    Fp2 = satimo.ff2mat(M2, 2, 3)

    ECC = l3d.ecc(Ft1, Ft2, Fp1, Fp2)

    Etot = sqrt(abs(Ft2)**2 + abs(Fp2)**2)
    l3d.plotflat(Etot)
    show()
    print(ECC)
    ############################################################################

