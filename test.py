import numpy as np
import matplotlib_terminal
import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot([0, 1], [0, 1])
plt.plot([1, 0], [0, 1], lw=3)
plt.scatter([0], [.5])

plt.show('gamma')
plt.show('block')
plt.show('braille')
plt.close()


ax = plt.gca()

plt.text(0.4, 0.1, "bar555", size=5,)
plt.text(0.5, 0.1, "bar6", size=6,)
plt.text(0.6, 0.2, "bar8", size=8,)
plt.text(0.7, 0.3, "bar10", size=10,)
plt.text(0.8, 0.5, "bar14", size=14,)
plt.text(0.8, 0.8, "bar16", size=16,)
plt.text(0.9, 0.8, "bar18", size=18,)
plt.text(0.8, 0.6, "bar20", size=20,)
plt.text(0.4, 0.2, "bar30", size=30,)
plt.text(0.3, 0.6, "bar50", size=50,)

plt.text(-0.5, 0.4, "$\sum_{k=0}^n k+1$", size=30,)
plt.text(-0.8, 0.3, "$\sum_{k=0}^n x_k+1$", size=12,)

plt.plot([0, 1], [0, 1], c='g', label='alamakota', lw=4)
x = np.linspace(0, 1, 400)
plt.plot(x, np.sin(1/x), c='r', label='sin 1/x', lw=4)


# im = plt.imshow(template, extent=[0, 1, 0, 1])
# plt.colorbar(im)


delta = 0.025
x = np.arange(-1.0, 1.0, delta)
y = np.arange(-1.0, 1.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')

plt.legend()
plt.title('Some random plotting')
plt.suptitle('Testing')

plt.show('gamma')
plt.show('block')
plt.show('braille')
plt.close()


category_names = ['Strongly disagree', 'Disagree',
                  'Neither agree nor disagree', 'Agree', 'Strongly agree']
results = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}

plt.style.use('dark_background')
def survey(results, category_names, fig, ax):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left')

    return fig, ax

fig = plt.figure()
ax = plt.gca()
survey(results, category_names, fig, ax)

plt.show()
plt.show('block')
plt.show('braille')
plt.savefig('xxx.png')
plt.savefig('xxx.txt')

plt.close()
plt.text(0, 0, r'$\sum_{i=0}^t (\frac{\sum_{k=0}^p c_{i,p}\cdot s_p}{|c_i|}nc_i + \frac{\sum_{k=0}^p (1-c_{i,p})\cdot s_p}{|1-c_i|}n(1-c_i)- s)^2$', fontsize=50)
plt.axis('off')
plt.show()
