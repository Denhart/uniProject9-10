from numpy import *
from matplotlib.pyplot import *
import aauplot
import satimo
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'
#
# rcParams['font.family'] = "Times New Roman"
# rcParams['font.size'] = "8"

aauplot.figure()
M = loadtxt("Triag-Top-LB-SatEnv-Eff.txt", skiprows=2).T
aauplot.efficiency(M[0], 10*log10(M[1]), label="SatEnv")

calfiles = ["850RefDipole.trx"]
reffiles = ["SD850-02.ref"]

f,e = satimo.efficiency("Triag-Top-LB.trx", calfiles, reffiles)
aauplot.efficiency(f,10*log10(e), label="SBN")
aauplot.end_efficiency()

show()
