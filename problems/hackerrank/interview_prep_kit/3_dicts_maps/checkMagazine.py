#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hashmap = {}
    for word in note:
        if word not in hashmap.keys():
            hashmap[word] = 0
        hashmap[word] += 1

    for word in magazine:
        if word in hashmap.keys():
            hashmap[word] -= 1

    for val in hashmap.values():
        if val > 0:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
