#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 47
# found online at projecteuler.net/problem=47
#
###############################################################################

from math import floor, sqrt

description = \
'The first two consecutive numbers to have two distinct prime factors\n' + \
'are:\n\n' + \
'\t14 = 2 x 7\n' + \
'\t15 = 3 x 5\n\n' + \
'The first three consecutive numbers to have three distinct prime\n' + \
'factors are:\n\n' + \
'\t644 = 2^2 x 7 x 23\n' + \
'\t645 = 3 x 5 x 43\n' + \
'\t646 = 2 x 17 x 19\n\n' + \
'Find the first four consecutive integers to have four distinct primes\n' + \
'factors. What is the first of these numbers?\n'

def display(self):
    return description

def numPrimeFactors(n):
    num = 0
    limit = int(sqrt(n))
    for i in range(2, limit+1):
	flag = False
	while n % i == 0:
	    if not flag:
		flag = True
		num += 1
	    n /= i
	    if n == 1:
		return num
    return num+1

def solve(self):
    qualify = [False] * 4
    i = 2*3*5*7
    while True:
	qualify[3] = qualify[2]
	qualify[2] = qualify[1]
	qualify[1] = qualify[0]
	qualify[0] = numPrimeFactors(i) == 4
	if qualify[3] and qualify[2] and qualify[1] and qualify[0]:
	    return i - 3
	i += 1



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
