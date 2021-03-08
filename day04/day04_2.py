#!/usr/bin/env python3
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

