#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 36
# found online at projecteuler.net/problem=36
# Solution by Timothy Reasa
#
###############################################################################

limit = 1000000
description = \
'The decimal number, 585 = 10010010012 (binary), is palindromic in both\n' + \
'bases.\n\n' + \
'Find the sum of all numbers, less than one million, which are\n' + \
'palindromic in base 10 and base 2.\n\n' + \
'(Please note that the palindromic number, in either base, may not\n' + \
'include leading zeros.)\n'

def display(self):
    return description

def isPalindrome(n):
    return str(n)[::-1] == str(n)

def solve(self):
    totalSum = 0
    for i in range(1, limit, 2):	# odd numbers aren't binary palindromes
        if isPalindrome(i) and isPalindrome(bin(i)[2:]):
	    totalSum += i
 
    return totalSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
