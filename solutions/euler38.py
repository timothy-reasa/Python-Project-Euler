#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 38
# found online at projecteuler.net/problem=38
# Solution by Timothy Reasa
#
###############################################################################

limit = 1000000
description = \
'Take the number 192 and multiply it by each of 1, 2, and 3:\n\n' + \
'\t192  1 = 192\n' + \
'\t192  2 = 384\n' + \
'\t192  3 = 576\n\n' + \
'By concatenating each product we get the 1 to 9 pandigital,\n' + \
'192384576. We will call 192384576 the concatenated product of 192\n' + \
'and (1,2,3).\n\n' + \
'The same can be achieved by starting with 9 and multiplying by 1, 2,\n' + \
'3, 4, and 5, giving the pandigital, 918273645, which is the\n' + \
'concatenated product of 9 and (1,2,3,4,5).\n\n' + \
'What is the largest 1 to 9 pandigital 9-digit number that can be\n' + \
'formed as the concatenated product of an integer with (1,2, ... , n)\n' + \
'where n  1?\n'

def display(self):
    return description

def isPandigital9(n):
    n = str(n)
    if len(n) != 9:
	return False
    for i in range(1,10):
	if not str(i) in n:
	    return False
    return True

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#    maxPan = 0
#     i = 1
#     while len(str(i) + str(2*i)) < 10: # must be product of at least 2 mults
#         temp = ''
# 	j = 1
# 	while len(temp) < 9:
# 	    temp += str(j*i)
# 	    j += 1
#         if temp > maxPan and isPandigital9(temp):
# 	    maxPan = temp
#   	i += 1
#  
#     return maxPan
#
###############################################################################

###############################################################################
#
# Optimized solution by Timothy Reasa
#
# Key realization:
# The maximum integer that could produce a 9 digit pandigital is 9876, because
# we need a 4-digit number that takes 5 digits when doubled.  Since these
# digits are the most significant in the resulting sum of products, we can
# start there and count down until we find a suitable number.
#
###############################################################################

def solve(self):
    maxPan = 0
    i = 9876	# maximum 4-digit number that could produce a pandigital
    while not isPandigital9(str(i) + str(2*i)):
        i -= 1
 
    return int(str(i) + str(2*i))


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
