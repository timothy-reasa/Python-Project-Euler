#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 36
# found online at projecteuler.net/problem=36
#
###############################################################################

from math import floor, log

limit = 1000000
description = \
'The decimal number, 585 = 10010010012 (binary), is palindromic in both\n' + \
'bases.\n\n' + \
'Find the sum of all numbers, less than one million, which are\n' + \
'palindromic in base 10 and base 2.\n\n' + \
'(Please note that the palindromic number, in either base, may not\n' + \
'include leading zeros.)\n'

binaryTable = [2**i for i in range(int(floor(log(limit)/log(2) + 1)))]

def display(self):
    return description

def isPalindrome(n):
    return str(n)[::-1] == str(n)

def toBinary(n):
    conversion = ''
    index = len(binaryTable) - 1
    while binaryTable[index] > n:
	index -= 1
    for i in range(index, -1, -1):
	if n >= binaryTable[i]:
	    conversion += '1'
	    n = n - binaryTable[i]
	else:
	    conversion += '0'
    return conversion

def solve(self):
    totalSum = 0
    for i in range(1, limit):
        if isPalindrome(i) and isPalindrome(toBinary(i)):
	    totalSum += i
 
    return totalSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
