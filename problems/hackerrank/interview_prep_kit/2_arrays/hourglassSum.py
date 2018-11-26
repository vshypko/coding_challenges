#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = float('-inf')

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            topLeft     = arr[i-1][j-1]
            top         = arr[i-1][j]
            topRight    = arr[i-1][j+1]
            current     = arr[i][j]
            bottomLeft  = arr[i+1][j-1]
            bottom      = arr[i+1][j]
            bottomRight = arr[i+1][j+1]
            currentSum = topLeft + top + topRight + current + bottomLeft + bottom + bottomRight
            maxSum = max(maxSum, currentSum)

    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
