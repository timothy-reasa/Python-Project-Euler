#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 76
# found online at projecteuler.net/problem=76
#
###############################################################################

description = \
'It is possible to write five as a sum in exactly six different ways:\n\n' + \
'\t4 + 1\n' + \
'\t3 + 2\n' + \
'\t3 + 1 + 1\n' + \
'\t2 + 2 + 1\n' + \
'\t2 + 1 + 1 + 1\n' + \
'\t1 + 1 + 1 + 1 + 1\n\n' + \
'How many different ways can one hundred be written as a sum of at\n' + \
'least two positive integers?\n'

def display(self):
    return description

def solve(self):
    upper = 100
    possibilities = [0] * (upper+1)
    possibilities[0] = 1

    for i in range(1, upper):
	for j in range(i, upper + 1):
	    possibilities[j] += possibilities[j-i]

    return possibilities[upper]


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
