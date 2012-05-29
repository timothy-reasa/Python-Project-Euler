#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 33
# found online at projecteuler.net/problem=33
# Solution by Timothy Reasa
#
###############################################################################

from math import pow
from fractions import gcd

description = \
'The fraction 49/98 is a curious fraction, as an inexperienced\n' + \
'mathematician in attempting to simplify it may incorrectly believe that\n' + \
'49/98 = 4/8, which is correct, is obtained by cancelling the 9s.\n\n' + \
'We shall consider fractions like, 30/50 = 3/5, to be trivial examples.\n\n' +\
'There are exactly four non-trivial examples of this type of fraction,\n' + \
'less than one in value, and containing two digits in the numerator and\n' + \
'denominator.\n\n' + \
'If the product of these four fractions is given in its lowest common\n' + \
'terms, find the value of the denominator.\n'

def display(self):
    return description

def solve(self):
    fractions = []
    for j in range(10, 100):
	for i in range(10, j-1):
	    k, l = divmod(i, 10)
	    m, n = divmod(j, 10)
	    if l != 0 or n != 0:
	        if k == n and l*j == m*i:
		    fractions.append((l, m))
	        if k == m and l*j == n*i:
		    fractions.append((l, n))
	        if l == m and k*j == n*i:		
		    fractions.append((k, n))
	        if l == n and k*j == m*i:
		    fractions.append((k, m))

    num = 1
    den = 1
    for f in fractions:
	num *= f[0]
	den *= f[1]
    
    d = gcd(num, den)
    return den / d


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
