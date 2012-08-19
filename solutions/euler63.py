#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 63
# found online at projecteuler.net/problem=63
# Solution by Timothy Reasa
#
###############################################################################

from __future__ import division
from math import ceil

description = \
'The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the\n' + \
'9-digit number, 134217728=8^9, is a ninth power.\n\n' + \
'How many n-digit positive integers exist which are also an nth power?\n'

def display(self):
    return description

###############################################################################
#
# Key realization:
# The problem can be restated as solving 10^(n-1) <= x^n < 10^n for x and n
#
# By solving the right portion of the above equation, we know that x < 10.
#
# For a lower bound, the left portion of the first equation can be 
# solved as follows:
# (n-1)/n <= log10(x)
# 10^((n-1)/n) <= x
# 
# As n trends toward infinity, the lower bound of x approaches 10.  Therefore
# this problem will terminate.
#
###############################################################################

def solve(self):

    count = 0
    lower = 0
    n = 1

    # iterate over all n's until the bounds overlap
    while lower <= 9:
	lower = int(ceil(10**((n-1)/n)))
	# add to the count for every x between the lower bound 
	#   and the upper bound (10)
 	count += 10-lower	
	n += 1

    return count



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
