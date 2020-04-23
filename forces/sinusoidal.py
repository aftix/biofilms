# forces/sinusoidal.py

import numpy
from forces.restraint import LinRestraint

def Sine(t, y, grid, i, params):
    forces = numpy.zeros(2)
    forces[0] = params['sineamp'] * numpy.sin(params['sineomega'] * t)
    return forces

def SineConstrained(t, y, grid, i, params):
    constraint = LinRestraint(t, y, grid, i, params)
    force = params['sineamp'] * numpy.sin(params['sineomega'] * t)
    return numpy.array([force + constraint[0], constraint[1]])
