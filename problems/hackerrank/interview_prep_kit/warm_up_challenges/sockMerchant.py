#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    hashmap = {}
    ans = 0

    for i in ar:
        if i not in hashmap.keys():
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    print(hashmap)
    for k, v in hashmap.items():
        ans += (v // 2)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
