#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets( arr, r ):
    # triplet 들을 찾기 이전에, 조건을 만족하는 tuple 들을 찾아 테이블에 기록해 둔 후,
    # index 별 tuple 의 쌍의 갯수를 찾으면 결국 triplet 의 갯수가 된다.

    nums = {}
    for i, n in enumerate( arr ):
        if n in nums:
            nums[ n ].append( i )
        else:
            nums[ n ] = [ i, ]

    tuplesTable = {}
    for n in sorted( nums ):
        n2 = n * r
        tuplesTable[ n ] = tuples = {}
        c2 = nums.get( n2 )
        if c2:
            c2Len = len( c2 )
            c2IndexIndex = 0
            for c1Index in nums[ n ]:
                for c2IndexIndex in range( c2IndexIndex, c2Len ):
                    c2Index = c2[ c2IndexIndex ]
                    if c2Index > c1Index:
                        break
                else:
                    c2IndexIndex = c2Len
                tuples[ c1Index ] = c2Len - c2IndexIndex

    for tuples in tuplesTable.values():
        count = 0
        for index in tuple( sorted( tuples.keys(), reverse = True ) ):
            count += tuples[ index ]
            tuples[ index ] = count

    count = 0
    for n in sorted( nums ):
        n2 = n * r
        c2 = nums.get( n2 )
        if c2:
            c2Len = len( c2 )
            c2IndexIndex = 0
            for c1Index in nums[ n ]:
                for c2IndexIndex in range( c2IndexIndex, c2Len ):
                    c2Index = c2[ c2IndexIndex ]
                    if c2Index > c1Index:
                        count += tuplesTable[ n2 ].get( c2Index, 0 )
                        break

    return count


if __name__ == '__main__':
    f = open( '_input.log' )

    def input():
        res = f.readline()
        return res

    fptr = sys.stdout
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
