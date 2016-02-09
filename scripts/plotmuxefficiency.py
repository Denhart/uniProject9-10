from numpy import *
from matplotlib.pyplot import *
# rcParams['font.family'] = "serif" 
# rcParams['font.size'] = "8" 
# rcParams['text.latex.preamble'] = [r'\usepackage{times}', r'\usepackage{mathptm}'] 
# rcParams['text.usetex'] = 'true'

# Sample data for
# - Csh1 = 0.3
# - Csh2 = 0.3

f = array([
    690, 780, 870, 960, 1700, 1800, 1900, 2000, 
    2100, 2200, 2300, 2400, 2500, 2600, 2700 ])
corr = array([
    0.86385048, 0.60293505, 0.23578027, 0.33591219, 0.01363163,
    0.0026207936, 0.00099476673, 0.0064184159, 0.0023931676, 
    0.00080082508, 0.00064372928, 0.0012988233, 0.0036714098, 
    0.0090974376, 0.018776168])

eff1 = array([
    -1.4913259, -1.2043077, -2.6727698, -1.7908629, -1.2199527, 
    -0.95189187, -1.0475838, -1.1644992, -1.0829572, -1.0682801, 
    -1.1758419, -1.3682495, -1.6185231, -1.9016638, -2.14748])
eff1 = 10**(eff1/10)

eff2 = array([ 
    -10.30636, -5.8769004, -1.8128462, -2.4681947, -0.44826384, 
    -0.51215651, -1.2844442, -1.6811713, -1.6057656, -1.5563981, 
    -1.6080421, -1.7273178, -1.9053317, -2.1275226, -2.3627485])
eff2 = 10**(eff2/10)


# Multiplexing efficiency
muxeff = lambda eff1,eff2,corr: 10*log10(sqrt(eff1*eff2*(1-abs(corr)**2)))

# Key values
print("Efficiencies {50%,50%}, Correlation 0.3:", muxeff(0.5,0.5,0.3), "dB")

def tab(eff1, eff2, corr):
    print("%-20s%-20s%-20s%-20s" % 
            (str(eff1), str(eff2), str(corr), 10**(muxeff(eff1,eff2,corr)/10)))

print("%-20s%-20s%-20s%-20s" % ("Efficiency 1", "Efficiency 2", "Correlation", "Mux efficiency"))
tab(1.0, 1.0, 0)
tab(1.0, 1.0, 0.9999999999999)
tab(0.5, 0.5, 0.3)
tab(0.5, 0.5, 0.5)
tab(0.5, 0.5, 0.7)
tab(0.25, 0.5, 0.3)
tab(0.25, 0.5, 0.5)
tab(0.25, 0.5, 0.7)
tab(0.25, 0.25, 0.3)
tab(0.25, 0.25, 0.5)
tab(0.25, 0.25, 0.7)


# Plot
plot(f, muxeff(eff1,eff2,corr))
xlabel("Frequency [MHz]")
ylabel("Multiplexing Efficiency [dB]")
grid(True, 'both', 'both')
# show()
