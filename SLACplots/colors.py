import numpy as np
import matplotlib
from matplotlib.colors import ListedColormap

SLACred = '#8C1515'
SLACgrey = '#53565A'
SLACblue = '#007C92'
SLACteal = '#279989'
SLACgreen = '#8BC751'
SLACyellow = '#FEDD5C'
SLACorange = '#E04F39'
SLACpurple = '#53284F'
SLAClavender = '#765E99'
SLACbrown = '#5F574F'

SLACcolors = [SLACred,
              SLACblue,
              SLACteal,
              SLACgreen,
              SLACyellow,
              SLACgrey,
              SLACorange,
              SLACpurple,
              SLAClavender,
              SLACbrown,
]

# SLACsage = [199./256, 209./256, 197./256]
white = [256./256, 256./256, 256./256]
SLACpaloverde = [39./256, 153./256, 137./256]
SLACredRGB = [140./256, 21./256, 21./256]

matplotlib.cm.register_cmap('SLACverde',
                            ListedColormap(np.array([np.interp(np.linspace(0, 1, 256),
                                                               [0, 1],
                                                               [whiteV, pvV])
                                                     for whiteV, pvV in zip(white, SLACpaloverde)]).T,
                                           name = 'SLACverde'))

matplotlib.cm.register_cmap('SLACred',
                            ListedColormap(np.array([np.interp(np.linspace(0, 1, 256),
                                                               [0, 1],
                                                               [whiteV, srV])
                                                     for whiteV, srV in zip(white, SLACredRGB)]).T,
                                           name = 'SLACred'))

LaTeXflavor = {"numu": r'$\nu_\mu$',
               "numubar": r'$\bar{\nu}_\mu$',
               "nue": r'$\nu_e$',
               "nuebar": r'$\bar{\nu}_e$',
               "nutau": r'$\nu_\tau$',
               "nutaubar": r'$\bar{\nu}_\tau$'}

matplotlib.rc('axes', **{"prop_cycle": matplotlib.cycler(color = SLACcolors)})
matplotlib.rc('image', **{"cmap": 'SLACverde'})
# matplotlib.rc('font', **{"family": 'sans-serif',
#                          "sans-serif": 'Arial',
#                          "size": 16,
#                          "weight": 'bold'})
# matplotlib.rc('font', **{"family": 'sans-serif',
#                          "sans-serif": 'Arial',
#                          "size": 16,
#                          "weight": 'bold'})
# matplotlib.rc('text', **{"usetex": True})
