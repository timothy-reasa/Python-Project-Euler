#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 53
# found online at projecteuler.net/problem=53
# Solution by Timothy Reasa
#
###############################################################################

from math import factorial

facts = [factorial(x) for x in range(101)]
description = \
'There are exactly ten ways of selecting three from five, 12345:\n\n' + \
'\t123, 124, 125, 134, 135, 145, 234, 235, 245, and 345\n\n' + \
'In combinatorics, we use the notation, 5C3 = 10.\n\n' + \
'In general,\n\n' + \
'\tnCr = n! / r!(n-r)!, where r <= n, n! = nx(n-1)...3x2x1, and 0! = 1.\n\n' + \
'It is not until n = 23, that a value exceeds one-million: \n' + \
'23C10 = 1144066.\n\n' + \
'How many, not necessarily distinct, values of nCr, for 1 <= n <= 100,\n' + \
'are greater than one-million?\n'

def display(self):
    return description

def numCombinations(n, r):
    return facts[n] / facts[r] / facts[n-r]

def solve(self):
    count = 0
    for n in range(1, 101):
	for r in range(1, n):
	    if numCombinations(n,r) > 1000000:
		count += 1

    return count

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
