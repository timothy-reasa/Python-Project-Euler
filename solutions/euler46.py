#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 46
# found online at projecteuler.net/problem=46
# Solution by Timothy Reasa
#
###############################################################################

from math import sqrt, floor

limit = 10000

description = \
'It was proposed by Christian Goldbach that every odd composite number\n' + \
'can be written as the sum of a prime and twice a square.\n\n' + \
'\t9 = 7 + 212\n' + \
'\t15 = 7 + 222\n' + \
'\t21 = 3 + 232\n' + \
'\t25 = 7 + 232\n' + \
'\t27 = 19 + 222\n' + \
'\t33 = 31 + 212\n\n' + \
'It turns out that the conjecture was false.\n\n' + \
'What is the smallest odd composite that cannot be written as the sum of\n' + \
'a prime and twice a square?\n'

def display(self):
    return description

def isTwiceSquare(n):
    if n&1:
	return False
    n = sqrt(n/2)
    return n == int(n)

def solve(self):
    # create sieve
    sieveLimit = (limit-1) / 2
    sieve = [False] * sieveLimit
    crossLimit = int((floor(sqrt(limit)) - 1) / 2)
    for i in range(1, crossLimit):
	if not sieve[i]:
            j = 2*i*(i+1)
	    while j < sieveLimit:
	        sieve[j] = True
	        j += 2*i+1

    # for an odd composite, the prime must be odd, so we don't need to 
    # include 2 in the list of primes
    primes = []	
    for i in range(sieveLimit):
	if not sieve[i]:
	    primes.append(2*i+1)

    i = 33
    while True:
	check = False
	p = 0
	while primes[p] <= i:
	    if isTwiceSquare(i-primes[p]):
		check = True
		break
	    p += 1
	if check == False:
	    return i
	i += 2



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
