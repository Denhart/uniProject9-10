"""
3D plot of satimo data. Plots the E-field abs.

References:
[1] http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut5.html
[2] http://stackoverflow.com/questions/15616768/distance-dependent-coloring-in-matplotlib
"""
import argparse
from numpy import *
from matplotlib import cm
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from sys import exit
# rcParams['font.family'] = "Times New Roman"
# rcParams['font.size'] = "10"

def gainColumnToMatrix(gain, nPhi, nTheta):
    d = resize(gain, (nPhi, nTheta))
    M1 = d[ix_(range(0,nPhi), range(0,int(nTheta/2)+1))]  # Include 0 deg
    M2 = d[ix_(range(0,nPhi), range(int(nTheta/2), nTheta))]  # Include 0 deg
    M2 = fliplr(M2)
    d = vstack((M2, M1)).T
    d = flipud(d)
    return d

def eFieldColumnsToMatrix(Epr, Epi, Etr, Eti, nPhi, nTheta):
    Ep = (Epr+1j*Epi)
    Et = (Etr+1j*Eti)
    Eabs = sqrt(abs(Ep)**2 + abs(Et)**2)
    d = resize(Eabs, (nPhi, nTheta))
    M1 = d[ix_(range(0,nPhi), range(0,int(nTheta/2)+1))]  # Include 0 deg
    M2 = d[ix_(range(0,nPhi), range(int(nTheta/2), nTheta))]  # Include 0 deg
    M2 = fliplr(M2)
    d = vstack((M2, M1)).T
    d = flipud(d)
    return d

def plot3d(theta, phi, r, stride=10):
    # Plotting E-field abs
    figure()
    ax = subplot(111, projection='3d')

    x = r*outer(sin(theta), cos(phi))
    y = r*outer(sin(theta), sin(phi))
    z = r*outer(cos(theta), ones_like(phi))

    # ax.plot_wireframe(x,y,z)
    print(x.shape,y.shape,z.shape)
    ax.plot_surface(x,y,z, cstride=stride, rstride=stride, facecolors=cm.jet(e/e.max()), linewidth=0)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.view_init(azim=-90, elev=90) # xy = -90,90
    show(block=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help="Far field file exported from Satimo. Must have columns: phi,theta,Epr,Epi,Etr,Eri")
    parser.add_argument('-e', '--efieldcol', help="First E-field column (E_phi_real) [default = 2].")
    parser.add_argument('-s', '--stride', help="'Stride' of 3D plot (1 = looks nice, slow, 10 = look worse, fast) [default = 2]", type=int)
    args = parser.parse_args()

    efficiency = 1
    if not args.efieldcol:
        args.efieldcol = 2
    eCol = args.efieldcol
    gainCol = 6

    if not args.stride:
        args.stride = 2

    m = loadtxt(args.fname, skiprows=4)
    nPhi = 64
    nTheta = 127

    Epr, Epi, Etr, Eti = m[:,eCol].T, m[:,eCol+1].T, m[:,eCol+2].T, m[:,eCol+3].T

    phi = linspace(0, 2*pi, 2*nPhi)
    theta = linspace(0, pi, nTheta/2+1)  # include 0 deg

    # directivity = 1/efficiency * m[:,gainCol].T
    # d = gainColumnToMatrix(directivity, nPhi, nTheta)

    e = eFieldColumnsToMatrix(Epr, Epi, Etr, Eti, nPhi, nTheta)

    plot3d(theta, phi, e, stride=args.stride)

