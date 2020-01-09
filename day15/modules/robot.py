''' Program of the repair droid '''

import random
from day15.modules.plate import Plate
from day15.modules.utils import Vector2D

# 0: The repair droid hit a wall. Its position has not changed.
# 1: The repair droid has moved one step in the requested direction.
# 2: its new position is the location of the oxygen system.

HIT_WALL = 0
MOVE_OK = 1
FOUND_EXIT = 2

# Storage types for Plates
EMPTY = 0
WALL = 1
EXIT = 2

class Robot:
    ''' class of the repair droid '''

    def __init__(self, name):
        # x, y position
        self.position = Vector2D()
        self.name = name
        # Dictionary of Hull Plates
        self.hull = {}
        # north (1), south (2), west (3), and east (4)
        self.direction = 1
        self.status = None

    def get_plate(self, plate: Plate):
        ''' check if a plate exist othervise add it '''
        if not plate.name in self.hull.keys():
            self.hull[plate.name] = plate
        else:
            self.hull[plate.name].times_traversed += 1

    def turn(self):
        ''' function to change direction of the droid '''
        # north (1), south (2), west (3), and east (4)
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.randint(1, 4)
        self.direction = new_direction

    def move(self, _type):
        ''' function to move the droid '''
        # Take on step in direction
        if self.direction == 1:
            self.position.y -= 1
        elif self.direction == 2:
            self.position.y += 1
        elif self.direction == 3:
            self.position.x -= 1
        elif self.direction == 4:
            self.position.x += 1
        self.get_plate(Plate(self.position.x, self.position.y, _type))
        if random.randint(0, 3) == 1:
            self.turn()

    def mark_wall(self):
        ''' function to mark a wall been hit '''
        temp_pos = Vector2D(self.position.x, self.position.y)
        if self.direction == 1:
            temp_pos.y -= 1
        elif self.direction == 2:
            temp_pos.y += 1
        elif self.direction == 3:
            temp_pos.x -= 1
        elif self.direction == 4:
            temp_pos.x += 1
        self.get_plate(Plate(temp_pos.x, temp_pos.y, WALL))

    def handle_input(self) -> int:
        ''' function to handle input to the computer '''
        return self.direction

    def handle_output(self, output):
        ''' function to handle output from to the computer
        0: The repair droid hit a wall. Its position has not changed.
        1: The repair droid has moved one step in the requested direction.
        2: its new position is the location of the oxygen system.
        '''
        if output == HIT_WALL:
            self.status = HIT_WALL
            self.mark_wall()
            self.turn()
        elif output == MOVE_OK:
            self.status = MOVE_OK
            self.move(EMPTY)
        elif output == EXIT:
            self.status = EXIT
            self.move(EXIT)
            print("Found the exit")
        else:
            print("Error wrong output!!")

    def __repr__(self):
        return self.name
