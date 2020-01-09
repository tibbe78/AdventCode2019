''' Program of the repair droid '''
from day15.modules.hull import Hull


class Robot:
    ''' class of the repair droid '''

    def __init__(self, name):
        # x, y position
        self.pos_x = 0
        self.pos_y = 0
        # The hull of the ship.
        self.name = name
        self.hull = Hull("{}_hull".format(self.name))

    def move(self):
        ''' function to move the droid '''
        # Take on step in direction
        # 0=up, 1=right, 2=down, 3=left
        pass

    def handle_input(self) -> int:
        ''' function to handle input to the computer '''
        # Take on step in direction
        # 0=up, 1=right, 2=down, 3=left
        return 0
        pass

    def handle_output(self, output):
        ''' function to handle output from to the computer
        0: The repair droid hit a wall. Its position has not changed.
        1: The repair droid has moved one step in the requested direction.
        2: its new position is the location of the oxygen system.
        '''
        if output == 0:
        pass

    def __repr__(self):
        return self.name
