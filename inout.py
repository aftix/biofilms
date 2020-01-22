# inout.py

import jsonpickle

def serialize_cell(cell, ofile):
    ofile.write(jsonpickle.dumps(cell))
    ofile.write('\n')

def serialize_cellmatrix(grid, ofile):
    ofile.write(str(len(grid)))
    ofile.write('\n')
    for cell in grid:
        serialize_cell(cell, ofile)

def deserialize_cell(ifile):
    return jsonpickle.loads(ifile.readline())

def deserialize_cellmatrix(ifile):
    numcells = int(ifile.readline())
    return [deserialize_cell(ifile) for i in range(numcells)]

def save(grid, loc):
    with open(loc, "w") as f:
        serialize_cellmatrix(grid, f)

def load(loc):
    with open(loc, "r") as f:
        grid = deserialize_cellmatrix(f)
    return grid
