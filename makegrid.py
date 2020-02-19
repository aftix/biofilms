#!/usr/bin/env python3

import sys
import inout
import generation
from datastructure import BeginParams, Cell
import jsonpickle
import numpy
from typing import List

if len(sys.argv) < 2:
    name: str = 'grid.dat'
else:
    name = sys.argv[1]

def PullOut(c: Cell) -> None:
    if c.pos[0] < 0.5:
        c.pos[0] = -0.05
    else:
        c.pos[0] = 1.05

def PullEdge(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if i == nrows / 2:
        if j == 0 or j == nrows - 1:
            grid[-1].update = True
            grid[-1].updateFunc = PullOut

params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008, majhook=PullEdge)

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
