#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 41
# found online at projecteuler.net/problem=41
# Solution by Timothy Reasa
#
###############################################################################

from math import sqrt
from itertools import permutations

description = \
'We shall say that an n-digit number is pandigital if it makes use\n' + \
'of all the digits 1 to n exactly once. For example, 2143 is a 4-digit\n' + \
'pandigital and is also prime.\n\n' + \
'What is the largest n-digit pandigital prime that exists?\n'

def display(self):
    return description


def isPrime(n):
#    not needed (only used on pandigital numbers)
#    if n < 2:
#	return False
#    if n == 2:
#	return True
    if not n & 1:
	return False
    for x in range(3, int(sqrt(n))+1, 2):
	if n % x == 0:
	    return False
    return True

def solve(self):
    maxP = 0
    i = 1
    # 8 and 9 digit pandigital numbers are divisible by 3 (not prime)
    # assume one 7 digit number is both pandigital and prime
    for i in permutations([1,2,3,4,5,6,7]):
        j = int(filter(str.isdigit, repr(i)))
        if isPrime(j):
	    maxP = j	# permuations generated in increasing order

    return maxP


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
