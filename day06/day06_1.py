# --- Day 6: Universal Orbit Map ---
# Part One

import sys , string
from dataclasses import dataclass

# Class of the orbiting "planets"

@dataclass
class Planet:
    def __init__(self, name : str):
        self.name = name
        self.children = {}
        self.parent = None

    def AddParent(self, planet):
        self.parent = planet
    
    def AddChild(self, planet):
        self.children[planet.name] = planet
    
    def HasChild(self, name : str) -> bool:
        if name in self.children.keys(): return True
        else: return False

    def __repr__(self):
        return "Planet:" + self.name


def FindLinks(planet : Planet) -> int:
    links = 0
    if planet.parent:
        links = 1
        links += FindLinks(planet.parent)
    return links


# Should we debug or not.
debug = True

# List of the orbits from the input file
orbitList = []

# Open input orbit map file
# Input file has opcode and values split by comma
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


#example orbit list - The total number of direct and indirect orbits in this example is 42.
#        G - H       J - K - L
#       /           /
#COM - B - C - D - E - F
#               \
#                I
#orbitList = [["COM","B"],["B","C"],["C","D"],["D","E"],["E","F"],["B","G"],["G","H"],["D","I"],["E","J"],["J","K"],["K","L"]]

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

# iterate from all planets
totalLinks = 0
for planet in orbitDict:
    totalLinks += FindLinks(orbitDict[planet])
print(totalLinks)


