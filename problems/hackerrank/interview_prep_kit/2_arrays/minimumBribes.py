#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    numBribes = 0
    for i in range(len(q)):
        counter = 0
        for j in range(len(q)):
            if q[j] - (j + 1) > 2:
                print("Too chaotic")
                return
            if j < len(q) - 1 and q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                numBribes += 1
            else:
                counter += 1
        if counter == len(q):
            break
    print(numBribes)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
