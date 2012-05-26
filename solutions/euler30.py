#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 30
# found online at projecteuler.net/problem=30
# Solution by Timothy Reasa
#
###############################################################################

from math import pow

upperLimit = 325512	# intersection of y = 9^5 * log10(x) and y = x
description = \
'Surprisingly there are only three numbers that can be written as\n' + \
'the sum of fourth powers of their digits:\n\n' + \
'\t1634 = 14 + 64 + 34 + 44\n' + \
'\t8208 = 84 + 24 + 04 + 84\n' + \
'\t9474 = 94 + 44 + 74 + 44\n\n' + \
'As 1 = 14 is not a sum it is not included.\n\n' + \
'The sum of these numbers is 1634 + 8208 + 9474 = 19316.\n\n' + \
'Find the sum of all the numbers that can be written as the sum of\n' + \
'fifth powers of their digits.\n'

def display(self):
    return description

def solve(self):
    # only ten factorials needed.
    pows = [0, 1, int(pow(2, 5)), int(pow(3, 5)), int(pow(4, 5)), \
	int(pow(5, 5)), int(pow(6, 5)), int(pow(7, 5)), int(pow(8, 5)), \
	int(pow(9, 5))]

    finalSum = 0
    for i in range (5, upperLimit):
	partialSum = 0
	temp = i
	while temp != 0:
	    partialSum += pows[temp % 10]
	    temp = temp / 10
        if partialSum == i:
            finalSum += i

    return finalSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
