from numpy import *
from matplotlib.pyplot import *
import aauplot

aauplot.figure()
lam = 3e8/2600e6
d = linspace(0.1, 1000, 1000)
FSPL = (4*pi*d/lam)**2

plot(d, 10*log10(FSPL))
xlim(0, 1000)
ylim(0, 120)
grid(True)
xlabel("Distance [m]")
ylabel("Path loss [dB]")
tight_layout()
savefig("distancePathloss.pdf")
show()
