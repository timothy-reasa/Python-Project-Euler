#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 188
# found online at projecteuler.net/problem=188
# Solution by Timothy Reasa
#
###############################################################################

import sys

base = 1777
exponent = 1855
description = \
'The hyperexponentiation or tetration of a number a by a positive\n' + \
'integer b, denoted by a^^b, is recursively defined by:\n\n' + \
'\ta^^1 = a,\n' + \
'\ta^^(k+1) = a^(a^^k).\n\n' + \
'Thus we have e.g. 3^^2 = 3^3 = 27, hence 3^^3 = 3^27 = 7625597484987\n' + \
'and 3^^4 is roughly 10^3.6383346400240996*10^12.\n\n' + \
'Find the last 8 digits of 1777^^1855.\n'

def display(self):
    return description

def tetration(base, exponent, modulus):
    if exponent == 1:
	return base % modulus
    return pow(base, tetration(base, exponent - 1, modulus), modulus)

def solve(self):
    if sys.getrecursionlimit() < exponent:
	sys.setrecursionlimit(exponent * 2)
    return tetration(base, exponent, 10**8)

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
