#! /usr/bin/python3
# # --- Day 4: Secure Container ---
# Part One

import sys , string
from dataclasses import dataclass

passMin = 240298
passMax = 784956
passSize = passMax - passMin

passLenght = 5 # Cause two is the same.

# Two adjacent digits are the same (like 22 in 122345). = we can remove one digit in count.
# digits aren't smaller. left to right.

j = 0
# Brute Force each number....
for n in range(passMin,passMax):
    # Split an as digits
    a = [int(d) for d in str(n)]
    if (a[5] >= a[4]) and (a[4] >= a[3]) and (a[3] >= a[2]) and (a[2] >= a[1] and (a[1] >= a[0])):
        if (a[0] == a[1]) or (a[1] == a[2]) or (a[2] == a[3]) or (a[3] == a[4]) or (a[4] == a[5]):
            j+=1
print (j)


