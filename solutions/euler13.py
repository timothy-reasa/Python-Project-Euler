#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 13
# found online at projecteuler.net/problem=13
# Solution by Timothy Reasa
#
###############################################################################

import os

description = \
'Work out the first ten digits of the sum of the one-hundred 50-digit\n' + \
'numbers in the text file \'numbers13.txt\'.\n'

def display(self):
    return description

def solve(self):
    if os.path.exists('numbers13.txt'):
	f = open('./numbers13.txt', 'r')
    else:
	f = open('./solutions/numbers13.txt', 'r')

    total = 0
    for line in f:
        total += int(line)

    f.close()
    return int(str(total)[:10])


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
