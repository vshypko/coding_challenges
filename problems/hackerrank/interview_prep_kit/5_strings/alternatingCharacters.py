#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    i = counter = 0

    while i < len(s) - 1:
        if not ((s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A')):
            counter += 1
        i += 1

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
