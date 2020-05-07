import matplotlib
matplotlib.use('module://matplotlib_terminal.backend')

import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.style.use({
    'figure.figsize': (12, 4),
    'lines.linewidth': 2,
    'axes.edgecolor': 'white',
    'xtick.major.size': 6,
    'xtick.major.width': 3,
    'xtick.direction': 'out',
    'ytick.major.size': 6,
    'ytick.major.width': 3,
    'ytick.direction': 'out',

    'font.family': 'monospace',
    'font.monospace': 'Ubuntu Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Computer Modern Typewriter, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace',

    # 'terminal.unicode_latex': True,
})
