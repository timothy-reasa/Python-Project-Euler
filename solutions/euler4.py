#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 4
# found online at projecteuler.net/problem=4
#
###############################################################################


description = \
'A palindromic number reads the same both ways. The largest palindrome\n' + \
'made from the product of two 2-digit numbers is 9009 = 91 x 99.\n\n' + \
'Find the largest palindrome made from the product of two 3-digit numbers.\n'

def display(self):
    return description

def isPalindrome(n):
    return str(n)[::-1] == str(n)

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     biggestPalindrome = 0
#     for i in range(1,999):
#         for j in range(1,999):
# 	    temp = i*j
# 	    if temp > biggestPalindrome and isPalindrome(temp):
# 		biggestPalindrome = temp
# 
#     return biggestPalindrome
#
###############################################################################

###############################################################################
#
# Optimized solution based on pseudocode from Lster
#
# Key observation:
# A six digit palindrome is in the form 
#   P = 100000x + 10000y + 1000z + 100z + 10y + x
#     = 11(9091x + 910y + 100z)
#
# Therefore, either a or b or both must be divisible by 11.
#
###############################################################################

def solve(self):
    biggestPalindrome = 0
    a = 999
    while a >= 100:
	if a % 11 == 0:
	    b = 999
	    delta = 1
	else:
	    b = 990 	# largest integer <= 999 and divisible by 11
	    delta = 11

	while b >= a:
	    temp = a*b
	    if temp <= biggestPalindrome:
		break
	    elif isPalindrome(temp):
		biggestPalindrome = temp

	    b -= delta
	a -= 1
 
    return biggestPalindrome


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
