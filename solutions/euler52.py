#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 52
# found online at projecteuler.net/problem=52
# Solution by Timothy Reasa
#
###############################################################################

description = \
'It can be seen that the number, 125874, and its double, 251748, contain\n' + \
'exactly the same digits, but in a different order.\n\n' + \
'Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,\n' + \
'contain the same digits.\n'

def display(self):
    return description

def containSameDigits(listNums):
    digits = str(listNums[0])
    for n in listNums[1:]:
	for d in str(n):
	    if not d in digits:
		return False

    return True

def solve(self):
    i = 1
    while not containSameDigits([2*i, 3*i, 4*i, 5*i, 6*i]):
	i += 1

    return i

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
