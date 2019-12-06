# --- Day 6: Universal Orbit Map ---
# Part Two

import sys , string
from dataclasses import dataclass

# Class of the orbiting "planets"
@dataclass
class Planet:
    def __init__(self, name : str):
        self.name = name
        self.children = {}
        self.parent = None
        self.level = None

    def AddParent(self, planet):
        self.parent = planet
    
    def SetLevel(self, level):
        self.level = level
    
    def AddChild(self, planet):
        self.children[planet.name] = planet
    
    def HasChild(self, name : str) -> bool:
        if name in self.children.keys(): return True
        else: return False

    def __repr__(self):
        return "Planet:" + self.name +" L:" + str(self.level)

# Count Links between planets
def CountLinks(planet : Planet) -> int:
    links = 0
    if planet.parent:
        links = 1
        links += CountLinks(planet.parent)
    return links

# Set the level of each planet
def SetLevels(planet : Planet, level):
    planet.SetLevel(level)
    level += 1
    for child in planet.children:
        SetLevels(planet.children[child], level)

# Should we debug or not.
debug = True

# List of the orbits from the input file
orbitList = []

# Open input orbit map file
try:  
    file = open('day06_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

# Loop each line in file
for line in file:
    # split the orbit in parent child.
    parentChild = line.strip().split(')')
    orbitList.append(parentChild)
file.close()

#                          YOU
#                         /
#        G - H       J - K - L
#       /           /
#COM - B - C - D - E - F
#               \
#                I - SAN
#In this example, YOU are in orbit around K, and SAN is in orbit around I. 
#To move from K to I, a minimum of 4 orbital transfers are required:
#orbitList = ["COM","B"],["B","C"],["C","D"],["D","E"],["E","F"],["B","G"],["G","H"],["D","I"],["E","J"],["J","K"],["K","L"],["K","YOU"],["I","SAN"]

orbitDict = {}

# Init all the childs & parents
for pair in orbitList:
    parent = pair[0]
    child = pair[1]
    if parent not in orbitDict.keys(): orbitDict[parent] = Planet(parent)
    if child not in orbitDict.keys(): orbitDict[child] = Planet(child)


# fill in the links between the parents & childs
for pair in orbitList:
    parent = pair[0]
    child = pair[1]
    if orbitDict[parent].HasChild(child): print("ERRORR!!!")
    else: 
        orbitDict[parent].AddChild(orbitDict[child])
        orbitDict[child].AddParent(orbitDict[parent])


# set the planet levels
SetLevels(orbitDict["COM"],0)

# Which level are we on?
youLev = orbitDict["YOU"].parent.level
santaLev = orbitDict["SAN"].parent.level

# find list back for both to compare
print("You on Level: " + str(youLev))
print("Santa on Level: " + str(santaLev))
level = youLev
you = orbitDict["YOU"].parent
SAN = orbitDict["SAN"].parent
jumps = 0
while level > 0:
    if you.name == SAN.name: 
        print("Found first: " + SAN.name + ". " + str(jumps) + " jumps away")
        break
    if you.level >= SAN.level:
        jumps += 1
        you = you.parent
    elif SAN.level >= you.level:
        jumps += 1
        SAN = SAN.parent

