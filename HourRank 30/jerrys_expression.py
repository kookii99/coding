#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING expression as parameter.
#
def solve_recursively( expression ):
    def parse():
        nonlocal index, ki
        char = expression[ index ]
        if char == '?':
            ki += 1
            return [ ki - 1, ], []
        elif char == '+':
            index += 1
            posiLeft, negaLeft = parse()
            index += 1
            posiRight, negaRight = parse()
            return posiLeft + posiRight, negaLeft + negaRight
        elif char == '-':
            index += 1
            posiLeft, negaLeft = parse()
            index += 1
            posiRight, negaRight = parse()
            return posiLeft + negaRight, negaLeft + posiRight
    index = 0
    ki = 0
    posi, nega = parse()

    posiSize = len( posi )
    negaSize = len( nega )
    result = [ 1, ] * ki
    diff = posiSize - negaSize
    if diff > 0:
        remainder = diff % negaSize
        quotient = diff // negaSize
        for i in range( negaSize ):
            index = nega[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient
    else:
        remainder = -diff % posiSize
        quotient = -diff // posiSize
        for i in range( posiSize ):
            index = posi[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient

    return result


def solve_iterative( expression ):
    ki = 0
    stack = []
    results = []
    for char in expression:
        if char == '+':
            stack.append( 1 )
        elif char == '-':
            stack.append( 3 )
        elif char == '?':
            results.append( ( [ ki, ], [] ) )
            ki += 1

            while stack:
                last = stack.pop()
                if last == 1 or last == 3:
                    stack.append( last + 1 )
                    break
                elif last == 2:
                    posiRight, negaRight = results.pop()
                    posiLeft, negaLeft = results.pop()
                    results.append( ( posiLeft + posiRight, negaLeft + negaRight ) )
                elif last == 4:
                    posiRight, negaRight = results.pop()
                    posiLeft, negaLeft = results.pop()
                    results.append( ( posiLeft + negaRight, negaLeft + posiRight ) )

    posi, nega = results.pop()

    posiSize = len( posi )
    negaSize = len( nega )
    result = [ 1, ] * ki
    diff = posiSize - negaSize
    if diff > 0:
        remainder = diff % negaSize
        quotient = diff // negaSize
        for i in range( negaSize ):
            index = nega[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient
    else:
        remainder = -diff % posiSize
        quotient = -diff // posiSize
        for i in range( posiSize ):
            index = posi[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient

    return result


def solve( expression ):
    ki = 0
    stack = []
    posi = []
    nega = []
    sign = 1
    for char in expression:
        if char == '+':
            stack.append( ( 1, sign ) )
        elif char == '-':
            stack.append( ( 3, sign ) )
        elif char == '?':
            if sign > 0:
                posi.append( ki )
            else:
                nega.append( ki )
            ki += 1

            while stack:
                last, sign = stack.pop()
                if last == 1 or last == 3:
                    sign = sign if last == 1 else -sign
                    stack.append( ( last + 1, sign ) )
                    break

    posiSize = len( posi )
    negaSize = len( nega )
    result = [ 1, ] * ki
    diff = posiSize - negaSize
    if diff > 0:
        remainder = diff % negaSize
        quotient = diff // negaSize
        for i in range( negaSize ):
            index = nega[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient
    else:
        remainder = -diff % posiSize
        quotient = -diff // posiSize
        for i in range( posiSize ):
            index = posi[ i ]
            if i < remainder:
                result[ index ] += quotient + 1
            else:
                result[ index ] += quotient

    return result


if __name__ == '__main__':
    def input():
        f = open( '_input.log' )
        return tuple( line.strip() for line in f )


    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    expression = input()

    res = solve(expression[0])

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
