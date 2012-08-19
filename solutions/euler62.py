#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 62
# found online at projecteuler.net/problem=62
# Solution by Timothy Reasa
#
###############################################################################

from itertools import permutations
from math import floor, log10

description = \
'The cube, 41063625 (345^3), can be permuted to produce two other cubes:\n' + \
'56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the\n' + \
'smallest cube which has exactly three permutations of its digits\n' + \
'which are also cube.\n\n'+ \
'Find the smallest cube for which exactly five permutations of its\n' + \
'digits are cube.\n'

def display(self):
    return description

def getSig(x):
    l = [0] * 10
    while x > 0:
	l[x%10] += 1
	x = x // 10
    return ' '.join(map(str, l))

def solve(self):

    permCache = {}
    i = 1
    while True:
	cube = i*i*i
 	sig = getSig(cube)
	previous = permCache.get(sig, (0,cube))

	# this happens to work, but there could be a sixth permutation
	#   that is also a cube
	if previous[0] == 4:		
	    return previous[1]
	permCache[sig] = (previous[0]+1, previous[1])
	i += 1



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
