import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = raw_input()
    cntr = collections.Counter(s)
    y = collections.OrderedDict(cntr.most_common())
    z = list(y.items())
    q = collections.OrderedDict(z[1:3])
    p = sorted(q.keys(), key=lambda x: x.lower())
    print(str(z[0][0])+" "+str(z[0][1]))

    for i in p:
        values=q[i]
        print(i + ' ' + str(values))
  
