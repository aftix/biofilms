# datastructure.py

from collections import Counter
from math import isclose


class Cell(object):
    def __init__(self, x=0, y=0, rad=0.05, close=list(), far=list()):
        self.x = x
        self.y = y
        self.rad = rad
        self.close = close
        self.far = far

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, rhs):
        return isclose(self.x, rhs.x) and isclose(self.y, rhs.y) \
                and isclose(self.rad, rhs.rad) \
                and Counter(self.close) == Counter(rhs.close) \
                and Counter(self.far) == Counter(rhs.far)

def MakeCell(x=0, y=0, rad=0.05, close=list(), far=list()):
    return Cell(x, y, rad, close, far)

# Spring constant
spring_k = 1
# Relaxed length for springs between close neighbors
spring_relax_close = 0.04
# Relaxed length for spring between far neighbors
spring_relax_far = 0.04

# Coeffecient of damping
damping = 10
