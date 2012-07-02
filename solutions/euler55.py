#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 55
# found online at projecteuler.net/problem=55
# Solution by Timothy Reasa
#
###############################################################################

limit = 10000
cache = set()

description = \
'If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.\n\n' + \
'Not all numbers produce palindromes so quickly. For example,\n\n' + \
'\t349 + 943 = 1292,\n' + \
'\t1292 + 2921 = 4213\n' + \
'\t4213 + 3124 = 7337\n\n' + \
'That is, 349 took three iterations to arrive at a palindrome.\n\n' + \
'Although no one has proved it yet, it is thought that some numbers,\n' + \
'like 196, never produce a palindrome. A number that never forms a\n' + \
'palindrome through the reverse and add process is called a Lychrel\n' + \
'number. Due to the theoretical nature of these numbers, and for the\n' + \
'purpose of this problem, we shall assume that a number is Lychrel until\n' + \
'proven otherwise. In addition you are given that for every number below\n' + \
'ten-thousand, it will either (i) become a palindrome in less than fifty\n' + \
'iterations, or, (ii) no one, with all the computing power that exists,\n' + \
'has managed so far to map it to a palindrome. In fact, 10677 is the\n' + \
'first number to be shown to require over fifty iterations before\n' + \
'producing a palindrome: 4668731596684224866951378664 (53 iterations,\n' + \
'28-digits).\n\n' + \
'Surprisingly, there are palindromic numbers that are themselves Lychrel\n' + \
'numbers; the first example is 4994.\n\n' + \
'How many Lychrel numbers are there below ten-thousand?\n\n' + \
'NOTE: Wording was modified slightly on 24 April 2007 to emphasise the\n' + \
'theoretical nature of Lychrel numbers.\n'

def display(self):
    return description

###############################################################################
#
# Cacheing the intermediate results of the Lychrel test shaves about 10ms
# from the execution time.
#
###############################################################################

def isLychrel(n):
    history = set()
    history.add(n)
    revN = int(str(n)[::-1])
    for i in range(50):
	n += revN
	history.add(n)
	revN = int(str(n)[::-1])
	if n == revN or n in cache:
	    cache.update(history)
	    return False

    return True
	
def solve(self):
    count = 0
    for i in range(1, limit):
	if isLychrel(i):
	    count += 1

    return count

	

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
