#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 48
# found online at projecteuler.net/problem=48
# Solution by Timothy Reasa
#
###############################################################################

description = \
'The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.\n\n' + \
'Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.\n'

def display(self):
    return description

def solve(self):
    total = 0
    for i in range(1, 1001):
	total += (i**i) % 10000000000
    return total % 10000000000

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
