#!/usr/bin/env python3

import sys
import inout
import generation
from datastructure import BeginParams
import jsonpickle
import numpy

if len(sys.argv) < 2:
    name: str = 'grid.dat'
else:
    name = sys.argv[1]

def fixedges(i, j, nrows, grid):
#    if i == nrows - 1 or j == nrows - 1:
#        grid[-1].fixed = True
    if i == 0 and j == 0:
        grid[-1].fixed = True

params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008, majhook=fixedges)
mygrid[0].pos = numpy.array([-0.08, -0.08])

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
