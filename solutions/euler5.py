#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 5
# found online at projecteuler.net/problem=5
#
###############################################################################

from math import sqrt, floor, log, pow

limit = 20
description = \
'2520 is the smallest number that can be divided by each of the numbers\n' + \
'from 1 to 10 without any remainder.\n\n' + \
'What is the smallest positive number that is evenly divisible by all of\n' + \
'the numbers from 1 to 20?\n'

def display(self):
    return description


###############################################################################
#
# Naive solution by Timothy Reasa
#
# def isDiv(x):
#     for j in range(1,20)[::-1]:
# 	if x % j != 0:
# 	    return False
#     return True
# 
# def solve(self):
#     discovered = False
#     i = 1
#     while not isDiv(i):
#         i += 1
#     return i
#
###############################################################################

###############################################################################
#
# Key observation:
# This problem can be easily solved by computing the prime factorizations of
# the integeres from 1 to 20 and taking the product of the least common 
# multiples.  This is quick to do by hand.
#
###############################################################################

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
    product = 1
    smallLimit = int(sqrt(limit))
    for p in filter(isPrime, range(1,limit)):
	if p < smallLimit:	# could have multiple factors of p
            product *= int(pow(p, floor(log(limit, p))))
  	else:			# can only have one factor
	    product *= p
    return product


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
