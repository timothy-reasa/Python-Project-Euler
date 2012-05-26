#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 21
# found online at projecteuler.net/problem=21
# Solution by Timothy Reasa
#
###############################################################################

from math import sqrt, floor

upperLimit = 10000
description = \
'Let d(n) be defined as the sum of proper divisors of n (numbers less\n' + \
'than n which divide evenly into n).  If d(a) = b and d(b) = a, where\n' + \
'a != b, then a and b are an amicable pair and each of a and b are\n' + \
'called amicable numbers.\n\n' + \
'For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,\n' + \
'22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284\n' + \
'are 1, 2, 4, 71 and 142; so d(284) = 220.\n\n' + \
'Evaluate the sum of all the amicable numbers under 10000.\n'

def display(self):
    return description

def d(x):
    sumDivisor = 1
    for i in range(2, int(floor(sqrt(x)))):
	if x % i == 0:
	    sumDivisor += i
	    temp = x / i
	    if temp != i:
	        sumDivisor += temp
	    
    return sumDivisor

def solve(self):
    cache = [0] * upperLimit
    for i in range(upperLimit):
	cache[i] = d(i)
    
    amicableSum = 0
    for i in range(upperLimit):
        if cache[i] < upperLimit and cache[cache[i]] == i and cache[i] != i:
	    amicableSum += i

    return amicableSum	


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
