# --- Day 1: The Tyranny of the Rocket Equation ---
# Part Two

import math 

# Should we debug or not.
debug = False

# Total Fuel required and also what we should calculate
totalFuel = 0

# Function to calculate the fuel for a mass
def CalcFuel(mass):
    return int(math.floor(mass / 3)) -2

# Open input file as read-only and calculate fuel for each module
# Input file has the mass och each module on each row
file = open('day01_input.txt', 'r') 
for line in file:
    moduleMass = int(line.strip())
    if debug: print("Module mass: " + str(moduleMass))
    fuelRequired = CalcFuel(moduleMass)
    # Calculate the fuel for the fuel until zero.
    while fuelRequired > 0:
        totalFuel += fuelRequired
        if debug: print("Fuel required: " + str(fuelRequired) + '\n')
        fuelRequired = CalcFuel(fuelRequired)
file.close()

print("The total amount of fuel required is: " + str(totalFuel) + '\n')