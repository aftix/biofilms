#!/usr/bin/env python3

# test.py

import generation
import graph
import inout

mygrid = generation.generate_offsetgrid(nrows=10, size=0.008)

inout.save(mygrid, 'test.dat')
newgrid = inout.load('test.dat')

assert(len(newgrid) == len(mygrid))
for i in range(len(mygrid)):
    assert(newgrid[i] == mygrid[i])

