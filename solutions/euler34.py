#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 34
# found online at projecteuler.net/problem=34
# Solution by Timothy Reasa
#
###############################################################################

from math import factorial

upperLimit = 2500000	# Upper bound provided by pudquick
			# Intersection of y=x and y=9!*log(x) is 2,309,171
description = \
'145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.\n\n' + \
'Find the sum of all numbers which are equal to the sum of the\n' + \
'factorial of their digits.\n\n' + \
'Note: as 1! = 1 and 2! = 2 are not sums they are not included.\n'

def display(self):
    return description

def solve(self):
    # only ten factorials needed.
    fact = [factorial(0), factorial(1), factorial(2), \
	factorial(3), factorial(4), factorial(5), \
  	factorial(6), factorial(7), factorial(8), \
	factorial(9)]

    finalSum = 0
    for i in range (3, upperLimit):
        partialSum = 0
	temp = i
	while temp != 0:
	    partialSum += fact[temp % 10]
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
