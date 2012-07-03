#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 43
# found online at projecteuler.net/problem=43
# Solution by Timothy Reasa
#
###############################################################################

from itertools import permutations

description = \
'The number, 1406357289, is a 0 to 9 pandigital number because it is\n' + \
'made up of each of the digits 0 to 9 in some order, but it also has a\n' + \
'rather interesting sub-string divisibility property.\n\n' + \
'Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,\n' + \
'we note the following:\n\n' + \
'\td2d3d4=406 is divisible by 2\n' + \
'\td3d4d5=063 is divisible by 3\n' + \
'\td4d5d6=635 is divisible by 5\n' + \
'\td5d6d7=357 is divisible by 7\n' + \
'\td6d7d8=572 is divisible by 11\n' + \
'\td7d8d9=728 is divisible by 13\n' + \
'\td8d9d10=289 is divisible by 17\n\n' + \
'Find the sum of all 0 to 9 pandigital numbers with this property.\n'

def display(self):
    return description

def solve(self):
    digits = [0,1,2,3,4,5,6,7,8,9]
    divisors = [0,2,3,5,7,11,13,17]
    total = 0
    for p in permutations(digits):
	check = True
	for i in range(1,len(p)-2):
	    number = p[i]*100+p[i+1]*10+p[i+2]
	    if number % divisors[i] != 0:
		check = False
		break
	if check:
	    total += int(filter(str.isdigit, repr(p)))
    return total


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
