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
        grid[-1].forceFunc = forces.StopGoConst
    elif j == nrows - 1:
        grid[-1].fixed = True
        grid[-1].force = True
        grid[-1].forceFunc = forces.LinRestraint
    else:
        grid[-1].force = True
        grid[-1].forceFunc = forces.LinRestraint

def SideWobble(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if j == 0:
        grid[-1].force = True
        grid[-1].forceFunc = forces.SineConstrained
    else:
        grid[-1].force = True
        grid[-1].forceFunc = forces.LinRestraint
        if j == nrows - 1:
            grid[-1].fixed = True

def DoubleSideWobble(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    if j == 0:
        grid[-1].force = True
        grid[-1].forceFunc = forces.SineConstrained
    elif j == nrows - 1:
        grid[-1].force = True
        grid[-1].forceFunc = forces.NegSineConstrained
    else:
        grid[-1].force = True
        grid[-1].forceFunc = forces.LinRestraint

def Constrain(i: int, j: int, nrows: int, grid: List[Cell]) -> None:
    grid[-1].force = True
    grid[-1].forceFunc = forces.LinRestraint


params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008, majhook=DoubleSideWobble, minhook=Constrain)

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
