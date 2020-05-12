import matplotlib
matplotlib.use('module://matplotlib_terminal.backend')

import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.style.use({
    'figure.figsize': (11, 8),
    'figure.autolayout': True,
    'lines.linewidth': 2,
    'axes.edgecolor': 'white',
    'xtick.major.size': 6,
    'xtick.major.width': 3,
    'xtick.direction': 'out',
    'ytick.major.size': 6,
    'ytick.major.width': 3,
    'ytick.direction': 'out',

    'font.family': 'monospace',
    'font.size': 12,
    'font.monospace': 'Ubuntu Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Computer Modern Typewriter, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace',


    'legend.fancybox': False,
    'legend.edgecolor': 'white',
    'legend.fontsize': 'medium',

    # 'terminal.unicode_latex': True,
})
