'''
Init the Class IntCode with the instruction pointer and a pointer to the ComputerMem (program)
'''

from day15.modules.robot import Robot


class IntCode:
    ''' Main class of the IntCode '''

    def __init__(self, _position_pointer: int, _code_list: list):
        self.blob = str(_code_list[_position_pointer])  # Like '1102'
        # start at -2 in string. Like '02' from blob
        self.opcode = int(self.blob[-2:])
        self.param = list()  # parameters to the opcode as a list.
        self.value = list()  # values based on parameter & mode as a list
        # parameter modes, end at -2 in string. like '11' from above '1102' blob
        self.param_mode_raw = self.blob[:-2]
        # Reversed list of the parameters
        self.param_mode_list = list(self.param_mode_raw)[::-1]
        self.param_mode = [0, 0, 0]  # set the parameter modes default
        self.position_pointer = _position_pointer
        self.relative_pointer = None
        # Pointer to the rest of the computerMem or program.
        self.code_list = _code_list
        # find & set parameter modes like [0,1,1] from above raw pmodes.
        # for each parameter we have a setting for. Else 0
        for i in range(len(self.param_mode_list)):
            # set the pmode to the pmode in the list
            self.param_mode[i] = (int(self.param_mode_list[i]))

    def get_instruction_pointer(self) -> int:
        ''' Returns the instruction pointer '''
        return self.position_pointer

    def set_relative_pointer(self, _relative_pointer: int):
        ''' sets the relative base pointer '''
        self.relative_pointer = _relative_pointer

    def get_relative_pointer(self) -> int:
        ''' gets the relative base pointer '''
        return self.relative_pointer

    def set_parameters(self, num, write_num=9):
        '''
        Set the parameters accompanying the Operation Code. Can be up to three
        parameters. num is equal to the amount of parameters and write_num specifies if one
        of them is the write parameter and should be handled specially.
        '''
        for i in range(num):  # Create one parameter at the time.
            # the location of the parameter in the Computer Mem
            param_location = self.position_pointer+(i+1)
            # Create the parameter to the opcode.
            self.param.append(self.code_list[param_location])

            # if the parameter refers to a memory outside of range, add more memory
            # not applicable for direct mode.
            if (self.param_mode[i] == 0 or self.param_mode[i] == 2):
                if self.param_mode[i] == 2:
                    total_memory = self.relative_pointer + self.param[i]
                else:
                    total_memory = self.param[i]
                if total_memory >= len(self.code_list):
                    # Add the amount of memory missing
                    for j in range(total_memory-len(self.code_list)+1):
                        self.code_list.append(0)

            # If the mode to parameter is 0 = Position mode.
            if self.param_mode[i] == 0:
                if i == write_num:
                    # if this is the write parameter send only back location
                    self.value.append(self.param[i])
                else:
                    # Else send back value of location
                    self.value.append(self.code_list[self.param[i]])

            # If the mode to parameter is 1 = Direct mode.
            elif self.param_mode[i] == 1:
                self.value.append(self.param[i])

            # If the mode to parameter is 2 = Relative mode
            elif self.param_mode[i] == 2:
                if i == write_num:
                    self.value.append(self.relative_pointer + self.param[i])
                else:
                    self.value.append(
                        self.code_list[self.relative_pointer + self.param[i]])

            else:
                print("Error!!")

    def add(self):
        ''' function that Add two values together '''
        self.set_parameters(3, 2)
        self.code_list[self.value[2]] = self.value[0] + self.value[1]
        self.position_pointer += 4

    def multiply(self):
        ''' function that Multiply two values together '''
        self.set_parameters(3, 2)
        self.code_list[self.value[2]] = self.value[0] * self.value[1]
        self.position_pointer += 4

    def get_input(self, robot: Robot):
        ''' Gets input to the program '''
        self.set_parameters(1, 0)
        self.code_list[self.value[0]] = robot.move()
        self.position_pointer += 2

    def send_output(self, robot: Robot):
        ''' sends output from the program '''
        self.set_parameters(1)
        robot.HandleOutput(self.value[0])
        self.position_pointer += 2

    def jump_if_true(self):
        ''' sets the instruction pointer input values are equal '''
        self.set_parameters(2)
        if self.value[0] != 0:
            self.position_pointer = self.value[1]
        else:
            self.position_pointer += 3

    def jump_if_false(self):
        ''' sets the instruction pointer input values are not equal '''
        self.set_parameters(2)
        if self.value[0] == 0:
            self.position_pointer = self.value[1]
        else:
            self.position_pointer += 3

    def if_less_than(self):
        ''' sets values in code list if they are smaller '''
        self.set_parameters(3, 2)
        if self.value[0] < self.value[1]:
            self.code_list[self.value[2]] = 1
        else:
            self.code_list[self.value[2]] = 0
        self.position_pointer += 4

    def if_equal(self):
        ''' sets values in code list if they are equal '''
        self.set_parameters(3, 2)
        if self.value[0] == self.value[1]:
            self.code_list[self.value[2]] = 1
        else:
            self.code_list[self.value[2]] = 0
        self.position_pointer += 4

    def change_relative_pointer(self):
        ''' adds to the relative pointer from parameter '''
        self.set_parameters(1)
        self.relative_pointer += self.value[0]
        self.position_pointer += 2

    def __repr__(self):
        return "OpCode: {}".format(self.opcode)
