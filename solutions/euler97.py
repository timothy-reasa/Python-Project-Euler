#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 97
# found online at projecteuler.net/problem=97
# Solution by Timothy Reasa
#
###############################################################################

description = \
'The first known prime found to exceed one million digits was discovered\n' + \
'in 1999, and is a Mersenne prime of the form 2^6972593 - 1; it contains\n' + \
'exactly 2,098,960 digits. Subsequently other Mersenne primes, of the\n' + \
'form 2^p -1, have been found which contain more digits.\n\n' + \
'However, in 2004 there was found a massive non-Mersenne prime which\n' + \
'contains 2,357,207 digits: 28433 x 2^7830457 + 1.\n\n' + \
'Find the last ten digits of this prime number.\n'

def display(self):
    return description

def solve(self):
    return (28433 * pow(2, 7830457, 10**10) + 1) % 10**10

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
