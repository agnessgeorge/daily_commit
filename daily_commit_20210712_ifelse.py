#!/bin/python3
# Given an integer,n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys

def weird_test(m):
    if m % 2 != 0:
        print("Weird")
    elif m % 2 == 0 and m in range(2,6):
        print("Not Weird")
    elif m % 2 == 0 and m in range(6,21):
        print("Weird")
    elif m % 2 == 0 and m > 20:
        print("Not Weird")
    

if __name__ == '__main__':
    n = int(input().strip())

weird_test(n)