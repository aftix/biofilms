#!/usr/bin/env python3

# main.py

import generation
import graph
import inout
import simulate
import sys
import os
import jsonpickle
from typing import Dict, List, Tuple
from datastructure import Params, Cell
import shutil
import numpy
import scipy.integrate

if len(sys.argv) < 2:
    loc: str = 'grid.dat'
else:
    loc = sys.argv[1]

if len(sys.argv) < 3:
    folder: str = 'output/'
else:
    folder = sys.argv[2]
    if folder[-1] != '/':
        folder += '/'

with open(loc, 'r') as fi:
    params: Params = jsonpickle.loads(fi.readline())
    mygrid = inout.deserialize_cellmatrix(fi)

try:
    shutil.rmtree(folder)
finally:
    os.mkdir(folder)

mygrid[0].pos = numpy.array([0, 0])

initialpos = numpy.array([])
for cell in mygrid:
    initialpos = numpy.append(initialpos, cell.pos)

solutions: List[List[Cell]] = list([mygrid])
solution = scipy.integrate.solve_ivp(
    simulate.StepForce,
    (0, params['del_t']),
    initialpos,
    args=(mygrid, params, solutions)
)

for ind in range(len(solutions)):
    with open(folder + f'{ind:05d}', 'w') as f:
        inout.serialize_cellmatrix(solutions[ind], f)
