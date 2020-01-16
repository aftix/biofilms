# datastructure.py

from collections import namedtuple

class Cell:
    def __init__(self, x=0, y=0, rad=0.05, neighbors=list()):
        self.x = x
        self.y = y
        self.rad = rad
        self.neighbors = neighbors

def MakeCell(x=0, y=0, rad=0.05, neighbors=list()):
    return Cell(x, y, rad, neighbors)
