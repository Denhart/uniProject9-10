#!/usr/bin/python3
"""
Plot Efficiency from file(s) created by CST STUDIO.
"""
import argparse
from os.path import splitext
from numpy import *
from matplotlib.pyplot import *
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = "8"

#   Arguments
parser = argparse.ArgumentParser()
parser.add_argument('files', help="Efficiency file(s) exported from CST.", nargs="+")
parser.add_argument('-o', '--outfile', help="Output file name. Standard: INFILE.pdf")
parser.add_argument('-s', '--show', action="store_true", help="Show resulting figure instead of saving it.")
parser.add_argument('-x', '--xlabel', help="Alternative x-label. Default: Frequencey [MHz].")
parser.add_argument('-y', '--ylabel', help="Alternative y-label. Default: Efficiency [dB].")
parser.add_argument('-l', '--lineskip', help="Number of rows to skip in the input file(s). Default: 2.")
parser.add_argument('-d', '--delimiter', help="CSV file delimiter. Default: any whitespace.")
parser.add_argument('-n', '--nolegend', action="store_true", help="If this is set, no legend is printed.")
args = parser.parse_args()

if (not args.outfile):
    tmpRoot, tmpExt = splitext(args.files[0])
    args.outfile = tmpRoot + ".pdf"

#   Read first file
if (not args.delimiter):
    args.delimiter = None

if (args.lineskip):
    m = loadtxt(args.files[0], skiprows=int(args.lineskip), delimiter=args.delimiter, usecols=(0,1))
    f = m[:,0].T
    y = m[:,1].T
else:
    m = loadtxt(args.files[0], skiprows=2, delimiter=args.delimiter, usecols=(0,1))
    f = m[:,0].T
    y = m[:,1].T

#   Read the rest of the files
idx = 1
for thisfile in args.files[1:]:
    if (args.lineskip):
        m = loadtxt(thisfile, skiprows=int(args.lineskip), delimiter=args.delimiter, usecols=(0,1))
        f = vstack((f, m[:,0].T))
        y = vstack((y, m[:,1].T))
    else:
        m = loadtxt(thisfile, skiprows=2, delimiter=args.delimiter, usecols=(0,1))
        f = vstack((f, m[:,0].T))
        y = vstack((y, m[:,1].T))
    idx = idx + 1

def freqscale(f):
    if f.max() > 100:
        return 1.0
    else:
        return 1000.0

def to_db(x):
    if x.min() < 0:
        return x
    else:
        return 10*log10(x)

if 1:
    figure(figsize=(3.5, 3))
    f *= freqscale(f)
    y = to_db(y)

    ax1 = subplot(111)
    ax1.plot(f.T,y.T)
    ax1.set_xlabel("Frequency [MHz]")
    ax1.set_ylabel("Efficiency [dB]")
    ax1.set_xlim(f.min(), f.max())
    for x in [700, 960, 1710, 2650]:
        ax1.axvline(x, color='k', linestyle='--')
        ax1.text(x, 1.02, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))
    ax1.set_ylim(-9, 0)
    ax1.set_yticks([-9, -6, -3, 0])
    if (args.xlabel):
        ax1.set_xlabel(args.xlabel)
    if (args.ylabel):
        ax1.set_ylabel(args.ylabel)
    grid(True)

    ax2 = gca().twinx()
    ax2.set_ylim(-9,0)
    ax2.set_yticks([-9,-6,-3,0])
    ax2.set_yticklabels(around(10**(ax2.get_yticks()/10),2))
    ax2.set_ylabel("Efficiency [.]")

    if len(args.files) > 1:
        if not args.nolegend:
            legend(args.files, loc=9, bbox_to_anchor=(0.5, -0.2), ncol=2, fancybox=False, prop={'size': 8}, handlelength=3)

    tight_layout()
    if args.show:
        show()
    else:
        savefig(args.outfile, bbox_inches = "tight", additional_artists="art")
    close()
