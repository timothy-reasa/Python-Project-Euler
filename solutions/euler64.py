#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 64
# found online at projecteuler.net/problem=64
# Solution by Timothy Reasa
#
###############################################################################

from __future__ import division
from math import ceil,floor,sqrt

limit = 10000

description = \
'All square roots are periodic when written as continued fractions...For\n' + \
'conciseness, we use the notation 23 = [4;(1,3,1,8)], to indicate that\n' + \
'the block (1,3,1,8) repeats indefinitely.\n\n' + \
'The first ten continued fraction representations of (irrational) square\n' + \
'roots are:\n\n' + \
'\tsqrt(2)=[1;(2)], period=1\n' + \
'\tsqrt(3)=[1;(1,2)], period=2\n' + \
'\tsqrt(5)=[2;(4)], period=1\n' + \
'\tsqrt(6)=[2;(2,4)], period=2\n' + \
'\tsqrt(7)=[2;(1,1,1,4)], period=4\n' + \
'\tsqrt(8)=[2;(1,4)], period=2\n' + \
'\tsqrt(10)=[3;(6)], period=1\n' + \
'\tsqrt(11)=[3;(3,6)], period=2\n' + \
'\tsqrt(12)= [3;(2,6)], period=2\n' + \
'\tsqrt(13)=[3;(1,1,1,1,6)], period=5\n\n' + \
'Exactly four continued fractions, for N <= 13, have an odd period.\n\n' + \
'How many continued fractions for N <= 10000 have an odd period?\n'

def display(self):
    return description

###############################################################################
#
# Key realization:
# From Wikipedia: "The following iterative algorithm can be used for
# this [finding the continued fraction expansion of a square root] purpose
# (S is any natural number that is not a perfect square):
#
# m_0 = 0
# d_0 = 1
# a_0 = floor(sqrt(S))
# m_n+1 = d_n * a_n - m_n
# d_n+1 = (S - (m_n+1)^2) / d_n
# a_n+1 = floor((sqrt(S) + m_n+1) / d_n+1) = floor((a_0 + m_n+1) / d_n+1)
#
# Notice that m_n, d_n, and a_n are always integers. The algorithm
# terminates when this triplet is the same as one encountered before.
# The expansion will repeat from then on. The sequence [a0; a1, a2, a3, ...]
# is the continued fraction expansion:
#
###############################################################################

def solve(self):

    count = 0
    for S in range(2,limit+1):
	a0 = floor(sqrt(S))

	# perfect squares aren't irrational
	if a0*a0 != S: 
	    length = 0
	    m = 0
	    d = 1
	    a = a0

	    # new termination conditiona quits one iteration early
	    while a != 2*a0: 
		length += 1
		m = d * a - m
		d = (S - m*m) / d
		a = floor((a0 + m)/d)

	    # because of termination condition, length is accurate
	    if length & 1:
		count += 1

    return count



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
