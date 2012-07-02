#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 57
# found online at projecteuler.net/problem=57
# Solution by Timothy Reasa
#
###############################################################################

from math import log10

limit = 1000
description = \
'It is possible to show that the square root of two can be expressed\n' + \
'as an infinite continued fraction.\n\n' + \
'\tSqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...\n\n' + \
'By expanding this for the first four iterations, we get:\n\n' + \
'\t1 + 1/2 = 3/2 = 1.5\n' + \
'\t1 + 1/(2 + 1/2) = 7/5 = 1.4\n' + \
'\t1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...\n' + \
'\t1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...\n\n' + \
'The next three expansions are 99/70, 239/169, and 577/408, but the\n' + \
'eighth expansion, 1393/985, is the first example where the number of\n' + \
'digits in the numerator exceeds the number of digits in the\n' + \
'denominator.\n\n' + \
'In the first one-thousand expansions, how many fractions contain a\n' + \
'numerator with more digits than denominator?\n'

def display(self):
    return description

###############################################################################
#
# Key observations:
# We can derive recursive formulas for the numerator and denominator
# N_i = N_i-1 + 2*D_i-1
# D_i = N_i-1 + D_i-1
#
###############################################################################	

def solve(self):
    count = 0
    n = 577
    d = 408
    for i in range(7,limit+1):
	n = n + 2*d
	d = n - d
	if int(log10(n)) > int(log10(d)):
	    count += 1

    return count

	

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
