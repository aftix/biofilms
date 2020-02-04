# prettify.py

import sys
import gfx

if len(sys.argv) < 2:
    direc: str = 'output/'
else:
    direc = sys.argv[1]
    if direc[-1] != '/':
        direc += '/'


