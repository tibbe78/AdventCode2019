#!/usr/bin/env python3
# --- Day 13: Care Package ---
# Part Two

import sys
from day13.packages.render.arcade_game import ArcadeWindow

def main():
    try:
        file = open('./day13_input.txt', 'r')
    except IOError:
        print("Can't open file!!")
        sys.exit(0)
    opCodeRaw = file.readline().strip()
    file.close()
    opCodeList = list(map(int, opCodeRaw.split(","))).copy()
    
    startValue = 2
    _arcadeWindow = ArcadeWindow()
    _arcadeWindow.setup(opCodeList,startValue)
    _arcadeWindow.start()


if __name__ == "__main__":
    main()