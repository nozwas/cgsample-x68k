# -*- coding: shift_jis -*-
# cg03: xbasip demo cg
# nozwas <https://github.com/nozwas>

from xbasip.console import *
from xbasip.graph import *
from math import sqrt, pi, cos

SCALE = 200
STEP = 4
OFFSET_X = (768 - 3 * SCALE) // 2
OFFSET_Y = SCALE * 2
COLOR = 9

@micropython.native
def draw():
    hi = [-9999] * SCALE * 3
    lo = [+9999] * SCALE * 3
    for y in range(-SCALE, SCALE, STEP):
        if inkey0() != 0:
            break
        for x in range(-SCALE, SCALE, STEP):
            t = pi * sqrt(x * x + y * y) / SCALE
            z = int(SCALE // 2 * (cos(t) - 0.3 * cos(t * 3)))
            xx = x - (y + SCALE) // 2 + SCALE * 2
            yy = z + (y + SCALE) // 2
            if yy < lo[xx] or yy > hi[xx]:
                pset(OFFSET_X + xx, OFFSET_Y - yy, COLOR)
                lo[xx] = min(yy, lo[xx])
                hi[xx] = max(yy, hi[xx])
    
screen(2, 0, 1, 1)
key_off()
cursor_off()
keyflush()
draw()
end()
