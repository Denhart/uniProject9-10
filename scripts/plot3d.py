#!/usr/bin/python3
from numpy import *
from matplotlib.pyplot import *
import argparse
import l3d
import satimo
import cst

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("fname", help="farfield file to plot")
    p.add_argument("-s", "--satimo", help="input file is from Satimo", action="store_true")
    p.add_argument("-c", "--cst", help="input file is from CST", action="store_true")
    args = p.parse_args()

    if args.satimo and args.cst:
        print("Could not determine whether CST or Satimo files.")
        exit()
    elif args.satimo:
        M1 = satimo.loadfile(args.fname)

        Ft1 = satimo.ff2mat(M1, 4, 5)
        Fp1 = satimo.ff2mat(M1, 2, 3)

        Etot = sqrt(abs(Ft1)**2 + abs(Fp1)**2)
        ECC = l3d.plot3d(Etot, 2)
    elif args.cst:
        M1 = cst.loadfile(args.fname)

        Ft1 = cst.ff2mat(M1, 3, 4)
        Fp1 = cst.ff2mat(M1, 5, 6)

        Etot = sqrt(abs(Ft1)**2 + abs(Fp1)**2)
        ECC = l3d.plot3d(Etot, 10)
    else:
        print("Please specify either CST or Satimo (see --help)")
        exit()

    show()
