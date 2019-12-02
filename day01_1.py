# --- Day 1: The Tyranny of the Rocket Equation ---
# Part One

import math 

# Should we debug or not.
debug = False

# Total Fuel required and also what we should calculate
totalFuel = 0

# Function to calculate the fuel for a mass
def CalcFuel(mass):
    return int(math.floor(mass / 3)) -2

# Open input file and calculate fuel for each module
# Input file has the mass och each module on each row
with open('day01_input.txt') as openFile:
    for count, line in enumerate(openFile):
        moduleMass = int(line.strip())
        if debug: print("Module mass: " + str(moduleMass))
        fuelRequired = CalcFuel(moduleMass)
        totalFuel += fuelRequired
        if debug: print("Fuel required: " + str(fuelRequired) + '\n')
openFile.close()

print("The total amount of fuel required is: " + str(totalFuel) + '\n')