'''
Class used in the intcode to process the parameters of the opcode
'''
from dataclasses import dataclass
from day15.modules.utils import Pointer
import day15.modules.intcode

@dataclass
class Parameter:
    ''' Class to handle the opcode parameters '''

    def __init__(self, parent: 'IntCode'):
        self.param = list()  # parameters to the opcode as a list.
        self.value = list()  # values based on parameter & mode as a list
        # the intcode parent
        self.parent: 'IntCode' = parent
        # parameter modes, end at -2 in string. like '11' from above '1102' blob
        mode_raw = parent.blob[:-2]
        # Reversed list of the parameters
        mode_list = list(mode_raw)[::-1]
        self.mode = [0, 0, 0]  # set the parameter modes default
        # find & set parameter modes like [0,1,1] from above raw pmodes.
        # for each parameter we have a setting for. Else 0
        for i in range(len(mode_list)):
            # set the pmode to the pmode in the list
            self.mode[i] = (int(mode_list[i]))


    def process(self, num: int, write_num=99):
        '''
        Set the parameters accompanying the Operation Code. Can be up to three
        parameters. num is equal to the amount of parameters and write_num specifies if one
        of them is the write parameter and should be handled specially.
        '''
        for i in range(num):  # Create one parameter at the time.
            # the location of the parameter in the Computer Mem
            location: Pointer = self.parent.pointer.instruction+(i+1)
            # Create the parameter to the opcode.
            self.param.append(self.parent.code_list[location])

            # if the parameter refers to a memory outside of range, add more memory
            # not applicable for direct mode.
            if (self.mode[i] == 0 or self.mode[i] == 2):
                if self.mode[i] == 2:
                    total_memory = self.parent.pointer.relative + self.param[i]
                else:
                    total_memory = self.param[i]
                if total_memory >= len(self.parent.code_list):
                    # Add the amount of memory missing
                    self.parent.code_list.extend(
                        [0] * total_memory-len(self.parent.code_list))

            # If the mode to parameter is 0 = Position mode.
            if self.mode[i] == 0:
                if i == write_num:
                    # if this is the write parameter send only back location
                    self.value.append(self.param[i])
                else:
                    # Else send back value of location
                    self.value.append(self.parent.code_list[self.param[i]])

            # If the mode to parameter is 1 = Direct mode.
            elif self.mode[i] == 1:
                self.value.append(self.param[i])

            # If the mode to parameter is 2 = Relative mode
            elif self.mode[i] == 2:
                if i == write_num:
                    self.value.append(self.parent.pointer.relative + self.param[i])
                else:
                    self.value.append(
                        self.parent.code_list[self.parent.pointer.relative + self.param[i]])
            else:
                print("Error unknown parameter mode!!")

    def __repr__(self):
        return f"Parameter: {self.parent.blob}"
