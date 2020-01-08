''' Day 14: Space Stoichiometry
 Part One
 Trying to follow PEP8 Style Guide.
'''

import sys
import math
from day14.modules.reaction import Reaction
from day14.modules.reaction import Chemical
from day14.modules.reaction import Ingredient

CHEMICALS = {}

TOTAL_ORE = 1000000000000

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
        for ingredient in line_split[0].split(','):
            quantity, name = split_text(ingredient)
            chemical = add_chemical(name)
            ingredient = Ingredient(chemical, reaction, quantity)
            reaction.add_ingredient(ingredient)
    file.close()


def recursive_ore(_name: str, _quantity: int) -> int:
    ''' Recursively find the ore needed '''
    # Create a multiplier for the amount needed of this reaction.

    _chemical = CHEMICALS[_name]

    if _chemical.left_over >= _quantity:
        _chemical.left_over -= _quantity
        return 0

    float_value = (_quantity - _chemical.left_over)  / _chemical.reaction.quantity
    reaction_multiplier = int(math.ceil(float_value))

    # figure out how much of the chemical is left over after the reaction
    chemical_produced = (_chemical.reaction.quantity * reaction_multiplier) + _chemical.left_over
    _chemical.left_over = chemical_produced - _quantity

    ore = 0

    # Go through each ingredient in this reaction and run this function
    for ingredient in CHEMICALS[_name].reaction.ingredients.values():
        if ingredient.chemical.name == 'ORE':
            ore += ingredient.quantity * reaction_multiplier
        else:
            ore += recursive_ore(ingredient.chemical.name, ingredient.quantity * reaction_multiplier)
    return ore


# Run the main program
main()

# get the ore needed
print("Ore needed is: {}".format(recursive_ore('FUEL', 1)))
