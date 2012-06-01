#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 42
# found online at projecteuler.net/problem=42
# Solution by Timothy Reasa
#
###############################################################################

import os
import string

description = \
'The nth term of the sequence of triangle numbers is given by\n\n' + \
'\tt_n = 0.5n(n+1)\n\n' + \
'so the first ten triangle numbers are:\n\n' + \
'\t1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...\n\n' + \
'By converting each letter in a word to a number corresponding to its\n' + \
'alphabetical position and adding these values we form a word value. For\n' + \
'example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the\n' + \
'word value is a triangle number then we shall call the word a triangle\n' + \
'word.\n\n' + \
'Using words42.txt, a 16K text file containing nearly two-thousand\n' + \
'common English words, how many are triangle words?\n'

def display(self):
    return description

def toNumber(s):
    s = s.lower()
    value = 0
    for letter in s:
	i = string.find(string.ascii_lowercase, letter)
	value += i + 1
    return value

def solve(self):
    # generate cache of triangle numbers
    triangleNumbers = set()
    for i in range(100):
	triangleNumbers.add(int(i*(i+1)*0.5))

    # open word file
    if os.path.exists('./words42.txt'):
	f = open('./words42.txt', 'r')
    else:
	f = open('./solutions/words42.txt', 'r')
    words = f.read().replace('"', '').split(',')
    f.close()

    total = 0
    for word in words:
        if toNumber(word) in triangleNumbers:
	    total += 1

    return total

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
