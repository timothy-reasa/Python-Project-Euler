#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 51
# found online at projecteuler.net/problem=51
# Solution by Timothy Reasa
#
###############################################################################

from math import floor, sqrt
import sys

limit = 1000000

description = \
'By replacing the 1st digit of *3, it turns out that six of the nine\n' + \
'possible values: 13, 23, 43, 53, 73, and 83, are all prime.\n\n' + \
'By replacing the 3rd and 4th digits of 56**3 with the same digit, this\n' + \
'5-digit number is the first example having seven primes among the ten\n' + \
'generated numbers, yielding the family: 56003, 56113, 56333, 56443,\n' + \
'56663, 56773, and 56993. Consequently 56003, being the first member of\n' + \
'this family, is the smallest prime with this property.\n\n' + \
'Find the smallest prime which, by replacing part of the number (not\n' + \
'necessarily adjacent digits) with the same digit, is part of an eight\n' + \
'prime value family.\n'

def display(self):
    return description  
	
def getDigitCount(n):
    l = [0] * 10
    while n > 0:
	l[n % 10] += 1
	n /= 10
    return l

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

    # look for prime families
    for i in range(1, sieveLimit):
	if not sieve[i]:
	    p = 2*i+1
	    l = getDigitCount(p)

	    # in order for there to be 8 primes in the family, 
	    #   at least one needs to have repeatings 0's, 1's, or 2's
	    for j in range(3):	
		if l[j] == 3:
		    s = str(p).replace(str(j), ".")
		    familySize = 1

		    # find other primes in the family
		    for k in range(j+1, 10):
			candidate = int(s.replace(".", str(k)))
			if not sieve[(candidate-1)/2]:
			    familySize += 1
		    if familySize == 8:
			return p
	


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
