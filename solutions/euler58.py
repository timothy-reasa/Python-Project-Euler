#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 58
# found online at projecteuler.net/problem=58
# Solution by Timothy Reasa
#
###############################################################################

from __future__ import division
from math import floor, sqrt

limit = 1000000000

description = 'Starting with 1 and spiralling anticlockwise in the\n' + \
'following way, a square spiral with side length 7 is formed.\n\n' + \
'\t37 36 35 34 33 32 31\n' + \
'\t38 17 16 15 14 13 30\n' + \
'\t39 18  5  4  3 12 29\n' + \
'\t40 19  6  1  2 11 28\n' + \
'\t41 20  7  8  9 10 27\n' + \
'\t42 21 22 23 24 25 26\n' + \
'\t43 44 45 46 47 48 49\n\n' + \
'It is interesting to note that the odd squares lie along the bottom\n' + \
'right diagonal, but what is more interesting is that 8 out of the 13\n' + \
'numbers lying along both diagonals are prime; that is, a ratio of 8/13\n' + \
'= 62%.\n\n' + \
'If one complete new layer is wrapped around the spiral above, a square\n' + \
'spiral with side length 9 will be formed. If this process is continued,\n' + \
'what is the side length of the square spiral for which the ratio of\n' + \
'primes along both diagonals first falls below 10%?\n'

def display(self):
    return description

# performance testing showed significant advantage to trial division
# instead of a sieve approach.
def isPrime(n):
    # this application only has tests for odd numbers
    for x in range(3, int(sqrt(n))+1, 2):
	if n % x == 0:
	    return False
    return True

def solve(self):

    diagonals = 5
    primeDiagonals = 3
    s = 3

    # declaring variables here instead of in loop.  
    # minor improvement in speed
    d3 = 0
    d2 = 0
    d1 = 0

    while primeDiagonals / diagonals >= 0.1:
	s += 2

	# lower right diagonal is a square, and therefore never prime
	d3 = s*s-(s-1)
	d2 = d3-(s-1)
	d1 = d2-(s-1)
	
	if isPrime(d3):
	    primeDiagonals += 1
	if isPrime(d2):
	    primeDiagonals += 1
	if isPrime(d1):
	    primeDiagonals += 1

	diagonals += 4

    return s


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))
