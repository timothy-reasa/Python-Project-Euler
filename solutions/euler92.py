#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 92
# found online at projecteuler.net/problem=92
#
###############################################################################

from math import factorial

limit = 10000000
cacheSquares = [i*i for i in range(10)]
cacheFactorials = [factorial(i) for i in range(11)]

description = \
'A number chain is created by continuously adding the square of the\n' + \
'digits in a number to form a new number until it has been seen before.\n' +\
'For example,\n\n' + \
'\t44 -> 32 -> 13 -> 10 -> 1 -> 1\n' + \
'\t85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89\n\n' + \
'Therefore any chain that arrives at 1 or 89 will become stuck in an\n' + \
'endless loop. What is most amazing is that EVERY starting number will\n' + \
'eventually arrive at 1 or 89.\n\n' + \
'How many starting numbers below ten million will arrive at 89?\n'

def display(self):
    return description

def squareSum(n):
    k = 0
    while n > 0:
	n, m = divmod(n, 10)
	k += m*m
    return k

###############################################################################
#
# Naive solution by Timothy Reasa
# 
# def solve(self):
#     endValue = [0] * limit
# 
#     for i in range(1, limit):
#         temp = i
# 	while temp >= i and temp != 89 and temp != 1:
#             squareSum = 0
# 	    for digit in str(temp):
# 	        squareSum += int(digit)**2
# 	    temp = squareSum
#         if temp == 89:
# 	    endValue[i] = 89
# 	elif temp == 1:
# 	    endValue[i] = 1
# 	else:
# 	    endValue[i] = endValue[temp]
# 	
#     return endValue.count(89)
# 
###############################################################################

###############################################################################
#
# Better solution by Timothy Reasa
#
# Key realization:
# Numbers up to seven digits will always drop to 567 or less after one
# iteration of the sum of squares procedure.
#
# def solve(self):
#     cacheLimit = 568
#     cache = [False] * cacheLimit
# 
#     for i in range(1, cacheLimit):
#   	temp = i
# 	while not cache[temp] and temp != 89 and temp != 1:
#             temp = squareSum(temp)
# 	if temp == 89 or cache[temp]:
# 	    cache[i] = True
# 
#     total89 = cache.count(True)
#     i = cacheLimit
#     while i < limit:
#         if cache[squareSum(i)]:
# 	    total89 += 1
#         i += 1
# 
#     return total89
#
###############################################################################

###############################################################################
#
# Optimized solution based on code by Abu Shadid
#
# Key realization:
# Any permutation has the same chain of sums of squares.  We don't need to 
# check all numbers; when we find a chain that results in 89, count it for all
# its permutations
#
###############################################################################
    
def countPermutations(n):
    count = [0] * 10
    dummy = 1
    for x in str(n):
	count[int(x)] += 1
    for x in count:
	dummy *= cacheFactorials[x]
    return cacheFactorials[len(str(n))]/dummy

def squareChain(n):
    while n != 1 and n != 89:
	n = squareSum(n)
    return n

def solve(self):
    sol = 0
    for a in range(9, -1, -1):
	for b in range(a, -1, -1):
	    for c in range(b, -1, -1):
		for d in range(c, -1, -1):
		    for e in range(d, -1, -1):
	    	 	for f in range(e, -1, -1):
    			    for g in range(f, -1, -1):
				temp = a * 10**6 + b * 10**5 + c * 10**4 + \
					d * 10**3 + e * 10**2 + f * 10 + g
				if temp != 0:
				    if squareChain(temp) == 89:
					sol += countPermutations(temp)
    return sol

  


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
