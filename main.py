#!/usr/bin/env python3

# main.py

import generation
import graph
import inout

mygrid = generation.generate_offsetgrid(nrows=10, size=0.008)

graph.plot_cells(mygrid)

