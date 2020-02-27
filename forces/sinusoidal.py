# forces/sinusoidal.py

import numpy

def LowerLeftSine(t, y, grid, params):
    forces = numpy.zeros(2)
    forces[0] = params['sineamp'] * numpy.sin(params['sineomega'] * t)
    return forces
