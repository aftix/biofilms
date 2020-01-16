# gfx/plotgrid.py

import matplotlib.pyplot as plt

def plot_cells(cells, name='plot.png'):
    fig, ax = plt.subplots()

    for (x, y, rad) in cells:
        ax.add_artist(plt.Circle((x, y), rad, color='k'))

    fig.savefig(name)
