# forces/step.py

import numpy

def StopGoConst(t, y, grid, i, params):
    if int(t) % 10 == 0:
        grid[i].fixed = False
        return numpy.array([params['extforce_x'], 0])
    grid[i].fixed = True
    return numpy.zeros(2)
