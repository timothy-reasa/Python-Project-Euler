#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 25
# found online at projecteuler.net/problem=25
#
###############################################################################

from math import ceil, log

numDigits = 1000

description = \
'The Fibonacci sequence is defined by the recurrence relation:\n\n' + \
'\tFn = Fn1 + Fn2, where F1 = 1 and F2 = 1.\n\n' + \
'Hence the first 12 terms will be:\n\n' + \
'\tF1 = 1\n' + \
'\tF2 = 1\n' + \
'\tF3 = 2\n' + \
'\tF4 = 3\n' + \
'\tF5 = 5\n' + \
'\tF6 = 8\n' + \
'\tF7 = 13\n' + \
'\tF8 = 21\n' + \
'\tF9 = 34\n' + \
'\tF10 = 55\n' + \
'\tF11 = 89\n' + \
'\tF12 = 144\n' + \
'The 12th term, F12, is the first term to contain three digits.\n\n' + \
'What is the first term in the Fibonacci sequence to contain 1000 digits?\n'

def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def solve(self):
#     oldFib = 1
#     fib = 2
#     iteration = 3
#     while len(str(fib)) < 1000:
#         temp = fib + oldFib
#         oldFib = fib
#         fib = temp
#         iteration += 1
# 
#     return iteration
# 
###############################################################################

###############################################################################
#
# Optimized solution based on math by ke9tv
#
# Key realization:
# A number that contains 1000 digits is greater than 10^999.
# The nth Fibonaci number converges to phi^n / sqrt(5).
# 	phi^n/sqrt(5) > 10^999 
#	n * log(phi) - 0.5 * log(5) > 999 * log(10)
#	n > (999 * log(10) + 0.5 * log(5)) / log(phi)
#
###############################################################################

def solve(self):
    phi = 1.618033989
    return int(ceil(((numDigits-1) * log(10) + 0.5 * log(5)) / log(phi)))

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
