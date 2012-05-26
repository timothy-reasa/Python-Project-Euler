#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 7
# found online at projecteuler.net/problem=7
#
###############################################################################


from math import sqrt

description = \
'By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,\n' + \
'we can see that the 6th prime is 13.\n\n' + \
'What is the 10,001st prime number?\n'

def display(self):
    return description

###############################################################################
#
# This is pretty efficient.  If an upper bound on the prime was known, it 
# would be possible to use the Sieve of Eratosthenes.  To find larger primes,
# it might  be more efficient to store all discovered primes to use in the 
# trial divisions in the primality testing.
#
###############################################################################

def isPrime(n):
    if not n & 1:	# if n is even (and not 2)
	return False
    for x in range(3, int(sqrt(n))+1, 2):
	if n % x == 0:
	    return False
    return True

def solve(self):
    primes = 2
    current = 3
    while primes < 10001:
        current += 2
        if isPrime(current):
	    primes += 1

    return current


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
