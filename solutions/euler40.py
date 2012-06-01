#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 40
# found online at projecteuler.net/problem=40
# Solution by Timothy Reasa
#
###############################################################################

from math import pow

description = \
'An irrational decimal fraction is created by concatenating the positive\n' + \
'integers:\n\n' + \
'\t0.123456789101112131415161718192021...\n\n' + \
'It can be seen that the 12th digit of the fractional part is 1.\n\n' + \
'If d_n represents the nth digit of the fractional part, find the value\n' + \
'of the following expression.\n\n' + \
'\td_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000\n'

def display(self):
    return description


def solve(self):
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    integer = 1
    digitCounter = 0
    targetIndex = 0

    while targetIndex < len(targets):
	for digit in str(integer):
	    digitCounter += 1
	    if digitCounter == targets[targetIndex]:
		product *= int(digit)
		targetIndex += 1
		if targetIndex == len(targets):
		    break
	integer += 1

    return product

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
