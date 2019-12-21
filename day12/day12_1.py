# --- Day 12: The N-Body Problem ---
# Part One
import sys
from typing import List
from day12.modules.moon import Moon

# Main Code -------------------------------------------------

# moons
moonlist: List[Moon] = list()
moonlist.append(Moon(0,"Io",12,0,-15))
moonlist.append(Moon(1,"Europa",-8,-5,-10))
moonlist.append(Moon(2,"Ganymede",7,-17,1))
moonlist.append(Moon(3,"Callisto",2,-11,-6))

time = 0

# Calc Velocity and Position
for time in range (1000):
    # Calc Velocity
    for moon in moonlist:
        moon.CalcGravity(moonlist)
    # Calc Position
    for moon in moonlist:
        moon.CalcPosition()

totalEnergy = 0
# Calc Energy in system
for moon in moonlist:
        totalEnergy += moon.CalcEnergy()

print("The total energy in the system is: {}".format(totalEnergy))

