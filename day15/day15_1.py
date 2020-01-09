''' The main program '''
# --- Day 15: Oxygen System ---
# Part One

import sys
import os
import time
from day15.modules.robot import Robot
from day15.modules.intcode import IntCode
from day15.modules.utils import Pointer
from day15.modules.rendergame import RenderGame

# 60 FPS
TIME_DELTA = 0.01666666666

def get_codelist() -> list():
    ''' Parse the input text file and return a list och the OpsCode '''
    try:
        file = open('day15/day15_input.txt', 'r')
    except IOError:
        print("Can't open file!!")
        sys.exit(0)
    line_raw = file.readline().strip()
    return list(map(int, line_raw.split(","))).copy()


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
        RenderGame.quit_game()
        sys.exit(0)
    else:
        print("Error no opCode??!!")
        sys.exit(0)


def main():
    ''' The main function '''

    # Set window position x,y
    #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    print("Initilizing...")
    time.sleep(2)
    display = RenderGame.init_game()
    start_time = time.perf_counter()
    robot = Robot("Wall-E")
    code_list = get_codelist()
    # instruction & relative pointer in the opcode so we know where in the code we are.
    pointer = Pointer()
    # Go through the intcode command list and check the values
    while pointer.instruction < len(code_list):
        int_code = IntCode(pointer, code_list)
        check_command(int_code, robot)
        # after and output command check if we should render screen
        if int_code.opcode == 4:
            if time.perf_counter() - start_time > TIME_DELTA:
                RenderGame.update_game(robot, display)



# Run the main program
main()
