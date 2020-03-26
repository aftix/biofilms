# forces/step.py

import numpy
from forces.restraint import LinRestraint

def StopGoConst(t, y, grid, i, params):
    constraint = LinRestraint(t, y, grid, i, params)
    if int(t) % 10 == 0:
        grid[i].fixed = False
        return numpy.array([params['extforce_x'], constraint[1]])
    grid[i].fixed = True
    return constraint
