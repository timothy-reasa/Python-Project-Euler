#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 65
# found online at projecteuler.net/problem=65
# Solution by Timothy Reasa
#
###############################################################################

from __future__ import division
from math import ceil,floor,sqrt

limit = 10000

description = \
'\n'

def display(self):
    return description

###############################################################################
#
# Key realization:
# Let's try analyzing the given numerators to find a pattern.  We have
# 2, 3, 8, 11, 19, 87, 106, 193, 1264, 1457, ...
#
# It looks like the nth numerator is the (n-1)th numerator * a multiple 
# + (n-2)th numerator.  The multiple is 1,2,1, 1,4,1, 1,6,1, ...
#
# Lets see if this pattern produces the correct answer.
#
###############################################################################

def solve(self):

    i = 11
    current = 1457
    previous = 1264
    previous2 = 0
    multiple = 8

    while i <= 100:
	previous2 = previous
	previous = current

	if i%3 == 0:
	    current = previous*multiple + previous2
	    multiple += 2
 	else:
	    current = previous + previous2

	i += 1

    return sum(map(int, str(current)))



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
