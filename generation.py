# generation.py

from datastructure import MakeCell, Cell, Params
from math import isclose
from typing import List, Tuple
import numpy

"""
Generate a matrix of cells in a hexagonal pattern on a 1x1 square
nrows is the number of full spaced rows (~1/2 of full row count)
size is the radius of the cells
The matrix is a list of tuples that are (centerx, centery, radius)
"""
def generate_offsetgrid(param: Params, nrows: int, size: float=0.05, majhook=None, minhook=None) \
        -> List[Cell]:
    # needed_space is space needed for main and side rows
    # it is diameter * (number of major rows) * (number of minor rows)
    needed_space: float = 2 * size * (2 * nrows - 1)
    if needed_space >= 1:
        raise OverflowError

    # taken_space is the space taken up in a major row
    taken_space: float = 2 * size * nrows

    # gap_space is the space between cells on a major row
    # From needed_space, this is at least 2*size to accomadate the minor rows
    gap_space: float = (1 - taken_space) / (nrows - 1)

    grid: List[Cell] = list()

    # Generate the major rows
    xpos: float = size
    ypos: float = size
    iter_space: float = gap_space + 2*size # space between centers
    for i in range(nrows):
        for j in range(nrows):
            grid.append(MakeCell(xpos, ypos, size))
            if majhook is not None:
                majhook(i, j, nrows, grid)
            xpos += iter_space
        xpos = size
        ypos += iter_space

    # Generate the minor rows
    xpos, ypos = 2 * size + gap_space / 2, 2 * size + gap_space / 2
    for i in range(nrows - 1):
        for j in range(nrows - 1):
            grid.append(MakeCell(xpos, ypos, size))
            if minhook is not None:
                minhook(i, j, nrows, grid)
            xpos += iter_space
        xpos = 2 * size + gap_space / 2
        ypos += iter_space

    big_space: float = iter_space
    small_space: float = (iter_space / 2) *  1.4142135623731 #sqrt2

    param['spring_relax_close'] = small_space
    param['spring_relax_far'] = big_space

    for cell in grid:
        cell.close = list()
        cell.far = list()

        for ind, other in enumerate(grid):
            mydist: float = numpy.linalg.norm(cell.pos - other.pos)
            if isclose(big_space, mydist):
                cell.far.append(ind)
            elif isclose(small_space, mydist):
                cell.close.append(ind)

    return grid


