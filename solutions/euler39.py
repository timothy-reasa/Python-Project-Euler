#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 38
# found online at projecteuler.net/problem=38
# Solution by Timothy Reasa
#
###############################################################################

limit = 1000
description = \
'If p is the perimeter of a right angle triangle with integral length\n' + \
'sides, {a,b,c}, there are exactly three solutions for p = 120.\n\n' + \
'\t{20,48,52}, {24,45,51}, {30,40,50}\n\n' + \
'For which value of p  1000, is the number of solutions maximised?\n'

def display(self):
    return description

def solve(self):
    maxSoln = 0
    maxP = 0
    for p in range(limit+1):
	numSoln = 0
        for a in range(1, p-1):
	    for b in range(1, p-a-1):
		c = p - a - b
		if c*c == a*a + b*b:
		    numSoln += 1
	if numSoln > maxSoln:
	    maxP = p
	    maxSoln = numSoln
 
    return maxP


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
