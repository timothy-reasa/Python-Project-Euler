#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 37
# found online at projecteuler.net/problem=37
# Solution by Timothy Reasa
#
###############################################################################

from math import floor, log10, sqrt

limit = 1000000		# guess the final prime occurs less than this
description = \
'The number 3797 has an interesting property. Being prime itself, it is\n' + \
'possible to continuously remove digits from left to right, and remain\n' + \
'prime at each stage: 3797, 797, 97, and 7. Similarly we can work from\n' + \
'right to left: 3797, 379, 37, and 3.\n\n' + \
'Find the sum of the only eleven primes that are both truncatable from\n' + \
'left to right and right to left.\n\n' + \
'NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.\n'

def display(self):
    return description

def isTruncatable(n, sieve):
    # check for right to left truncation
    temp = n / 10
    while temp > 0:
        if temp == 1:
	    return False
  	if temp != 2:
	    if not temp & 1 or sieve[(temp-1)/2]:
	    	return False
        temp /= 10
    # check for left to right truncation
    numDigits = int(log10(n))
    temp = n % 10**numDigits
    while temp > 0:
	if temp == 1:
	    return False
  	if temp != 2:
	    if not temp & 1 or sieve[(temp-1)/2]:
	    	return False
        numDigits = int(log10(temp))
	temp = temp % 10**numDigits
    return True

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

    truncs = set()
    i = 5	# 11 (index 5) is first truncatable prime
    while len(truncs) < 11:
	if not sieve[i] and isTruncatable(2*i+1, sieve):
	    truncs.add(2*i+1)
   	i += 1

    return sum(truncs)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
