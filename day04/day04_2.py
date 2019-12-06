# --- Day 4: Secure Container ---
# Part Two

import sys , string

from datetime import datetime, timedelta

passMin = 240298
passMax = 784956

debug = False

# Two adjacent digits are the same (like 22 in 122345).
# digits aren't smaller. left to right.

startTime = datetime.now()

j = 0
# Brute Force each number....
for n in range(passMin,passMax):
    # Split int as digits
    a = [int(d) for d in str(n)]
    if (a[5] >= a[4]) and (a[4] >= a[3]) and (a[3] >= a[2]) and (a[2] >= a[1] and (a[1] >= a[0])):
        if (a[0] == a[1]) or (a[1] == a[2]) or (a[2] == a[3]) or (a[3] == a[4]) or (a[4] == a[5]):
            match = 0
            if (a[0] == a[1]) and (a[1] != a[2]): match += 1
            if (a[1] == a[2]) and (a[2] != a[3]) and (a[1] != a[0]): match += 1
            if (a[2] == a[3]) and (a[3] != a[4]) and (a[2] != a[1]): match += 1
            if (a[3] == a[4]) and (a[4] != a[5]) and (a[3] != a[2]): match += 1
            if (a[4] == a[5]) and (a[4] != a[3]): match += 1
            if (match > 0):     
                j+=1
                if debug: 
                    print(a)
                    print(match)
print (j)
elapsedTime = datetime.now() - startTime
print("It took: " + str(elapsedTime.total_seconds()) + " Seconds")



"""
An Elf just remembered one more important detail: 
the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

You arrive at the Venus fuel depot only to discover it's protected by a password. 
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 240298-784956. """