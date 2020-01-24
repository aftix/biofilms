# graph.py

import matplotlib.pyplot as plt
import itertools
from typing import List
from datastructure import Cell

def plot_cells(cells: List[Cell], name: str='plot.png') -> None:
    fig, ax = plt.subplots()

    for cell in cells:
        ax.add_artist(plt.Circle((cell.x, cell.y), cell.rad, color='k'))
        for n in itertools.chain(cell.close, cell.far):
            ax.plot([cell.x, cells[n].x], [cell.y, cells[n].y], 'k', linewidth=1)

    fig.savefig(name)
