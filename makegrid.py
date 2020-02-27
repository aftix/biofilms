#!/usr/bin/env python3

import sys
import inout
import generation
from datastructure import BeginParams, Cell
import jsonpickle
import numpy
from typing import List
import forces

if len(sys.argv) < 2:
    name: str = 'grid.dat'
else:
    name = sys.argv[1]

def SqueezeFunc(c: Cell) -> None:
    pass
    if c.pos[0] < 0.5:
        c.pos[0] = 0.5 - c.rad - 0.001
    else:
        c.pos[0] = 0.5 + c.rad + 0.001

def Squeeze(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if j == (nrows / 2) - 1 or j == nrows / 2:
        grid[-1].update = True
        grid[-1].updateFunc = SqueezeFunc

def Pull(c: Cell) -> None:
    c.pos = numpy.array([-0.08, -0.08])

def Fix(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if j == 0 and i == 0:
        grid[-1].force = True
        grid[-1].forceFunc = forces.LowerLeftSine
    elif j == nrows - 1 or i == nrows - 1:
        grid[-1].fixed = True


params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008, majhook=Fix)

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
