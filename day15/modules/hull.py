''' Class of the hull of the ship that is a grid of plates '''


class Plate:
    ''' Class of one plate of the hull, like a pixel. '''

    def __init__(self, x, y, _type=0):
        # x, y position
        self.pos_x = x
        self.pos_y = y
        self.type = _type
        self.times_traversed = 1
        self.name = "P_{}_{}".format(self.pos_x, self.pos_y)

    def __repr__(self):
        return self.name


class Hull:
    ''' Class of the hull of the ship that is a dict of plates '''

    def __init__(self, name):
        # directory of Grid Plates
        self.grid = {}
        self.name = name

    def add_plate(self, plate: Plate):
        ''' add one plate to the grid and check the min max of the grid '''
        self.grid[plate.name] = plate

    def check_exists(self, plate: Plate):
        ''' check if a plate exist othervise add it '''
        if not plate.name in self.grid.keys():
            self.add_plate(plate)

    def get_type(self, plate) -> int:
        ''' get the type of a plate '''
        self.check_exists(plate)
        return self.grid[plate.name].type

    def set_type(self, plate):
        ''' set the type of a plate '''
        self.check_exists(plate)
        self.grid[plate.name].type = plate.type
        self.grid[plate.name].times_traversed += 1

    def __repr__(self):
        return self.name
