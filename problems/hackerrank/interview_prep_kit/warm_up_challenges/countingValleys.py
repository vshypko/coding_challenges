#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    seaLevel = 0
    valleyCounter = 0
    for c in s:
        prevSeaLevel = seaLevel
        if c == 'U':
            seaLevel += 1
        elif c == 'D':
            seaLevel -= 1
        if prevSeaLevel == -1 and seaLevel == 0:
            valleyCounter += 1
    return valleyCounter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
