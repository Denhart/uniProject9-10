from numpy import *
from matplotlib.pyplot import *

# Plot a farfield-matrix as a color-map.
#
# @param r Matrix to plot (theta x phi).
# @param x_lim Minimum and maximum x-axis value.
# @param y_lim Minimum and maximum y-axis value.
def plotflat(r, x_lim=(0,360), y_lim=(0,180), cmap="jet"):
    nx, ny = shape(r.T)
    x = linspace(x_lim[0], x_lim[1], nx)
    y = linspace(y_lim[0], y_lim[1], ny)
    X,Y = meshgrid(x,y)
    pcolor(X,Y,r, cmap=cmap)
    xlim(*x_lim)
    ylim(*y_lim)
    grid(True)
    colorbar()

# Do a spherical integral of a theta-phi matrix.
#
# @param r Matrix to integrate (x-axis=phi, y-axis=theta).
# @param phi Phi axis values.
# @param theta Theta axis values.
# @return Scalar result of the integration.
def intsphere(r, theta, phi):
    return trapz(trapz(r, phi) * sin(theta), theta)

# Compute the envelope correlation coefficient between two farfields. The
# farfields are split into theta and phi part. Each part is a matrix with
# theta on one axis and phi on the other.
#
# @param Eth1 E-field, theta part, antenna 1
# @param Eth2 E-field, theta part, antenna 2
# @param Eph1 E-field, phi part, antenna 1
# @param Eph1 E-field, phi part, antenna 2
# @return Envelope Correlation Coefficient (scalar)
#
# @note https://mns.ifn.et.tu-dresden.de/Lists/nPublications/Attachments/612/Wang_Q_WSA_10.pdf
def ecc(Eth1, Eth2, Eph1, Eph2):
    # Axes
    ntheta,nphi = Eth1.shape
    phi = linspace(0, 2*pi, nphi)
    theta = linspace(0, pi, ntheta)

    # Correlation
    Pv = intsphere(abs(Eth1)**2, theta, phi)
    Ph = intsphere(abs(Eph1)**2, theta, phi)
    XPR = Pv/Ph

    Pt = 1 / (4*pi)
    Pp = 1 / (4*pi)

    A = lambda Etm,Etn,Epm,Epn: XPR*Etm*conj(Etn)*Pt + Epm*conj(Epn)*Pp

    I1 = intsphere(A(Eth1,Eth2,Eph1,Eph2), theta,phi)
    I2 = intsphere(A(Eth1,Eth1,Eph1,Eph1), theta,phi)
    I3 = intsphere(A(Eth2,Eth2,Eph2,Eph2), theta,phi)
    return abs(I1/sqrt(I2*I3))**2
