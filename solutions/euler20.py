#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 20
# found online at projecteuler.net/problem=20
# Solution by Timothy Reasa
#
###############################################################################

from math import factorial

target = 100

description = \
'n! means n x (n  1) x ... x 3 x 2 x 1\n\n' + \
'For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of\n' + \
'the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.\n\n' + \
'Find the sum of the digits in the number 100!\n'

def display(self):
    return description
    

def solve(self):
    facto = str(factorial(target))
    sumDigits = 0
    for c in facto:
	sumDigits += int(c)
    return sumDigits
 


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
