# simulate.py

from datastructure import ForceLink, Cell, MakeForceLink, Params
from typing import List, Tuple, Union, Dict
from collections import Counter
import numpy
from math import isclose

"""
Forcing function for ODE solver
y's are interlaced pos as x y x y x y
"""
def StepForce(t, y, grid, params):
    derivs = numpy.zeros(len(y))

    lj_A: float = params['repl_epsilon'] * numpy.power(params['repl_min'], 12)
    lj_B: float = params['repl_epsilon'] * 2 * numpy.power(params['repl_min'], 6)

    for i in range(len(grid)):
        for j in range(i+1, len(grid)):
            AtoB = y[j*2:j*2+2] - y[i*2:i*2+2]
            dist: float = numpy.linalg.norm(AtoB)

            if j in grid[i].close:
                force: float = params['spring_k'] * (
                            dist - params['spring_relax_close']
                )
            elif j in grid[i].far:
                force = params['spring_k'] * (
                            dist - params['spring_relax_far']
                )
            else:
                continue

            if abs(force) < 1e-15:
                force = 0

            # LJ repulsion
            if dist < params['repl_dist']:
                force += (12 * lj_A * numpy.power(dist, -13) - lj_B * numpy.power(dist, -7))

            unitDist = AtoB / dist
            checknan = numpy.isnan(unitDist)
            checkinf = numpy.isinf(unitDist)
            if numpy.isfinite(unitDist).all() and numpy.isfinite(force):
                derivs[i*2:i*2+2] += (force * unitDist)
                derivs[j*2:j*2+2] -= (force * unitDist)
        if grid[i].fixed:
            derivs[i*2:i*2+2] = numpy.zeros(2)
        if grid[i].force:
            derivs[i*2:i*2+2] += grid[i].forceFunc(t, y[i*2:i*2+2], grid, i, params)
    derivs /= params['damping']
    return derivs

"""
Given a grid position, find bulk stress of each cell
"""
def GetStress(grid: List[Cell], params: Dict[str, Union[float, int, str]]) -> Tuple[float, float, float]:
    maxcompression: float = 0
    maxtension: float = 0
    avgstress: float = 0

    for i, cell in enumerate(grid):
        cell.stress = 0
        cell.tensorstress = numpy.zeros((2,2))

    for i in range(len(grid)):
        for j in range(i+1, len(grid)):
            direc = grid[i].pos - grid[j].pos
            dist: float = numpy.linalg.norm(direc)

            if j in grid[i].close:
                force: float = float(params['spring_k']) * (
                            dist - float(params['spring_relax_close'])
                )
            elif j in grid[i].far:
                force = float(params['spring_k']) * (
                        dist - float(params['spring_relax_far'])
                )
            else:
                continue


            if abs(force) < 1e-15:
                continue

            # vec F = |F| rhat
            rhat = direc / dist

            # S_i,ab = -0.5 sum(j, (r_i,a - r_j,a) * F_ij,b)
            # r_i,a - r_j,a = direc_a
            newstress = numpy.array([rhat * force, rhat * force])
            newstress *= numpy.transpose(numpy.array([direc, direc]))

            # neighbor is the same (F changes direction as well as direc)
            grid[i].tensorstress += newstress
            grid[j].tensorstress += newstress
        # At this point, stress is done calculating
        grid[i].tensorstress *= -0.5
        # bulk stress is the trace of diagonalized tensor stress
        # AKA sum of eigenvalues
        # The sum of eigenvalues IS THE TRACE!!!!
        grid[i].stress = grid[i].tensorstress[0,0] + grid[i].tensorstress[1,1]

        if grid[i].stress > maxcompression:
            maxcompression = grid[i].stress
        elif grid[i].stress < maxtension:
            maxtension = grid[i].stress
        avgstress += grid[i].stress
    avgstress /= len(grid)
    return maxcompression, maxtension, avgstress

