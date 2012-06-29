#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 49
# found online at projecteuler.net/problem=49
# Solution by Timothy Reasa
#
###############################################################################

from math import floor, log10, sqrt
from itertools import permutations

limit = 10000
description = \
'The arithmetic sequence, 1487, 4817, 8147, in which each of the terms\n' + \
'increases by 3330, is unusual in two ways:\n\n' + \
'\t(i) each of the three terms are prime, and,\n' + \
'\t(ii) each of the 4-digit numbers are permutations of one another.\n\n' + \
'There are no arithmetic sequences made up of three 1-, 2-, or 3-digit\n' + \
'primes, exhibiting this property, but there is one other 4-digit\n' + \
'increasing sequence.\n\n' + \
'What 12-digit number do you form by concatenating the three terms\n' + \
'in this sequence?\n'

def display(self):
    return description

def getDigitCount(n):
    l = [0] * 10
    while n > 0:
	l[n % 10] += 1
	n /= 10
    return l

def arePermutations(a, b, c):
    A = getDigitCount(a)
    B = getDigitCount(b)
    C = getDigitCount(c)
    return A == B and B == C   

def solve(self):
    # create sieve
    sieveLimit = (limit-1) / 2
    sieve = [False] * sieveLimit
    crossLimit = int((floor(sqrt(limit)) - 1) / 2)
    for i in range(1, crossLimit):
	if not sieve[i]:
            j = 2*i*(i+1)
	    while j < sieveLimit:
	        sieve[j] = True
	        j += 2*i+1

    # Four digits primes must be odd.  Therefore, a, our starting number must
    # be odd and i, our increment, must be even.
    # Then a, a+i and a+2i are all odd.
    #
    # Point of ambiguity: did the problem description mean to set the 
    # increment to 3330?
    # 
    # If not, replace the below line with this: for i in range(2,limit/2,2):
    i = 3330
    for a in range(1, limit-2*i-1, 2):
	if a != 1487 or i != 3330:	# must not return the given example
	    a2 = a+i
	    a3 = a+2*i
	    if not sieve[(a-1)/2] and not sieve[(a2-1)/2] and not sieve[(a3-1)/2]:
		if arePermutations(a, a2, a3):
		    return str(a)+str(a2)+str(a3)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
