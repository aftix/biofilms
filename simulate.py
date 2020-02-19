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
    for i in range(len(grid)):
        for j in range(i, len(grid)):
            dist: float = numpy.linalg.norm(y[i*2:i*2+2] - y[j*2:j*2+2])
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
            AtoB = y[j*2:j*2+2] - y[i*2:i*2+2]
            unitDist = AtoB / dist
            derivs[i*2:i*2+2] += (force * unitDist)
            derivs[j*2:j*2+2] -= (force * unitDist)
        if grid[i].fixed:
            derivs[i*2:i*2+2] = numpy.zeros(2)
    derivs /= params['damping']
    return derivs

"""
Given a grid position, find bulk stress of each cell
"""
def BulkStress(grid: List[Cell], params: Dict[str, Union[float, int]]) -> Tuple[float, float]:
    maxtension: float = 0
    maxcompression: float = 0
    for i in range(len(grid)):
        grid[i].stress = 0
    for i in range(len(grid)):
        for j in range(i, len(grid)):
            dist: float = numpy.linalg.norm(grid[i].pos - grid[j].pos)
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
                continue
            grid[i].stress += force
            grid[j].stress += force
        if grid[i].stress > maxtension:
            maxtension = grid[i].stress
        elif grid[i].stress < maxcompression:
            maxcompression = grid[i].stress
    return maxtension, maxcompression

