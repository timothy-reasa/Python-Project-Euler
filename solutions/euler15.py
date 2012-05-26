#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 15
# found online at projecteuler.net/problem=15
# Solution by Timothy Reasa
#
###############################################################################

from math import factorial

N = 20
description = \
'Starting in the top left corner of a 22 grid, there are 6 routes\n' + \
'(without backtracking) to the bottom right corner.\n\n' + \
'How many routes are there through a 2020 grid?\n\n' + \
'NOTE from Tim: backtracking refers to moving left or up.\n'

def display(self):
    return description

###############################################################################
#
# For an N x N grid, there are 2N required moves - N down and N right
#
# Think of it as choosing the times to go down.  Out of 2N possible options,
# we need to pick N.  The other N options are automatically right.  This is 
# equivalent to 2N choose N
#
###############################################################################

def solve(self):
    # calculate (2N choose N)
    return factorial(2*N) / factorial(N) / factorial(N)


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
