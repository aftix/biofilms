#!/usr/bin/env python3
# prettify.py

import sys
import graph
import inout
import os

if len(sys.argv) < 2:
    direc: str = 'output/'
else:
    direc = sys.argv[1]
    if direc[-1] != '/':
        direc += '/'

with open(direc + 'globals') as glb:
    maxstress: float = float(glb.readline())

for name in os.listdir(direc):
    fname: str = direc + os.fsdecode(name)
    if fname.endswith(".dat"):
        with open(fname, "r") as inp:
            grid = inout.deserialize_cellmatrix(inp)
            graph.plot_cells(grid, name=fname[:-3] + 'png', maxstress=maxstress)


