# generation.py

from datastructure import MakeCell
from math import sqrt

"""
Generate a matrix of cells in a hexagonal pattern on a 1x1 square
nrows is the number of full spaced rows (~1/2 of full row count)
size is the radius of the cells
The matrix is a list of tuples that are (centerx, centery, radius)
"""
def generate_offsetgrid(nrows, size=0.05):
    # needed_space is space needed for main and side rows
    # it is diameter * (number of major rows) * (number of minor rows)
    needed_space = 2 * size * (2 * nrows - 1)
    if needed_space >= 1:
        raise OverflowError

    # taken_space is the space taken up in a major row
    taken_space = 2 * size * nrows

    # gap_space is the space between cells on a major row
    # From needed_space, this is at least 2*size to accomadate the minor rows
    gap_space = (1 - taken_space) / (nrows - 1)

    grid = list()

    # Generate the major rows
    xpos, ypos = size, size
    for i in range(nrows):
        for j in range(nrows):
            grid.append(MakeCell(xpos, ypos, size))
            xpos += gap_space + 2*size
        xpos = size
        ypos += gap_space + 2*size

    # Generate the minor rows
    xpos, ypos = 2 * size + gap_space / 2, 2 * size + gap_space / 2
    for i in range(nrows - 1):
        for j in range(nrows - 1):
            grid.append(MakeCell(xpos, ypos, size))
            xpos += gap_space + 2*size
        xpos = 2 * size + gap_space / 2
        ypos += gap_space + 2 * size

    for cell in grid:
        cell.close = list()
        cell.far = list()
        big_space = gap_space + 2*size
        small_space = (size + gap_space / 2) * sqrt(2)

        for ind, other in enumerate(grid):
            mydist = sqrt((other.x - cell.x)**2 + (other.y - cell.y)**2)
            if abs(big_space - mydist) < 0.0005:
                cell.far.append(ind)
            elif abs(small_space - mydist) < 0.0005:
                cell.close.append(ind)

    return grid


