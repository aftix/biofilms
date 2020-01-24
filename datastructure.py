# datastructure.py

from collections import Counter
from math import isclose
from typing import List, TypeVar

# Cell_t = TypeVar('Cell', bound='Cell')
class Cell(object):
    def __init__(self,\
            x: float=0,\
            y: float=0,\
            rad: float=0.05,\
            close: List[int]=list(),\
            far: List[int]=list()\
    ) -> None:
        self.x = x
        self.y = y
        self.rad = rad
        self.close = close
        self.far = far

    def __str__(self) -> str:
        return str(self.__dict__)

    def __eq__(self, rhs: 'Cell') -> bool:
        return isclose(self.x, rhs.x) and isclose(self.y, rhs.y) \
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

# Spring constant
spring_k: float = 1
# Relaxed length for springs between close neighbors
spring_relax_close: float = 0.04
# Relaxed length for spring between far neighbors
spring_relax_far: float = 0.04

# Coeffecient of damping
damping: float = 10
