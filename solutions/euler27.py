#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 27
# found online at projecteuler.net/problem=27
# Solution by Timothy Reasa
#
###############################################################################

from math import sqrt

description = \
'Euler published the remarkable quadratic formula:\n\n' + \
'\tn^2 + n + 41\n\n' + \
'It turns out that the formula will produce 40 primes for the\n' + \
'consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41\n' + \
'= 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,\n' + \
'41^2 + 41 + 41 is clearly divisible by 41.\n\n' + \
'Using computers, the incredible formula n^2 - 79n + 1601 was discovered,\n' +\
'which produces 80 primes for the consecutive values n = 0 to 79. The\n' + \
'product of the coefficients, -79 and 1601, is -126479.\n\n' + \
'Considering quadratics of the form:\n\n' + \
'\tn^2 + an + b, where |a| < 1000 and |b| < 1000\n' + \
'\t\twhere |n| is the modulus/absolute value of n\n\n' + \
'Find the product of the coefficients, a and b, for the quadratic\n' + \
'expression that produces the maximum number of primes for consecutive\n' + \
'values of n, starting with n = 0.\n'

def display(self):
    return description

def isPrime(n):
    if n < 2:
	return False
    if n == 2:
	return True
    if not n & 1:	# if n is even (and not 2)
	return False
    for x in range(3, int(sqrt(n))+1, 2):
	if n % x == 0:
	    return False
    return True

def solve(self):
    maxSequence = 0
    maxCoefs = (0, 0)
    # for n=0, quadratic = b, so b must be a positive prime
    # for n=1, quadratic = 1+a+b, so a > -(b+1)
    #     therefore, a is odd and negative and b ranges from -(a+1) to 1000
    for a in range(-999, 0, 2):
	for b in range(-a, 1000, 2):
	    n = 1
	    while isPrime(n*(n+a) + b):
		n += 1
	    if n > maxSequence:
		maxSequence = n
		maxCoefs = (a, b)
	
    return maxCoefs[0] * maxCoefs[1]


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))
