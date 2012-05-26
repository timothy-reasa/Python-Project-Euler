#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 14
# found online at projecteuler.net/problem=14
# Solution by Timothy Reasa
#
###############################################################################

limit = 1000000

description = \
'The following iterative sequence is defined for the set of positive\n' + \
'integers:\n\n' + \
'\tn ->  n/2 (n is even)\n' + \
'\tn ->  3n + 1 (n is odd)\n\n' + \
'Using the rule above and starting with 13, we generate the following\n' + \
'sequence:\n\n' + \
'\t13 ->  40 -> 20 ->  10 ->  5 ->  16 ->  8 ->  4 ->  2 ->  1\n\n' + \
'It can be seen that this sequence (starting at 13 and finishing at 1)\n' + \
'contains 10 terms. Although it has not been proved yet (Collatz \n' + \
'Problem), it is thought that all starting numbers finish at 1.\n\n' + \
'Which starting number, under one million, produces the longest chain?\n\n' + \
'NOTE: Once the chain starts the terms are allowed to go above one\n' + \
'million.\n'

def display(self):
    return description

###############################################################################
#
# Original solution by Timothy Reasa
#
# def solve(self):
#     maxSequence = 0
#     maxStart = 0
#     for i in range(1, limit+1):
# 	temp = i
#     	count = 0
# 	while temp > 1:
#             if not temp & 1: 	# i is even
# 	        temp = temp / 2
# 	    else:
# 	        temp = 3*temp + 1
#             count += 1
#         if count > maxSequence:
# 	    maxSequence = count
#             maxStart = i
# 
#     return maxStart
#
###############################################################################

###############################################################################
#
# Key realization:
# This problem lends itself to dynamic programming and memoization
#
###############################################################################

def solve(self):
    cache = [0] * limit
    
    # initialize variables
    cache[0] = 1
    maxSequence = 1
    maxStart = 1
    for i in range(2, limit+1):
        if not i & 1: 	# i is even
	    cache[i-1] = cache[(i/2)-1] + 1
	else:
	    temp = 3*i + 1
            count = 1
            while temp > i:
	        if not temp & 1:
	            temp = temp/2
                else:
	            temp = 3*temp + 1
                count += 1
	    cache[i-1] = count + cache[temp-1]
        if cache[i-1] > maxSequence:
	    maxSequence = cache[i-1]
            maxStart = i

    return maxStart


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
