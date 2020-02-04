# simulate.py

from datastructure import ForceLink, Cell, MakeForceLink, Params
from typing import List, Tuple
from collections import Counter
import numpy

"""
Find Forces between cells and return as a matrix
"""
def FindForces(params: Params, grid: List[Cell]) -> List[ForceLink]:
    forces: List[ForceLink] = list()
    for i in range(len(grid)):
        for j in range(i, len(grid)):
            dist: float = numpy.linalg.norm(grid[i].pos - grid[j].pos)
            if j in grid[i].close:
                force: float = params['spring_k'] * (
                            params['spring_relax_close'] - dist
                )
                rel: float = params['spring_relax_close']
            elif j in grid[i].far:
                force = params['spring_k'] * (
                            params['spring_relax_far'] - dist
                )
                rel = params['spring_relax_far']
            else:
                continue

            if force < 1e-15:
                force = 0
            newlink = MakeForceLink(parties=(i,j), val=force, relax=rel)
            forces.append(newlink)
    return forces

"""
Forcing function for ODE solver
y's are interlaced pos as x y x y x y
"""
def StepForce(t, y, grid, params, sols):
    derivs = numpy.zeros(len(y))
    for i in range(len(grid)):
        for j in range(i, len(grid)):
            dist: float = numpy.linalg.norm(y[i*2:i*2+2] - y[j*2:j*2+2])
            if j in grid[i].close:
                force: float = params['spring_k'] * (
                            params['spring_relax_close'] - dist
                )
                rel: float = params['spring_relax_close']
            elif j in grid[i].far:
                force = params['spring_k'] * (
                            params['spring_relax_far'] - dist
                )
                rel = params['spring_relax_far']
            else:
                continue

            if force < 1e-15:
                force = 0
            AtoB = y[j*2:j*2+2] - y[i*2:i*2+2]
            unitDist = AtoB / dist
            derivs[i*2:i*2+2] += (force * unitDist)
            derivs[j*2:j*2+2] -= (force * unitDist)
    newgrid = grid
    for i, cell in enumerate(newgrid):
        cell.pos = y[i*2:i*2+2]
        cell.force = derivs[i*2:i*2 + 2]
    sols.append([newgrid])
    derivs /= -params['damping']
    return derivs

"""
Update the force values on the cells themselves
"""
def UpdateCellForces(params: Params, grid: List[Cell], forces: List[ForceLink]) -> None:
    for cell in grid:
        cell.force = numpy.zeros(2)

    for f in forces:
        A, B = f.parties
        AtoB = (grid[B].pos - grid[A].pos)
        unitDist = AtoB / numpy.linalg.norm(AtoB)
        grid[A].force = grid[A].force + f.val * unitDist
        grid[B].force = grid[B].force - f.val * unitDist
