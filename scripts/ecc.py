from numpy import *
from matplotlib.pyplot import *
import argparse
import l3d
import satenv
import cst

def satenv_example():
    M1 = satenv.loadfile("ff2correlation/satimo_ifa.txt")
    M2 = satenv.loadfile("ff2correlation/satimo_slot.txt")

    Ft1 = satenv.ff2mat(M1, 4, 5)
    Fp1 = satenv.ff2mat(M1, 2, 3)
    Ft2 = satenv.ff2mat(M2, 4, 5)
    Fp2 = satenv.ff2mat(M2, 2, 3)

    ECC = l3d.ecc(Ft1, Ft2, Fp1, Fp2)
    print(ECC)
    Ftot = sqrt(abs(Ft1)**2 + abs(Fp1)**2)
    l3d.plotflat(Ftot)

def cst_example():
    M1 = cst.loadfile("cst_870_top.txt")
    M2 = cst.loadfile("cst_870_side.txt")

    Ft1 = cst.ff2mat(M1, 3, 4)
    Fp1 = cst.ff2mat(M1, 5, 6)

    Ft2 = cst.ff2mat(M2, 3, 4)
    Fp2 = cst.ff2mat(M2, 5, 6)

    ECC = l3d.ecc(Ft1, Ft2, Fp1, Fp2)
    print(ECC)

if __name__ == "__main__":
    satenv_example()
    show()
    exit()
    p = argparse.ArgumentParser()
    p.add_argument("fnames", help="farfield files to compute correlation for", nargs=2)
    p.add_argument("-s", "--satenv", help="input files are from SatEnv", action="store_true")
    p.add_argument("-c", "--cst", help="input files are from CST", action="store_true")
    args = p.parse_args()

    if args.satenv and args.cst:
        print("Could not determine whether CST or SatEnv files.")
        exit()
    elif args.satenv:
        M1 = satenv.loadfile(args.fnames[0])
        M2 = satenv.loadfile(args.fnames[1])

        Ft1 = satenv.ff2mat(M1, 4, 5)
        Fp1 = satenv.ff2mat(M1, 2, 3)

        Ft2 = satenv.ff2mat(M2, 4, 5)
        Fp2 = satenv.ff2mat(M2, 2, 3)
    elif args.cst:
        M1 = cst.loadfile(args.fnames[0])
        M2 = cst.loadfile(args.fnames[1])

        Ft1 = cst.ff2mat(M1, 3, 4)
        Fp1 = cst.ff2mat(M1, 5, 6)

        Ft2 = cst.ff2mat(M2, 3, 4)
        Fp2 = cst.ff2mat(M2, 5, 6)
    else:
        print("Please specify either CST or SatEnv (see --help)")
        exit()

    ECC = l3d.ecc(Ft1, Ft2, Fp1, Fp2)
    print("ECC:", ECC)
