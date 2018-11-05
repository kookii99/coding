#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def solve( names ):
    m = set()
    p = {}
    results = []
    for name in names:
        if name in p:
            p[ name ] += 1
            results.append( name + ' ' + str( p[ name ] ) )
            continue

        p[ name ] = 1

        pre = ''
        found = False
        for c in name:
            pre += c
            if pre not in m:
                if not found:
                    results.append( pre )
                    found = True
            m.add( pre )
        if not found:
            results.append( pre )

    return results

if __name__ == '__main__':
    def input():
        f = open( '_input.log' )
        return tuple( line.strip() for line in f )

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    names = []

    for _ in range(n):
        names_item = input()
        names.append(names_item)

    res = solve(names)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
