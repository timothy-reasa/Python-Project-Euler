#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 61
# found online at projecteuler.net/problem=61
# Solution by Timothy Reasa
#
###############################################################################

from itertools import permutations

target = 500
description = \
'\n'

def display(self):
    return description

def createCandidates(func):
    l = []
    i = 2
    temp = 1
    while temp < 10000:
	temp = func(i)
	if temp >= 1000:
	    l.append(temp)
	i += 1
    return l

def rotate(candidates,x):
    working = []
    end = x % 100
    for c in candidates:
	if c // 100 == end:
	    working.append(c)
    return working

def rotateMatch(y,x):
    return x % 100 == y // 100

def solve(self):

    tri = createCandidates(lambda x: x*(x+1) // 2)
    sqr = createCandidates(lambda x: x*x)
    pent = createCandidates(lambda x: x*(3*x-1) // 2)
    hexa = createCandidates(lambda x: x*(2*x-1))
    hept = createCandidates(lambda x: x*(5*x-3) // 2)
    octa = createCandidates(lambda x: x*(3*x-2))

    # check all orderings of polygonal numbers
    polygonal = [hept, hexa, pent, sqr, tri]
    for p in permutations(polygonal):

        for a in octa:		# cyclic, so we must pick a starting point
	    filtered1 = rotate(p[0],a)	# and permute the rest
	    for b in filtered1:
	        filtered2 = rotate(p[1],b)
	        for c in filtered2:
		    filtered3 = rotate(p[2],c)
		    for d in filtered3:
		        filtered4 = rotate(p[3],d)
		        for e in filtered4:
			    filtered5 = rotate(p[4],e)
			    for f in filtered5:
			        if rotateMatch(a,f):
				    return a+b+c+d+e+f



###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
