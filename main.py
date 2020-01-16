#!/usr/bin/env python3

# main.py

import generation
import gfx

mygrid = generation.generate_offsetgrid(nrows=10, size=0.008)

gfx.plot_cells(mygrid)
