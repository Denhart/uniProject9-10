from numpy import *
from matplotlib.pyplot import *
import satimo
import l3d

f,h,v = satimo.loadtrx("antenna_meas.trx")

# Choosing one specific frequency
print("Farfield frequency: %.2f GHz" % (f[0]/1e9))
h = h[0]
v = v[0]

E = sqrt(abs(h)**2 + abs(v)**2)
thetamax = (180-22.5) * pi/180 # No probe at theta = 180

figure()
l3d.plot3d(E, th_lim=(0, thetamax))
savefig("ex2_3dfarfield.pdf")

figure()
l3d.plotflat(E, th_lim=(0, thetamax))
savefig("ex2_2dfarfield.pdf")

show()
