#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 26
# found online at projecteuler.net/problem=26
# Solution by Timothy Reasa
#
###############################################################################

from __future__ import division

target = 1000

description = \
'A unit fraction contains 1 in the numerator. The decimal representation\n' + \
'of the unit fractions with denominators 2 to 10 are given:\n\n' + \
'\t1/2	=  0.5\n' + \
'\t1/3	=  0.(3)\n' + \
'\t1/4	=  0.25\n' + \
'\t1/5	=  0.2\n' + \
'\t1/6	=  0.1(6)\n' + \
'\t1/7	=  0.(142857)\n' + \
'\t1/8	=  0.125\n' + \
'\t1/9	=  0.(1)\n' + \
'\t1/10	=  0.1\n' + \
'Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It\n' + \
'can be seen that 1/7 has a 6-digit recurring cycle.\n\n' + \
'Find the value of d  1000 for which 1/d contains the longest recurring\n' + \
'cycle in its decimal fraction part.\n'

def display(self):
    return description

def getCycleLength(den):
    nums = []
    remainder = 1
    # assumes that every decimal either repeats or terminates
    while True:
	nums.append(remainder)
	remainder = (remainder * 10) % den
	if remainder in nums:
	    return len(nums) - nums.index(remainder) - 1
	if remainder == 0:
	    return 0


def solve(self):
    maxLength = 1
    maxIndex = 2
    for i in range(2, target + 1):
	length = getCycleLength(i)
        if length > maxLength:
	    maxIndex = i
	    maxLength = length
    return maxIndex


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
