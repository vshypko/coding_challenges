#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    binary = str(bin(n))[2:]
    bits = ['0'] * 32
    bits[32-len(binary):] = binary

    for i in range(len(bits)):
        bits[i] = '1' if bits[i] == '0' else '0'

    return(int(''.join(bits), 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
