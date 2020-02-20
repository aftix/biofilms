# graph.py

import matplotlib.pyplot as plt
import matplotlib.colors as col
import itertools
from typing import List
from datastructure import Cell
from math import isclose
import numpy

def plot_cells(cells: List[Cell], name: str='plot.png', maxstress: float=1) -> None:
    fig, ax = plt.subplots()

    for cell in cells:
        for n in itertools.chain(cell.close, cell.far):
            radial = cell.pos - cells[n].pos
            radial = radial / numpy.linalg.norm(radial)
            xs: List[float] = [cell.pos[0] + cell.rad * radial[0], cells[n].pos[0] - cells[n].rad * radial[0]]
            ys: List[float] = [cell.pos[1] + cell.rad * radial[1], cells[n].pos[1] - cells[n].rad * radial[1]]
            #ax.plot(xs, ys, 'k', linewidth=1)
        circ = plt.Circle((cell.pos[0], cell.pos[1]), cell.rad)
        if not cell.fixed:
            circ.set_edgecolor('k')
        else:
            circ.set_edgecolor('g')
        if isclose(cell.stress, 0):
            circ.set_facecolor('white')
        elif cell.stress > 0:
            circ.set_facecolor(col.hsv_to_rgb([0, cell.stress/maxstress, 1]))
        else:
            circ.set_facecolor(col.hsv_to_rgb([0.677778, -cell.stress/maxstress, 1]))
        ax.add_artist(circ)

    ax.set_xlim([-0.1, 1.1])
    ax.set_ylim([-0.1, 1.1])
    fig.savefig(name)
    plt.close(fig)

def plot_avgstress(avgs: List[float], times: List[float], name: str='avgstress.png') -> None:
    fig, ax = plt.subplots()
    ax.plot(times, avgs, color='k', marker='.', label='Average Stress', linestyle='None')
    ax.set_xlabel('Time')
    ax.set_ylabel('Average Stress')
    fig.savefig(name)
    plt.close(fig)
