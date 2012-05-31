#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 35
# found online at projecteuler.net/problem=35
#
###############################################################################

from math import sqrt, floor, log10

primeLimit = 1000000
description = \
'The number, 197, is called a circular prime because all rotations of\n' + \
'the digits: 197, 971, and 719, are themselves prime.\n\n' + \
'There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,\n' + \
'37, 71, 73, 79, and 97.\n\n' + \
'How many circular primes are there below one million?\n'

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

numDigits = lambda n: int(log10(n))+1

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

def getCirculars(prime):
    circulars = []
    temp = prime
    for i in range(numDigits(temp)-1):	
        nextCircular, j = divmod(temp, 10)
        temp = j * pow(10, numDigits(temp)-1) + nextCircular
        circulars.append(temp)
    return circulars

def isCircularPrime(prime, seive):
    circulars = getCirculars(prime)
    for c in circulars:
	if not c & 1:	# circular is eve
	    return False
    for c in circulars:
	if seive[(c-1)/2]:
	    return False
    return True

def solve(self):
    sieve = createSieve(primeLimit)    
    circCount = 1	# count 2 as well
    for i in range(1, int((primeLimit-1) / 2)):
	if not sieve[i] and isCircularPrime(2*i+1, sieve):
	    circCount += 1

    return circCount


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
