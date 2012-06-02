#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 99
# found online at projecteuler.net/problem=99
# Solution by Timothy Reasa
#
###############################################################################

import os
from math import log, pow

description = \
'Comparing two numbers written in index form like 211 and 37 is not\n' + \
'difficult, as any calculator would confirm that 2^11 = 2048 <\n' + \
'3^7 = 2187.\n\n' + \
'However, confirming that 632382^518061 > 519432^525806 would be much\n' + \
'more difficult, as both numbers contain over three million digits.\n\n' + \
'Using base_exp99.txt, a 22K text file containing one thousand lines with\n' +\
'a base/exponent pair on each line, determine which line number has the\n' + \
'greatest numerical value.\n\n' + \
'NOTE: The first two lines in the file represent the numbers in the\n' + \
'example given above.\n'

def display(self):
    return description

def solve(self):
    if os.path.exists('./base_exp99.txt'):
	f = open('./base_exp99.txt', 'r')
    else:
	f = open('./solutions/base_exp99.txt', 'r')

    values = []
    for line in f:
	nums = line.split(',')
	values.append(int(nums[1]) * log(int(nums[0])))
    f.close()

    maxIndex = 0
    maxValue = 0
    for i in range(len(values)):
	if values[i] > maxValue:
	    maxValue = values[i]
	    maxIndex = i

    return maxIndex+1

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
