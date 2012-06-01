#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 39
# found online at projecteuler.net/problem=39
#
###############################################################################

from __future__ import division

limit = 1000
description = \
'If p is the perimeter of a right angle triangle with integral length\n' + \
'sides, {a,b,c}, there are exactly three solutions for p = 120.\n\n' + \
'\t{20,48,52}, {24,45,51}, {30,40,50}\n\n' + \
'For which value of p  1000, is the number of solutions maximised?\n'

def display(self):
    return description


###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     maxSoln = 0
#     maxP = 0
#     for p in range(limit+1):
# 	numSoln = 0
#         for a in range(1, p-1):
# 	    for b in range(1, p-a-1):
# 		c = p - a - b
# 		if c*c == a*a + b*b:
# 		    numSoln += 1
# 	if numSoln > maxSoln:
# 	    maxP = p
# 	    maxSoln = numSoln
#  
#     return maxP
# 
###############################################################################

###############################################################################
#
# Optimized solution based on mathematics observed by rayfil
#
# Key realization:
# Because c^2 = a^2 + b^2, P = a + b + c will always be even.
#
# Because c = P - b - a, we have a^2 + b^2 = P^2+a^2+b^2 - 2Pa - 2Pb + 2ab.
# We can solve this for b = P(P-2a) / 2(P-a)
#
###############################################################################

def solve(self):
    maxSoln = 0
    maxP = 0
    for p in range(2, limit, 2):
	counter = 0
        for a in range(limit):
	    b = p*(p-2*a) / (2*(p-a))
	    if a >= b:
		break
	    elif b == int(b):
		counter += 1
        if counter > maxSoln:
	    maxSoln = counter
	    maxP = p

    return maxP

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
