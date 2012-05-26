#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 9
# found online at projecteuler.net/problem=9
#
###############################################################################

from math import sqrt

perimeter = 1000
description = \
'A Pythagorean triplet is a set of three natural numbers, a < b < c,\n' + \
'for which,\n\n' + \
'\ta^2 + b^2 = c^2\n\n' + \
'For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.\n\n' + \
'There exists exactly one Pythagorean triplet for which a + b + c = 1000.\n' +\
'Find the product abc.\n'

def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     a = 1
#     b = 1
#     c = 1
#
#     while True:
#         b = a+1
#         while True:
# 	    c = sqrt(a*a + b*b)
#             if a+b+c == 1000:
#          	return a*b*int(c)
# 	    if a+b+c > 1000:
# 	        break
# 	    b += 1
#         a += 1
#
###############################################################################

###############################################################################
#
# Optimized solution based on mathematics from Pier
#
# Key observation:
# Pythagorean triplets are in the form a = 2mn, b = m^2 - n^2, c = m^2 + n^2
# The constraint is a + b + c = 1000
#
# Therefore 2mn + (m^2 - n^2) + (m^2 + n^2) = 1000
#	2mn + 2m^2 = 1000
#	2m(m+n) = 1000
#	m(m+n) = 500
#
# Solve for m > n.  Find a, b, c
#
###############################################################################

def findTriplet(x):
    x /= 2
    for m in range(1, x):
	n = x / m - m
	if m > n and int(m*(m+n)) == x:
	    return (2*m*n, m*m - n*n, m*m + n*n)
    return None

def solve(self):
    trip = findTriplet(perimeter)
    return trip[0] * trip[1] * trip[2]


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
    
