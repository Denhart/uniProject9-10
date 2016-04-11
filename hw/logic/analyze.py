from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure(figsize=(7,3))
m = loadtxt("avr_rffe_reg1_0x00.csv", delimiter=",", skiprows=1).T
step(1e6*m[0], m[1]+0.7, '-k')
step(1e6*m[0], m[2]-0.7, '-k')
yticks([0.5-0.7, 0.5+0.7, 1+1.4], ["SCLK", "SDATA", "Decoded"], rotation=90)
xlim(-1.5,14.5)
ylim(-1, 3)
xlabel("Time [$\mu$s]")

xstart = -0.97
xstep = 0.6192
yval = 1.4+1
for x in [
        [xstart, xstep, "S"],
        [xstart+xstep, 4*xstep, "Slave address\n0x07"],
        [xstart+5*xstep, 3*xstep, "Write\nregister cmd\n0x02"],
        [xstart+8*xstep, 5*xstep, "Register\n0x01"],
        [xstart+13*xstep, 1*xstep, "P\n1"],
        [xstart+14*xstep, 8*xstep, "Register value\n0x00"],
        [xstart+22*xstep, 1*xstep, "P\n1"],
        [xstart+23*xstep, 1*xstep, "BP"],
        ]:
    dx,dy = 0.1, 0.35
    xx = array([
        x[0], x[0]+dx, x[0]+x[1]-dx, x[0]+x[1], 
        x[0]+x[1]-dx, x[0]+dx, x[0] ])
    yy = array([yval, yval+dy, yval+dy, yval, 
        yval-dy, yval-dy, yval])
    plot(xx,yy, '-k')
    annotate(x[2], xy=(x[0]+x[1]/2, yval), ha="center", va="center")

tight_layout()
savefig("avr_rffe_reg1_0x00.pdf")
# show()
