# gfx/plotgrid.py

import matplotlib.pyplot as plt

def plot_cells(cells, name='plot.png'):
    fig, ax = plt.subplots()

    for cell in cells:
        ax.add_artist(plt.Circle((cell.x, cell.y), cell.rad, color='k'))
        for n in cell.neighbors:
            ax.plot([cell.x, cells[n].x], [cell.y, cells[n].y], 'k', linewidth=1)

    fig.savefig(name)
