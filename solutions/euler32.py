#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 32
# found online at projecteuler.net/problem=32
#
###############################################################################

from itertools import permutations
from math import pow

description = \
'We shall say that an n-digit number is pandigital if it makes use of\n' + \
'all the digits 1 to n exactly once; for example, the 5-digit number,\n' + \
'15234, is 1 through 5 pandigital.\n\n' + \
'The product 7254 is unusual, as the identity, 39  186 = 7254,\n' + \
'containing multiplicand, multiplier, and product is 1 through 9\n' + \
'pandigital.\n\n' + \
'Find the sum of all products whose multiplicand/multiplier/product\n' + \
'identity can be written as a 1 through 9 pandigital.\n\n' + \
'HINT: Some products can be obtained in more than one way so be sure\n' + \
'to only include it once in your sum.\n'

def display(self):
    return description

def solve(self):
    products = set()
    p = [1,2,3,4,5,6,7,8,9]
    for i in permutations(p):
	panDigit = int(filter(str.isdigit, repr(i)))
	for j, k in [(1,5), (2,5)]:
	    mult1 = int(str(panDigit)[:j])
	    mult2 = int(str(panDigit)[j:k])
	    product = int(str(panDigit)[k:])
	    if mult1*mult2 == product:
	        products.add(product)

    return sum(products)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
