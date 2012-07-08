#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 50
# found online at projecteuler.net/problem=50
# Solution by Timothy Reasa
#
###############################################################################

from math import floor, sqrt
import sys

limit = 1000000

description = \
'The prime 41, can be written as the sum of six consecutive primes:\n\n' + \
'\t41 = 2 + 3 + 5 + 7 + 11 + 13\n\n' + \
'This is the longest sum of consecutive primes that adds to a prime\n' + \
'below one-hundred.\n\n'  + \
'The longest sum of consecutive primes below one-thousand that adds to a\n' + \
'prime, contains 21 terms, and is equal to 953.\n\n' + \
'Which prime, below one-million, can be written as the sum of the most\n' + \
'consecutive primes?\n'

def display(self):
    return description  

def recursiveSolve(i, j, primeSet, sumThrough):
    if i == j:
	return (i, i)

    if sumThrough[j] - sumThrough[i] in primeSet:
	return (i, j)
    
    soln1 = recursiveSolve(i, j-1, primeSet, sumThrough)
    soln2 = recursiveSolve(i+1, j, primeSet, sumThrough)
    if soln1[1] - soln1[0] > soln2[1] - soln2[0]:
	return soln1

    return soln2
	

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

    # turn the sieve into a list, 
    # as well as track the sum of all primes less than it
    temp = 2
    sumThrough = [2]
    primeSet = set()
    primeSet.add(2)
    for i in range(1, sieveLimit):
	if not sieve[i]:
	    p = 2*i+1
	    primeSet.add(p)
	    temp += p
	    sumThrough.append(temp)

    consecutive = 0
    result = 0
    i = 0		# upper bound on the range of consecutive primes
    while i < len(sumThrough):
	j = i - consecutive - 1		# lower bound
	while j >= 0:
	    if sumThrough[i] - sumThrough[j] > limit:
		break
	    if sumThrough[i] - sumThrough[j] in primeSet:
		consecutive = i - j
		result = sumThrough[i] - sumThrough[j]
	    j -= 1
	i += 1
    
    return result


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
