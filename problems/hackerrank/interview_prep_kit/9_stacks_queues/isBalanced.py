#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if not s:
        return "NO"

    stack = list()
    opening_brackets = ['(', '[', '{']

    for c in s:
        if c in opening_brackets:
            stack.append(c)
        else:
            if not stack:
                return "NO"
            temp = stack.pop()
            if not ((c == ')' and temp == '(')
                or (c == ']' and temp == '[')
                or (c == '}' and temp == '{')):
                return "NO"

    return "YES" if not stack else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
