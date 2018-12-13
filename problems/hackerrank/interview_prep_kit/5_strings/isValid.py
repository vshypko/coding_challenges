#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    hashmap = {}

    for c in s:
        if not c in hashmap.keys():
            hashmap[c] = 0
        hashmap[c] += 1

    valList = list(hashmap.values())
    maxVal = max(valList)
    minVal = min(valList)

    print(hashmap)

    if (valList.count(maxVal) == len(valList)
            or valList.count(maxVal - 1) == len(valList) - 1
            or (valList.count(maxVal) == len(valList) - 1 and valList.count(minVal) == 1)):
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
