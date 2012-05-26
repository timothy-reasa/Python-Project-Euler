#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 23
# found online at projecteuler.net/problem=23
#
###############################################################################

from itertools import permutations
from math import factorial

target = 1000000

description = \
'A permutation is an ordered arrangement of objects. For example, 3124\n' + \
'is one possible permutation of the digits 1, 2, 3 and 4. If all of the\n' + \
'permutations are listed numerically or alphabetically, we call it\n' + \
'lexicographic order. The lexicographic permutations of 0, 1 and 2 are:\n\n' +\
'\t012   021   102   120   201   210\n\n' + \
'What is the millionth lexicographic permutation of the digits 0, 1, 2,\n' + \
'3, 4, 5, 6, 7, 8 and 9?\n'

def display(self):
    return description


###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     #itertools.permutations return in lexographic order
#     return int(''.join(str(i) for i in \
# 	list(permutations([0,1,2,3,4,5,6,7,8,9]))[target-1]))
#
###############################################################################

###############################################################################
#
# Optimized solution by gcapell
#
# Key realization:
# The nth permutation can be determined algorithmically.  For example, for the
# first digit, we have 10! = 3628800 permutations available, meaning 362880
# permutations exist for each possible first digit.  The millionth permutation
# then uses the third digit in the list in the first position, i.e., 2.  The
# next digit is now looking for the 1000000 - 362880*3 permutation of the
# remaining 9 digits
#
###############################################################################

def nthPerm(s, n):
    if len(s)< 2:
	return s
    quot, n = divmod(n, factorial(len(s)-1))
    return s[quot] + nthPerm(s[:quot] + s[quot+1:], n)

def solve(self):
    return nthPerm('0123456789', target-1)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
