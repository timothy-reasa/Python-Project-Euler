#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 1
# found online at projecteuler.net/problem=1
#
###############################################################################

ceiling = 999
description = \
'If we list all the natural numbers below 10 that are multiples of 3 or 5,\n' \
 + 'we get 3, 5, 6 and 9. The sum of these multiples is 23.\n\n' \
 + 'Find the sum of all the multiples of 3 or 5 below 1000.\n'

def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve: 
#     sum = 0
#     for i in range(1, 1000):
#         if i % 3 == 0 or i % 5 == 0:
# 	    sum += i
# 
#     return sum
#
###############################################################################

###############################################################################
#
# Optimized solution based on pseudocode from hk
#
# Key observation:
# The sum of all numbers divisible by 3 or 5 is the sum of numbers divisible
# by 3 plus the sum of numbers divisible by 5 minus the sum of numbers
# divisible by 15.
#
###############################################################################
def sumDivisibleBy(n):
    m = ceiling // n	# integer division
    return int(n * (m * (m+1) * 0.5))

def solve(self):
    return sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))

