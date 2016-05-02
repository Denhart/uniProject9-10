import numpy as np
import matplotlib.pyplot as plt

# Set up a figure of the correct dimensions and the correct font for the
# report.
#
# @param args Positional arguments for matplotlib.pyplot.figure()
# @param kwargs All arguments are passed onto the matplotlib.pyplot.figure()
#        function.
def figure(*args, **kwargs):
    if kwargs.get("figsize") == None:
        kwargs["figsize"] = (3.5, 3)

    plt.rcParams['font.family'] = "Times New Roman"
    plt.rcParams['font.size'] = "8"
    plt.figure(*args, **kwargs)

# Scale to get frequency axis to MHz
#
# @param f Frequency axis.
def freqscale(f):
    m = f.max()
    if m > 100e6: 
        return 1e-6 # Hz
    elif m > 100e3:
        return 1e-3 # kHz
    elif m > 100:
        return 1e0 # MHz
    else:
        return 1e3 # GHz

# Convert/preserve data in dB
#
# @param x Data to convert (e.g. efficiency).
# @return Data in dB.
def to_db(x):
    if x.min() < 0:
        return x
    else:
        return 10*np.log10(x)

# Plot an S-parameter.
#
# @param f Frequency axis for the plot.
# @param s S-parameter (abs-value in dB) to plot.
# @param c Color/linetype string (e.g. '--b' for dashed blue).
# @param label Label for the legend
def sparam(f, s, c="-", label=""):
    f *= freqscale(f)
    plt.plot(f, s, c, label=label)


# Finish the S-parameter plot with legend, etc.
#
# @param kwargs Parameters passed onto matplotlib.pyplot.legend().
def end_sparam(**kwargs):
    if kwargs.get("loc") == None:
        kwargs["loc"] = 1
    if kwargs.get("fontsize") == None:
        kwargs["fontsize"] = 8
    if kwargs.get("handlelength") == None:
        kwargs["handlelength"] = 3

    plt.ylim(-24, 0)
    plt.yticks([-24, -18, -12, -6, 0])

    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Magnitude [dB]")

    for x in [700, 960, 1710, 2650]:
        plt.axvline(x, color='k', linestyle='--')
        plt.text(x, 0.7, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))

    plt.grid(True)
    plt.legend(**kwargs)
    plt.tight_layout(rect=(0,0,1,0.97))

# Plot an efficiency graph.
#
# @param f Frequency axis.
# @param e Efficiency (. or dB).
# @param c Color/linetype string (e.g. '--b' for dashed blue).
# @param label Label for the graph's legend.
def efficiency(f, e, c="-", label=""):
    f *= freqscale(f)
    e = to_db(e)

    fstep = min(min(np.diff(f)), 0.5) # Maximum step size is 0.5 MHz
    fmin = min(f)
    fmax = max(f)
    f_LB = np.arange(700, 960, fstep)
    f_HB = np.arange(1710, 2650, fstep)

    lb_h = plt.plot(f_LB, np.interp(f_LB, f, e), c, label=label)
    if fmax >= 1710:
        hb_h = plt.plot(f_HB, np.interp(f_HB, f, e), color=lb_h[0].get_color(), linestyle=lb_h[0].get_linestyle())

# Finish the efficiency plot with legend, etc.
#
# @param kwargs Arguments passed on to matplotlib.pyplot.legend()
def end_efficiency(**kwargs):
    if kwargs.get("loc") == None:
        kwargs["loc"] = 1
    if kwargs.get("fontsize") == None:
        kwargs["fontsize"] = 8
    if kwargs.get("handlelength") == None:
        kwargs["handlelength"] = 3

    plt.legend(**kwargs)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Efficiency [dB]")
    plt.ylim(-15, 0)
    plt.yticks([-15,-12, -9, -6, -3, 0])

    plt.grid(True)
    
    for x in [700, 960, 1710, 2650]:
        plt.axvline(x, color='k', linestyle='--')
        plt.text(x, 0.3, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))

    ax1 = plt.gca()

    ax2 = ax1.twinx()
    ax2.set_ylim(-15,0)
    ax2.set_yticks([-15,-12,-9,-6,-3,0])
    ax2.set_yticklabels([int(x) for x in np.around(100*10**(ax2.get_yticks()/10))])
    ax2.set_ylabel("Efficiency [%]", rotation=270, va="bottom")

    plt.tight_layout(rect=(0,0,1,0.97))

# Plot correlation
#
# @param f Frequency axis.
# @param ecc Envelope correlation coefficient.
# @param c Color/linetype string (e.g. '--b' for dashed blue).
# @param label Label for the graph's legend.
def correlation(f, ecc, c="-", label=""):
    f *= freqscale(f)

    fstep = min(min(np.diff(f)), 0.5) # Maximum step size is 0.5 MHz
    fmin = min(f)
    fmax = max(f)
    f_LB = np.arange(700, 960, fstep)
    f_HB = np.arange(1710, 2650, fstep)

    lb_h = plt.plot(f_LB, np.interp(f_LB, f, ecc), c, label=label)
    if fmax >= 1710:
        hb_h = plt.plot(f_HB, np.interp(f_HB, f, ecc), color=lb_h[0].get_color(), linestyle=lb_h[0].get_linestyle())

# Finish the correlation plot with legend, etc.
#
# @param loc Location of the legend (like matplotlib.pyplot.legend())
# @param fontsize Font size for the legend.
def end_correlation(loc=1, fontsize=8):
    plt.legend(loc=loc, fontsize=fontsize, handlelength=3)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Correlation [.]")
    plt.ylim(0, 1)
    plt.yticks([0,0.25,0.50,0.75,1.0])

    plt.grid(True)
    
    for x in [700, 960, 1710, 2650]:
        plt.axvline(x, color='k', linestyle='--')
        plt.text(x, 1.02, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))

    plt.tight_layout(rect=(0,0,1,0.97))

# Plot a SAR graph.
#
# @param f Frequency axis.
# @param e Efficiency (. or dB).
# @param c Color/linetype string (e.g. '--b' for dashed blue).
# @param label Label for the graph's legend.
def sar(f, sar, c="-", label=""):
    f *= freqscale(f)

    fstep = min(min(np.diff(f)), 0.5) # Maximum step size is 0.5 MHz
    fmin = min(f)
    fmax = max(f)
    f_LB = np.arange(700, 960, fstep)
    f_HB = np.arange(1710, 2650, fstep)

    lb_h = plt.plot(f_LB, np.interp(f_LB, f, sar), c, label=label)
    if fmax >= 1710:
        hb_h = plt.plot(f_HB, np.interp(f_HB, f, sar), color=lb_h[0].get_color(), linestyle=lb_h[0].get_linestyle())

# Finish the SAR plot with legend, etc.
#
# @param kwargs Arguments passed on to matplotlib.pyplot.legend()
def end_sar(**kwargs):
    if kwargs.get("loc") == None:
        kwargs["loc"] = 1
    if kwargs.get("fontsize") == None:
        kwargs["fontsize"] = 8
    if kwargs.get("handlelength") == None:
        kwargs["handlelength"] = 3

    plt.legend(**kwargs)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("SAR [W/kg]")
    plt.ylim(0, 4)
    plt.yticks([0,1,2,3,4])

    plt.grid(True)
    
    for x in [700, 960, 1710, 2650]:
        plt.axvline(x, color='k', linestyle='--')
        plt.text(x, 4.1, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))

    plt.tight_layout(rect=(0,0,1,0.97))
