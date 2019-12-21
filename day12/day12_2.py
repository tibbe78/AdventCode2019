# --- Day 12: The N-Body Problem ---
# Part Two
import sys
from typing import List
from day12.modules.moon import Moon

# Main Code -------------------------------------------------

# moons Real
""" moonlist: List[Moon] = list()
moonlist.append(Moon(0, "Io",12,0,-15))
moonlist.append(Moon(1, "Europa",-8,-5,-10))
moonlist.append(Moon(2, "Ganymede",7,-17,1))
moonlist.append(Moon(3, "Callisto",2,-11,-6)) """

#Example 2
moonlist: List[Moon] = list()
moonlist.append(Moon(0, "Io",-1,0,2))
moonlist.append(Moon(1, "Europa",2,-10,-7))
moonlist.append(Moon(2, "Ganymede",4,-8,8))
moonlist.append(Moon(3, "Callisto",3,5,-1))

# Calc Velocity and Position
# Find period over one dimension
notFound = True
while notFound:
    # Calc Velocity
    for moon in moonlist:
        moon.CalcGravity(moonlist)
    # Calc Position
    for moon in moonlist:
        moon.CalcPosition()


