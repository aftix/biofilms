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

def Fix(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if j == 0:
        grid[-1].force = True
        grid[-1].forceFunc = forces.ConstRightForce
        grid[-1].fixed = True
    elif j == nrows - 1:
        grid[-1].fixed = True

params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008, majhook=Fix)

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
