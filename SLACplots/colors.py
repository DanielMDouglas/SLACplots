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
              SLACgrey,
              SLACblue,
              SLACteal,
              SLACgreen,
              SLACyellow,
              SLACorange,
              SLACpurple,
              SLAClavender,
              SLACbrown,
]

LaTeXflavor = {"numu": r'$\nu_\mu$',
               "numubar": r'$\bar{\nu}_\mu$',
               "nue": r'$\nu_e$',
               "nuebar": r'$\bar{\nu}_e$',
               "nutau": r'$\nu_\tau$',
               "nutaubar": r'$\bar{\nu}_\tau$'}

matplotlib.rc('axes', prop_cycle = matplotlib.cycler(color = SLACcolors))
matplotlib.rc('font', family = 'Ariel', size = 16, weight = 'bold')
matplotlib.rc('text', usetex = True)
