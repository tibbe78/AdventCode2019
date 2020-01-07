'''Module that contain the chemicals and the reactions'''


class Chemical:  # pylint: disable=too-few-public-methods
    '''Chemical is just one component of a reaction.
    But it also keeps track of all ingridients it's used in in
    '''
    def __init__(self, name: str):
        self.name = name
        self.ingredients = {}
        self.reaction = None
        self.quantity = 0

    def has_ingredient(self, name: str) -> bool:
        '''check if the ingredient has children'''
        return bool(name in self.ingredients.keys())

    def add_ingredient(self, ingredient: 'Ingredient'):
        '''Add a parent ingredient to a chemical'''
        if not self.has_ingredient(ingredient.name):
            self.ingredients[ingredient.name] = ingredient
        else:
            print("Error Ingredient exist!!")

    def __repr__(self):
        return "Chemical:{}".format(self.name)


class Reaction:
    '''A reaction containing children and a chemical + quantity as the result'''
    def __init__(self, chemical: Chemical, quantity: int):
        self.ingredients = {}
        self.quantity = quantity
        self.chemical = chemical
        # Which level in the tree structure of reactions this chemical is in.
        self.level = None
        self.name = "{}_{}".format(self.chemical.name, self.quantity)

    def has_ingredient(self, name: str) -> bool:
        '''check if the reaction has children'''
        return bool(name in self.ingredients.keys())

    def add_ingredient(self, ingredient: 'Ingredient'):
        '''Add a ingredient to a reaction'''
        if not self.has_ingredient(ingredient.name):
            self.ingredients[ingredient.name] = ingredient
        else:
            print("Error Ingredient exist!!")

    def __repr__(self):
        return "Reaction:{}_Quantity:{}".format(self.chemical.name, self.quantity)


class Ingredient:  # pylint: disable=too-few-public-methods
    '''SubClass of a reaction showing a child chemical + quantity'''
    def __init__(self, chemical: Chemical, reaction: Reaction, quantity: int):
        self.chemical = chemical
        self.reaction = reaction
        self.quantity = quantity
        self.name = "{}_{}".format(self.reaction.name, self.chemical.name)

    def __repr__(self):
        return "Reaction:{}_Ingredient:{}".format(self.reaction.name, self.chemical.name)
