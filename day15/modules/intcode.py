'''
Init the Class IntCode with the instruction pointer and a pointer to the ComputerMem (program)
'''

from dataclasses import dataclass
from day15.modules.robot import Robot
from day15.modules.utils import Pointer
from day15.modules.parameter import Parameter


class IntCode:
    ''' Main class of the IntCode '''

    def __init__(self, pointer: Pointer, _code_list: list):
        self.blob = str(_code_list[pointer.instruction])  # Like '1102'
        # start at -2 in string. Like '02' from blob
        self.opcode = int(self.blob[-2:])
        self.pointer = pointer
        # Pointer to the rest of the computerMem or program.
        self.code_list = _code_list
        self.parameter = Parameter(self)

    def add(self):
        ''' function that Add two values together '''
        self.parameter.process(3, 2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        v2 = self.parameter.value[2]
        self.code_list[v2] = v0 + v1
        self.pointer.instruction += 4

    def multiply(self):
        ''' function that Multiply two values together '''
        self.parameter.process(3, 2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        v2 = self.parameter.value[2]
        self.code_list[v2] = v0 * v1
        self.pointer.instruction += 4

    def get_input(self, robot: Robot):
        ''' Gets input to the program '''
        self.parameter.process(1, 0)
        v0 = self.parameter.value[0]
        self.code_list[v0] = robot.handle_input()
        self.pointer.instruction += 2

    def send_output(self, robot: Robot):
        ''' sends output from the program '''
        self.parameter.process(1)
        v0 = self.parameter.value[0]
        robot.handle_output(v0)
        self.pointer.instruction += 2

    def jump_if_true(self):
        ''' sets the instruction pointer input values are equal '''
        self.parameter.process(2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        if v0 != 0:
            self.pointer.instruction = v1
        else:
            self.pointer.instruction += 3

    def jump_if_false(self):
        ''' sets the instruction pointer input values are not equal '''
        self.parameter.process(2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        if v0 == 0:
            self.pointer.instruction = v1
        else:
            self.pointer.instruction += 3

    def if_less_than(self):
        ''' sets values in code list if they are smaller '''
        self.parameter.process(3, 2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        v2 = self.parameter.value[2]
        if v0 < v1:
            self.code_list[v2] = 1
        else:
            self.code_list[v2] = 0
        self.pointer.instruction += 4

    def if_equal(self):
        ''' sets values in code list if they are equal '''
        self.parameter.process(3, 2)
        v0 = self.parameter.value[0]
        v1 = self.parameter.value[1]
        v2 = self.parameter.value[2]
        if v0 == v1:
            self.code_list[v2] = 1
        else:
            self.code_list[v2] = 0
        self.pointer.instruction += 4

    def change_relative_pointer(self):
        ''' adds to the relative pointer from parameter '''
        self.parameter.process(1)
        v0 = self.parameter.value[0]
        self.pointer.relative += v0
        self.pointer.instruction += 2

    def __repr__(self):
        return f"OpCode: {self.opcode}"
