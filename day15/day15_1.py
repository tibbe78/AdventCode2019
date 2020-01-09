''' The main program '''
# --- Day 15: Oxygen System ---
# Part One

import sys
from day15.modules.robot import Robot
from day15.modules.intcode import IntCode


def check_command(int_code: IntCode, robot: Robot):
    ''' check the OpsCode and execute correct function '''
    if int_code.opcode == 1:
        int_code.add()
    elif int_code.opcode == 2:
        int_code.multiply()
    elif int_code.opcode == 3:
        int_code.get_input(robot)
    elif int_code.opcode == 4:
        int_code.send_output(robot)
    elif int_code.opcode == 5:
        int_code.jump_if_true()
    elif int_code.opcode == 6:
        int_code.jump_if_false()
    elif int_code.opcode == 7:
        int_code.if_less_than()
    elif int_code.opcode == 8:
        int_code.if_equal()
    elif int_code.opcode == 9:
        int_code.change_relative_pointer()
    elif int_code.opcode == 99:
        print("OpCode 99 Exit")
        sys.exit(0)
    else:
        print("Error no opCode??!!")
        sys.exit(0)


def get_codelist() -> list():
    ''' Parse the input text file and return a list och the OpsCode '''
    try:
        file = open('day15/day15_input.txt', 'r')
    except IOError:
        print("Can't open file!!")
        sys.exit(0)
    line_raw = file.readline().strip()
    return list(map(int, line_raw.split(","))).copy()


def main():
    ''' The main function '''
    robot = Robot("Wall-E")

    code_list = get_codelist()

    # instruction pointer in the opcode so we know where in the code we are.
    position_pointer = 0

    # Relative Base Pointer, will be changed by the program.
    relative_pointer = 0

    # Go through the intcode command list and check the values
    while position_pointer < len(code_list):

        # init the IntCode class
        int_code = IntCode(position_pointer, code_list)
        int_code.set_relative_pointer(relative_pointer)  # set the basePointer

        check_command(int_code, robot)

        # Get back the updated instruction pointer
        position_pointer = int_code.get_instruction_pointer()
        # and also the BasePointer or as called Relative Pointer.
        relative_pointer = int_code.get_relative_pointer()


# Run the main program
main()
