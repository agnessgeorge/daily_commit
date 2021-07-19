import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_split = s.split()
    caps = []
    for t in s_split:
        if t.isdigit():
            caps.append(t)
        else:
            u = t.capitalize()
            caps.append(u)
         
    new_s = ' '.join(caps)
    return new_s


if __name__ == '__main__':

    s = raw_input()

    result = solve(s)

    print(result)
