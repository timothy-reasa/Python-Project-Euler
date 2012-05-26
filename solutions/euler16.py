#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 16
# found online at projecteuler.net/problem=16
# Solution by Timothy Reasa
#
###############################################################################

from math import pow

power = 1000
description = \
'2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.\n\n' + \
'What is the sum of the digits of the number 2^1000?\n'

def display(self):
    return description

def solve(self):
    total = 0
    for i in str(int(pow(2, power))):
        total += int(i)

    return total


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
