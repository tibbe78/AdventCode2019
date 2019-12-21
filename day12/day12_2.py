# --- Day 12: The N-Body Problem ---
# Part Two
import sys
from typing import List
from day12.modules.moon import Moon
from math import gcd
import copy

def lcm(x, y, z):
    # return Least common Multiplier for three values.
    a = x * y // gcd(x, y)
    return (a * z // gcd(a, z))

# Main Code -------------------------------------------------

# moons Real
moonlist: List[Moon] = list()
moonlist.append(Moon(0, "Io",12,0,-15))
moonlist.append(Moon(1, "Europa",-8,-5,-10))
moonlist.append(Moon(2, "Ganymede",7,-17,1))
moonlist.append(Moon(3, "Callisto",2,-11,-6))

#Example 1 returns after 2772 time
""" moonlist: List[Moon] = list()
moonlist.append(Moon(0, "Io",-1,0,2))
moonlist.append(Moon(1, "Europa",2,-10,-7))
moonlist.append(Moon(2, "Ganymede",4,-8,8))
moonlist.append(Moon(3, "Callisto",3,5,-1)) """

# Example 2 returns after 4686774924 time
""" moonlist: List[Moon] = list()
moonlist.append(Moon(0, "Io",-8,-10,0))
moonlist.append(Moon(1, "Europa",5,5,10))
moonlist.append(Moon(2, "Ganymede",2,-7,3))
moonlist.append(Moon(3, "Callisto",9,-8,-3)) """

moonlist2 = copy.deepcopy(moonlist)

periods = list()
# Calc Velocity and Position
# Find period over one dimension at a time.
for axis in range(3):
    notFound = True
    period = 0
    while notFound:
        state = 0
        period += 1
        # Calc Velocity only for x axis
        for moon in moonlist:
            moon.FindPeriod1(axis,moonlist)
        # Calc Position only for x axis
        for moon in moonlist:
            moon.FindPeriod2(axis)
        # find when they are all back at start
        for i in range(4):
            if moonlist[i].position[axis] == moonlist2[i].position[axis] and moonlist[i].velocity[axis] == moonlist2[i].velocity[axis]:
                state += 1
            else:
                state = 0
                break
        if state == 4:
            periods.append(period)
            period = 0
            notFound = False

print("The Periods of each axis are: {}".format(periods))
LCM = lcm(periods[0],periods[1],periods[2])
print("The Least Common Multipler for the periods are: {}".format(LCM))
