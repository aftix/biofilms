# forces/constant.py

import numpy

def ConstRightForce(t, y, grid, i, params):
    return numpy.array([params['extforce_x'], 0])
