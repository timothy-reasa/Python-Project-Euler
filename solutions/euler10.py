#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 10
# found online at projecteuler.net/problem=10
#
###############################################################################

from math import sqrt, floor

primeLimit = 2000000
description = \
'The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\n\n' + \
'Find the sum of all the primes below two million.\n'

def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def isPrime(n):
#     if not n & 1:	# if n is even
# 	return False
#     for x in range(3, int(sqrt(n))+1, 2):
# 	if n % x == 0:
# 	    return False
#     return True
#
# def solve(self):
#     total = 2
#     for i in range(3, 2000000)[::2]:
#         if isPrime(i):
# 	    total += i
#
#     return total
#
###############################################################################

###############################################################################
#
# Optimized code based on pseudocode from daniel.is.fischer
#
# Key observation:
# The sieve of Eratosthenes is applicable here.
#
# Also, using range for the inner loop of createSieve creates a giant list,
# which towers over the rest of the algorithm in run time.  Hence, the while
# loop
#
###############################################################################

def createSieve(limit):
    sieveLimit = (limit-1) / 2
    sieve = [False] * sieveLimit
    crossLimit = int((floor(sqrt(limit)) - 1) / 2)
    for i in range(1, crossLimit):
	if not sieve[i]:
            j = 2*i*(i+1)
	    while j < sieveLimit:
	        sieve[j] = True
	        j += 2*i+1
    return sieve

def solve(self):
    sieve = createSieve(primeLimit)    
    primeSum = 2
    for i in range(1, int((primeLimit-1) / 2)):
	if not sieve[i]:
	    primeSum += 2*i+1
    return primeSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
