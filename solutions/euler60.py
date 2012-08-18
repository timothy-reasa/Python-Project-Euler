#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 60
# found online at projecteuler.net/problem=60
# Solution by Timothy Reasa
#
###############################################################################

from math import floor, sqrt, log10

partialLimit = 10000	# guess that the largest single prime is less than 10000
limit = 100000000	# greater than 9999 concatenated with 9999

description = 'The primes 3, 7, 109, and 673, are quite remarkable. By\n' + \
'taking any two primes and concatenating them in any order the result\n' + \
'will always be prime. For example, taking 7 and 109, both 7109 and 1097\n' + \
'are prime. The sum of these four primes, 792, represents the lowest sum\n' + \
'for a set of four primes with this property.\n\n' + \
'Find the lowest sum for a set of five primes for which any two primes\n' + \
'concatenate to produce another prime.\n'

def display(self):
    return description

def isPrimePair(primeSet,m,n):
    return (10**(int(floor(log10(m)))+1)*n+m in primeSet and
	10**(int(floor(log10(n)))+1)*m+n in primeSet)

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

    # turn the sieve into a list
    primes = []
    for i in range(1, sieveLimit):
	if not sieve[i]:
	    p = 2*i+1
	    primes.append(p)

    # creating set from list for quick membership testing
    primeSet = set(primes)

    # check all prime pairs only once per pair and store the results
    #   the dictionary key is the prime
    #   the dictionary value is a set of all larger primes that are pairs
    primeLists = {}
    for a in range(partialLimit):
	primeLists[primes[a]] = set()
  	for b in range(a+1,partialLimit):
	    if isPrimePair(primeSet,primes[a],primes[b]):
		primeLists[primes[a]].add(primes[b])
	
    # test values in the union of the pair sets until we have a candidate
    #  quit as soon as the working quint sums larger than the smallest found quint
    minSum = limit
    for a in primes:
	if a > minSum or a > partialLimit: 
	    break

	for b in primeLists[a]:
	    if a+b > minSum:
		break
	    workingB = primeLists[a] & primeLists[b]

	    for c in workingB:
		if a+b+c > minSum:
		    break
		workingC = primeLists[c] & workingB

	  	for d in workingC:
		    if a+b+c+d > minSum:
			break
		    workingD = primeLists[d] & workingC

		    for e in workingD:
			if a+b+c+d+e > minSum:
			    break
			minSum = a+b+c+d+e


    return minSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))
