#!/usr/bin/env python3

# test.py

import generation
import graph
import inout
import os
from datastructure import sim_params

mygrid = generation.generate_offsetgrid(nrows=10, size=0.008)

print(sim_params)
inout.save(mygrid, 'test.dat')
sim_params['spring_k'] = 15
print(sim_params)
newgrid = inout.load('test.dat')
print(sim_params)

assert(len(newgrid) == len(mygrid))
for i in range(len(mygrid)):
    assert(newgrid[i] == mygrid[i])

os.unlink('test.dat')
