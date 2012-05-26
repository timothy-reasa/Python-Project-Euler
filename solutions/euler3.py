#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 3
# found online at projecteuler.net/problem=3
# Solution by Timothy Reasa
#
###############################################################################

from math import sqrt

target = 600851475143
description = \
'The prime factors of 13195 are 5, 7, 13 and 29.\n\n' + \
'What is the largest prime factor of the number 600851475143 ?\n'

def display(self):
    return description

def isPrime(n):
    if n < 2:
	return False
    if n == 2:
	return True
    if not n & 1:
	return False
    for x in range(3, int(sqrt(n))+1, 2):
	if n % x == 0:
	    return False
    return True

def solve(self):
    n = target
    largestFactor = 2
    i = 2
    while n > 1:
        if n % i == 0 and isPrime(i):
	    n = n / i
	    largestFactor = i
        i += 1
    return largestFactor


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
