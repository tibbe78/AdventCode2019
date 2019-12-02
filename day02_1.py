# --- Day 2: 1202 Program Alarm ---
# Part One

# Current position in the opcode
OpPosition = 0

# Open input opCode file run the computer based on the rules.
# Input file has opcode and values split by comma

file = open('day02_input.txt', 'r') 
print (file.readline())


print("The value left at position 0 is: " + '\n')



""" Once you have a working computer, 
the first step is to restore the gravity assist program (your puzzle input) 
to the "1202 program alarm" state it had just before the last computer caught fire. 
To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.

What value is left at position 0 after the program halts? """