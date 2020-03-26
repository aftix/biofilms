# inout.py

import jsonpickle
import _io
from typing import List, Any, Tuple
from datastructure import Cell, Params

def serialize_cell(cell: Cell, ofile: _io.TextIOWrapper) -> None:
    ofile.write(jsonpickle.dumps(cell))
    ofile.write('\n')

def serialize_cellmatrix(grid: List[Cell], ofile: _io.TextIOWrapper) -> None:
    ofile.write(str(len(grid)))
    ofile.write('\n')
    for cell in grid:
        serialize_cell(cell, ofile)

def deserialize_cell(ifile: _io.TextIOWrapper) -> Any:
    return jsonpickle.loads(ifile.readline())

def deserialize_cellmatrix(ifile: _io.TextIOWrapper) -> List[Cell]:
    numcells = int(ifile.readline())
    return [deserialize_cell(ifile) for i in range(numcells)]

def save(params: Params, grid: List[Cell], loc: str) -> None:
    with open(loc, "w") as f:
        f.write(jsonpickle.dumps(params))
        f.write('\n')
        serialize_cellmatrix(grid, f)

def load(loc: str) -> Tuple[Params, List[Cell]]:
    with open(loc, "r") as f:
        newparams = jsonpickle.loads(f.readline())
        grid = deserialize_cellmatrix(f)
    return newparams, grid
