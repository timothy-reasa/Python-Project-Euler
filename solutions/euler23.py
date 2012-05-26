#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 23
# found online at projecteuler.net/problem=23
#
###############################################################################

from math import floor, sqrt

hardLimit = 28123

description = \
'A perfect number is a number for which the sum of its proper divisors\n' + \
'is exactly equal to the number. For example, the sum of the proper\n' + \
'divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28\n' + \
'is a perfect number.\n\n' + \
'A number n is called deficient if the sum of its proper divisors is\n' + \
'less than n and it is called abundant if this sum exceeds n.\n\n' + \
'As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the\n' + \
'smallest number that can be written as the sum of two abundant numbers\n' + \
'is 24. By mathematical analysis, it can be shown that all integers\n' + \
'greater than 28123 can be written as the sum of two abundant numbers.\n' + \
'However, this upper limit cannot be reduced any further by analysis \n' + \
'even though it is known that the greatest number that cannot be \n' + \
'expressed as the sum of two abundant numbers is less than this limit.\n\n' + \
'Find the sum of all the positive integers which cannot be written as\n' + \
'the sum of two abundant numbers.\n'

def display(self):
    return description


###############################################################################
#
# Optimized solution by MarkD349
#
# Key realization:
# Calculating the divisors of large numbers is most efficiently done using
# a sieve.  As divisors are being added to factor sets, the abundant numbers
# are generated, and sums are checked on the smallest abundant set possible.
#
###############################################################################

def noSum(abundants, n):
    for a in abundants:
        if n - a in abundants:
            return False
    return True

def solve(self):
    factorLim = int(sqrt(hardLimit)) + 1
    factors = dict([(x, set([1])) for x in range(1, hardLimit)])

    total = 0
    abn = set()

    for n in range(1, hardLimit):
        if n < factorLim:
	    # computing divisors with a sieve
            for b in range(n, hardLimit, n):
                factors[b].add(n)
                factors[b].add(int(b / n))
        if sum(factors[n]) > 2 * n:	# if abundant
            abn.add(n)
        if noSum(abn, n):	
            total += n

    return total


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
