# graph.py

import matplotlib.pyplot as plt
import itertools
from typing import List
from datastructure import Cell

def plot_cells(cells: List[Cell], name: str='plot.png') -> None:
    fig, ax = plt.subplots()

    for cell in cells:
        ax.add_artist(plt.Circle((cell.pos[0], cell.pos[1]), cell.rad, color='k'))
        for n in itertools.chain(cell.close, cell.far):
            ax.plot([cell.pos[1], cells[n].pos[0]], [cell.pos[1], cells[n].pos[1]], 'k', linewidth=1)

    fig.savefig(name)
