''' Day 14: Space Stoichiometry
 Part One
 Trying to follow PEP8 Style Guide.
'''

import sys
from day14.modules.reaction import *

REACTIONS = {}
CHEMICALS = {}

def add_chemical(name) -> Chemical:
    ''' Add a chemical to constant if needed '''
    if name not in CHEMICALS.keys():
        CHEMICALS[name] = Chemical(name)
    return CHEMICALS[name]


def split_text(text) -> [int, str]:
    ''' split the text input on a space and return a list with a str and int '''
    return [int(i) if i.isdigit() else i for i in text.strip().split(' ')]


def main():
    ''' Main Program '''

    try:
        file = open('day14/day14_input.txt', 'r')
    except IOError:
        print("Can't open file!!")
        sys.exit(0)

    for line in file:
        line_split = line.strip().split(' => ')
        quantity, name = split_text(line_split[1])
        chemical = add_chemical(name)
        reaction = Reaction(chemical, quantity)
        chemical.reaction = reaction
        chemical.quantity = quantity
        REACTIONS[reaction.name] = reaction
        for ingredient in line_split[0].split(','):
            quantity, name = split_text(ingredient)
            chemical = add_chemical(name)
            ingredient = Ingredient(chemical, reaction, quantity)
            reaction.add_ingredient(ingredient)
            chemical.add_ingredient(ingredient)
    file.close()

def recursive_level():
    print(CHEMICALS["ORE"])

# Run the main program
main()

# Set the level on each reaction.
recursive_level()
