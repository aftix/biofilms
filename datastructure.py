# datastructure.py

from collections import Counter
from math import isclose
from typing import List, Dict, Any, Union

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

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Cell):
            return NotImplemented
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

# Program constants
sim_params: Dict[str, Union[float, int]] = dict()
sim_params['spring_k'] = 1
sim_params['spring_relax_close'] = 0.04
sim_params['spring_relax_far'] = 0.04
sim_params['damping'] = 10
