from numpy import *
from matplotlib.pyplot import *
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Plot a farfield-matrix as a color-map. Remember that 0 degrees is the bottom
# of the plot in spherical coordinates.
#
# @param r Matrix to plot (theta x phi).
# @param th_lim Minimum and maximum theta/y-axis value (degrees).
# @param ph_lim Minimum and maximum phi/x-axis value (degrees).
# @param cmap Color map to use.
def plotflat(r, th_lim=(0,180), ph_lim=(0,360), cmap="jet"):
    nx, ny = shape(r.T)
    phmin = ph_lim[0]
    phmax = ph_lim[1]
    thmin = th_lim[0]
    thmax = th_lim[1]
    x = linspace(phmin, phmax, nx)
    y = linspace(thmin, thmax, ny)
    X,Y = meshgrid(x,y)
    pcolor(X,Y,r, cmap=cmap)
    xlim(phmin,phmax)
    ylim(thmin,thmax)
    grid(True)
    colorbar()
    xlabel("$\phi$ [degrees]")
    ylabel("$\\theta$ [degrees]")

# Plot a matrix, (theta x phi), in 3d space.
#
# @param r Matrix to plot.
# @param stride Resolution of the output. 1=detailed+slow, 10=rough+fast.
# @param th_lim Upper and lower theta limits (degrees).
# @param ph_lim Upper and lower phi limits (degrees).
def plot3d(r, stride=1, th_lim=(0, 180), ph_lim=(0, 360)):
    ax = subplot(111, projection="3d")

    ntheta, nphi = r.shape

    theta = linspace(th_lim[0], th_lim[1], ntheta)*pi/180  # include 0 deg
    phi = linspace(ph_lim[0], ph_lim[1], nphi)*pi/180

    x = r*outer(sin(theta), cos(phi))
    y = r*outer(sin(theta), sin(phi))
    z = r*outer(cos(theta), ones_like(phi))

    ax.plot_surface(x,y,z, cstride=stride, rstride=stride, facecolors=cm.jet(r/r.max()), linewidth=0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

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
    XPR12 = intsphere(abs(Eth2)**2, theta, phi) / intsphere(abs(Eph1)**2, theta, phi)
    XPR11 = intsphere(abs(Eth1)**2, theta, phi) / intsphere(abs(Eph1)**2, theta, phi)
    XPR22 = intsphere(abs(Eth2)**2, theta, phi) / intsphere(abs(Eph2)**2, theta, phi)

    Pt = 1 / (4*pi)
    Pp = 1 / (4*pi)

    A = lambda Etm,Etn,Epm,Epn,XPR: XPR*Etm*conj(Etn)*Pt + Epm*conj(Epn)*Pp

    I1 = intsphere(A(Eth1,Eth2,Eph1,Eph2,XPR12), theta,phi)
    I2 = intsphere(A(Eth1,Eth1,Eph1,Eph1,XPR11), theta,phi)
    I3 = intsphere(A(Eth2,Eth2,Eph2,Eph2,XPR22), theta,phi)
    return abs(I1/sqrt(I2*I3))**2
