#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 56
# found online at projecteuler.net/problem=56
# Solution by Timothy Reasa
#
###############################################################################

limit = 100
description = \
'A googol (10^100) is a massive number: one followed by one-hundred\n' + \
'zeros; 100^100 is almost unimaginably large: one followed by\n' + \
'two-hundred zeros. Despite their size, the sum of the digits in each\n' + \
'number is only 1.\n\n' + \
'Considering natural numbers of the form, a^b, where a, b < 100, what\n' + \
'is the maximum digital sum?\n'

def display(self):
    return description

def digitalSum(n):
    digitSum = 0
    while n > 0:
	digitSum += n % 10
	n = n // 10
    return digitSum	

def solve(self):
    maxSum = 0
    for a in range(limit):
	for b in range(limit):
	    # math.pow returns incorrect result?
   	    temp = digitalSum(a**b)
  	    if temp > maxSum:
		maxSum = temp

    return maxSum

	

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
