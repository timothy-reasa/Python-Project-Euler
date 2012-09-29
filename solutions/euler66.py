#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 66
# found online at projecteuler.net/problem=66
#
###############################################################################

from math import sqrt
limit = 1000

description = \
'Consider quadratic Diophantine equations of the form:\n\n' + \
'\tx^2 - Dy^2 = 1\n\n' + \
'For example, when D=13, the minimal solution in x is 649^2 - 13*180^2\n' + \
'= 1.\n\n' + \
'It can be assumed that there are no solutions in positive integers\n' + \
'when D is square.\n\n' + \
'By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain\n' + \
'the following:\n\n' + \
'\t3^2 - 22^2 = 1\n' + \
'\t2^2 - 31^2 = 1\n' + \
'\t9^2 - 54^2 = 1\n' + \
'\t5^2 - 62^2 = 1\n' + \
'\t8^2 - 73^2 = 1\n\n' + \
'Hence, by considering minimal solutions in x for D <= 7, the largest\n' + \
'x is obtained when D=5.\n\n' + \
'Find the value of D <= 1000 in minimal solutions of x for which the\n' + \
'largest value of x is obtained.\n'

def display(self):
    return description

###############################################################################
# 
# Ket realization:
# This form of Diophantine equations are known as Pell's equations, and can
# be solved using the chakravala method.
#
# See http://en.wikipedia.org/wiki/Pell%27s_equation and 
# http://en.wikipedia.org/wiki/Chakravala_method
#
###############################################################################

def chakravala(N):
    m = 1
    k = 1
    a = 1
    b = 0
 
    while k != 1 or b == 0:
    	m = k * (m/k+1) - m
    	m = m - int((m - sqrt(N))/k) * k
 
    	tempA = (a*m + N*b) / abs(k)
    	b = (a + b*m) / abs(k)
    	k = (m*m - N) / k
 
    	a = tempA
 
    return a

def solve(self):
    maxX = 0
    maxD = 2
    for d in range (2,limit+1):
	if int(sqrt(d))**2 != d:
	    x = chakravala(d)
	    if x > maxX:
		maxX = x
		maxD = d

    return maxD

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
