#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 75
# found online at projecteuler.net/problem=75
#
###############################################################################

from math import sqrt
from fractions import gcd

limit = 1500000
description = \
'It turns out that 12 cm is the smallest length of wire that can be bent\n' + \
'to form an integer sided right angle triangle in exactly one way, but\n' + \
'there are many more examples.\n\n' + \
'\t12 cm: (3,4,5)\n' + \
'\t24 cm: (6,8,10)\n' + \
'\t30 cm: (5,12,13)\n' + \
'\t36 cm: (9,12,15)\n' + \
'\t40 cm: (8,15,17)\n' + \
'\t48 cm: (12,16,20)\n\n' + \
'In contrast, some lengths of wire, like 20 cm, cannot be bent to form\n' + \
'an integer sided right angle triangle, and other lengths allow more than\n' + \
'one solution to be found; for example, using 120 cm it is possible to\n' + \
'form exactly three different integer sided right angle triangles.\n\n' + \
'\t120 cm: (30,40,50), (20,48,52), (24,45,51)\n\n' + \
'Given that L is the length of the wire, for how many values of\n' + \
'L <= 1,500,000 can exactly one integer sided right angle triangle be\n' + \
'formed?\n\n' + \
'Note: This problem has been changed recently, please check that you are\n' + \
'using the right parameters.\n'

def display(self):
    return description

###############################################################################
#
# Optimized solution by Mike at blog.dreamshire.com
#
# Key realization:
# Iterate over lengths of non-hypotenuse sides.  If side lengths aren't
# co-prime, we've already counted that pythagorean triple.
#
###############################################################################

def solve(self):
    tx = [0] * limit
    for i in range(1, int(sqrt(limit)), 2):
	for j in range(2, int(sqrt(limit))-i, 2):
	    if gcd(i, j) == 1:
		perimeter = abs(j*j - i*i) + 2*i*j + i*i + j*j
	        for s in range(perimeter, limit, perimeter):
		    tx[s] += 1

    return tx.count(1)

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
