import scipy.interpolate as interpolate
import matplotlib
import matplotlib.image as image
from matplotlib import rc, rcParams
import numpy as np

# Global formatting options

nearly_black = '#161616'
light_grey = '#EEEEEE'
lighter_grey = '#F5F5F5'
white = '#FFFFFF'
light_blue = '#6d9fd1'

fontsize = 16

tableau10 = [ '#4379a7', '#f28e2b', '#e15759', 
              '#76b7b2', '#59a14f', '#edc948',
              '#b07aa1', '#ff9da7', '#9c755f', '#bab0ac' ]

master_formatting = { 'axes.formatter.limits': (-3,3),
                      'xtick.major.pad': 7,
                      'ytick.major.pad': 7,
                      'ytick.color': nearly_black,
                      'xtick.color': nearly_black,
                      'ytick.direction': 'in',
                      'ytick.right': True,
                      'ytick.major.size': 8,
                      'axes.labelcolor': nearly_black,
                      'legend.facecolor': light_grey,
                      'pdf.fonttype': 42,
                      'ps.fonttype': 42,
                      'mathtext.fontset': 'custom',
                      'font.size': fontsize,
                      'font.family': ['serif'],
                      'font.serif': ['Minion Pro'],
                      'mathtext.fontset': 'custom',
                      'mathtext.rm': 'Minion Pro',
                      'mathtext.it': 'Minion Pro:italic',
                      'mathtext.bf': 'Minion Pro:bold',
                      #'text.usetex': True,
                      'savefig.bbox':'tight',
                      'axes.facecolor': white,
                      'axes.labelpad': 13.0,
                      'axes.labelsize': fontsize,
                      'axes.titlesize': fontsize,
                      'axes.titlepad': 25,
                      'axes.spines.right': True,
                      'lines.markersize': 10.0,
                      'lines.markeredgewidth': 1.0,
                      'lines.linewidth': 1.5,
                      'lines.scale_dashes': False,
                      'text.latex.preamble': [ r"\usepackage{amssymb}",
                                               r"\usepackage{amsmath}" ] }

def set_rcParams( formatting ):
    for k, v in formatting.items():
        rcParams[k] = v
