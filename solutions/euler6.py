#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 6
# found online at projecteuler.net/problem=6
#
###############################################################################

limit = 100
description = \
'The sum of the squares of the first ten natural numbers is\n\n' + \
'\t1^2 + 2^2 + ... + 10^2 = 385\n\n' + \
'The square of the sum of the first ten natural numbers is\n\n' + \
'\t(1 + 2 + ... + 10)^2 = 55^2 = 3025\n\n' + \
'Hence the difference between the sum of the squares of the first ten\n' + \
'natural numbers and the square of the sum is 3025 - 385 = 2640.\n\n' + \
'Find the difference between the sum of the squares of the first one\n' + \
'hundred natural numbers and the square of the sum.\n'


def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     sumSquare = 0
#     squareSum = 0
#     for i in range(limit+1):
# 	sumSquare += i*i
# 	squareSum += i
#     squareSum *= squareSum
#     return squareSum - sumSquare
#
###############################################################################

###############################################################################
# 
# Key observation:
# The sum of all numbers from 1 to N is N*(N+1)/2
# The sum of the squares of all numbers from 1 to N is N*(N+1)*(2N+1)/6
# This solution can be computed in O(1) time
#
###############################################################################

def solve(self):
    littleSum = limit*(limit+1) / 2
    sqSum = littleSum * littleSum
    sumSq = limit*(limit+1)*(2*limit+1) / 6

    return sqSum - sumSq


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
