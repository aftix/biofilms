#!/usr/bin/env python3

import sys
import inout
import generation
from datastructure import BeginParams
import jsonpickle

if len(sys.argv) < 2:
    name: str = 'grid.dat'
else:
    name = sys.argv[1]

params = BeginParams()
mygrid = generation.generate_offsetgrid(params, nrows=10, size=0.008)

with open(name, "w") as f:
    global sim_params
    f.write(jsonpickle.dumps(params))
    f.write('\n')
    inout.serialize_cellmatrix(mygrid, f)
