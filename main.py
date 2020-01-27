#!/usr/bin/env python3

# main.py

import generation
import graph
import inout
import simulate
import sys
import jsonpickle
from typing import Dict
from datastructure import Params

if len(sys.argv) < 2:
    loc: str = 'grid.dat'
else:
    loc = sys.argv[1]

with open(loc, 'r') as fi:
    params: Params = jsonpickle.loads(fi.readline())
    mygrid = inout.deserialize_cellmatrix(fi)

forces = simulate.FindForces(params, mygrid)
simulate.UpdateCellForces(params, mygrid, forces)
