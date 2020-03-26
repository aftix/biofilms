# forces/restraint.py

import numpy

def LinRestraint(t, y, grid, i, params):
    force = numpy.zeros(2)
    if y[1] > 1:
        force[1] = params['restraint_k'] * (1 - y[1])
    elif y[1] < 0:
        force[1] = -params['restraint_k'] * y[1]
    return force

def LennardJones(t, y, grid, i, params):
    force = numpy.zeros(2)
    if y[1] > 1:
        force[1] = -4 * params['lj_epsilon'] * (
            12 * numpy.power(params['lj_sigma'], 12) * numpy.power(y[1] - 1, -13)
            - 6 * numpy.power(params['lj_sigma'], 6) * numpy.power(y[1] - 1, -7))
    elif y[1] < 0:
        force[1] = 4 * params['lj_epsilon'] * (
            12 * numpy.power(params['lj_sigma'], 12) * numpy.power(y[1], -13)
            - 6 * numpy.power(params['lj_sigma'], 6) * numpy.power(y[1], -7))
    return force

def TwelveForce(t, y, grid, i, params):
    force = numpy.zeros(2)
    if y[1] > 1:
        force[1] = - params['lj_epsilon'] * numpy.power((1 - y[1]), -12)
    elif y[1] < 0:
        force[1] = params['lj_epsilon'] * numpy.power(y[1], -12)
    return force
