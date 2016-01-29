#!/usr/bin/python3
"""
Plot Correlation from file(s) created by CST STUDIO.
"""
import argparse
from os.path import splitext
from numpy import *
from matplotlib.pyplot import *
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = "8"

#   Arguments
parser = argparse.ArgumentParser()
parser.add_argument('corrfiles', help="Correlation file(s) exported from CST.", nargs="+")
parser.add_argument('-o', '--outfile', help="Output file name. Standard: INFILE.pdf")
parser.add_argument('-s', '--show', action="store_true", help="Show resulting figure instead of saving it.")
parser.add_argument('-x', '--xlabel', help="Alternative x-label. Default: Frequencey [MHz].")
parser.add_argument('-y', '--ylabel', help="Alternative y-label. Default: Correlation [.].")
parser.add_argument('-l', '--lineskip', help="Number of rows to skip in the input file(s). Default: 2.")
parser.add_argument('-d', '--delimiter', help="CSV file delimiter. Default: any whitespace.")
parser.add_argument('-n', '--nolegend', action="store_true", help="If this is set, no legend is printed.")
args = parser.parse_args()

if (not args.outfile):
    tmpRoot, tmpExt = splitext(args.corrfiles[0])
    args.outfile = tmpRoot + ".pdf"

#   Read first file
if (not args.delimiter):
    args.delimiter = None

if (args.lineskip):
    m = loadtxt(args.corrfiles[0], skiprows=int(args.lineskip), delimiter=args.delimiter, usecols=(0,1))
    f = m[:,0].T
    y = m[:,1].T
else:
    m = loadtxt(args.corrfiles[0], skiprows=2, delimiter=args.delimiter, usecols=(0,1))
    f = m[:,0].T
    y = m[:,1].T

#   Read the rest of the files
idx = 1
for thisfile in args.corrfiles[1:]:
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

if 1:
    figure(figsize=(3.5, 3))
    f *= freqscale(f)
    plot(f.T,y.T)
    xlabel("Frequency [MHz]")
    ylabel("Correlation [.]")
    xlim(f.min(), f.max())
    for x in [700, 960, 1710, 2650]:
        axvline(x, color='k', linestyle='--')
        text(x, 1.02, x, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=0))
    ylim(0, 1)
    yticks([0,0.25,0.5,0.75,1.0])
    if (args.xlabel):
        xlabel(args.xlabel)
    if (args.ylabel):
        ylabel(args.ylabel)
    grid(True)
    if len(args.corrfiles) > 1:
        if not args.nolegend:
            legend(args.corrfiles, loc=9, bbox_to_anchor=(0.5, -0.2), ncol=2, fancybox=False, prop={'size': 8}, handlelength=3)

    tight_layout()
    if args.show:
        show()
    else:
        savefig(args.outfile, bbox_inches = "tight", additional_artists="art")
    close()
