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
from scipy.constants import pi
from math import isclose

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
except FileNotFoundError:
    pass
finally:
    os.mkdir(folder)

initialpos = numpy.array([])
for cell in mygrid:
    initialpos = numpy.append(initialpos, cell.pos)


solution = scipy.integrate.solve_ivp(
    simulate.StepForce,
    (0, params['del_t']),
    initialpos,
    args=(mygrid, params)
)

maxstress: float = 0

avgstress: List[float] = list()
avgxoffset: List[float] = list()
avgyoffset: List[float] = list()
avgdisplacement: List[float] = list()

for ind in range(len(solution.t)):
    newgrid = mygrid
    for i in range(len(mygrid)):
        newgrid[i].pos = solution.y[2*i:2*i+2,ind]
    compression, tension, avg = simulate.GetStress(newgrid, solution.t[ind], params)
    dist, xoff, yoff, avgstrain = simulate.GetStrain(newgrid, params)
    avgstress.append(avg)
    avgxoffset.append(avgstrain[0])
    avgyoffset.append(avgstrain[1])
    avgdisplacement.append(dist)
    if compression > maxstress:
        maxstress = compression
    if -tension > maxstress:
        maxstress = -tension
    with open(folder + f'{ind:05d}.dat', 'w') as out:
        inout.serialize_cellmatrix(newgrid, out)

if isclose(maxstress, 0):
    maxstress = 1

with open(folder + 'globals', 'w') as out:
    out.write(str(maxstress))
    out.write('\n')

graph.plot_avgstress(avgstress, solution.t, name=folder + 'avgstress.png')
graph.plot_avgstrain(avgxoffset, avgyoffset, avgdisplacement, solution.t, name=folder)
