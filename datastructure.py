# datastructure.py

from collections import Counter
from math import isclose
from typing import List, Dict, Any, Union, Tuple
import numpy

# Program constants
Params = Dict[str, Union[float, int]]
def BeginParams() -> Params:
    sim_params: Params = dict()
    sim_params['spring_k'] = 1
    sim_params['spring_relax_close'] = 0.04
    sim_params['spring_relax_far'] = 0.04
    sim_params['damping'] = 10
    return sim_params

# Cell object
class Cell(object):
    def __init__(self,\
            x: float=0,\
            y: float=0,\
            rad: float=0.05,\
            close: List[int]=list(),\
            far: List[int]=list()\
    ) -> None:
        self.pos = numpy.array([x, y])
        self.rad = rad
        self.close = close
        self.far = far
        self.force = numpy.zeros(2)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Cell):
            return NotImplemented
        return isclose(self.pos[0], rhs.pos[0]) and isclose(self.pos[1], rhs.pos[1]) \
                and isclose(self.rad, rhs.rad) \
                and Counter(self.close) == Counter(rhs.close) \
                and Counter(self.far) == Counter(rhs.far)

def MakeCell(\
        x: float=0,\
        y: float=0,\
        rad: float=0.05,\
        close: List[int]=list(),\
        far: List[int]=list()
) -> Cell:
    return Cell(x, y, rad, close, far)

# Force link between two cells. This is the actual force calculated, not the spring
# Contains attached cells, amount of force, and relaxed length
class ForceLink(object):
    def __init__(self, parties: Tuple[int, int], val: float=0, relax: float=0) -> None:
        self.parties = parties
        self.val = val
        self.relax = relax

    def __str__(self) -> str:
        return str(self.__dict__)

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, ForceLink):
            return NotImplemented
        return Counter(self.parties) == Counter(rhs.parties) and isclose(self.val, rhs.val) \
                and isclose(self.relax, rhs.relax)

def MakeForceLink(parties: Tuple[int, int], val: float, relax: float=0) -> ForceLink:
    return ForceLink(parties=parties, val=val, relax=relax)
