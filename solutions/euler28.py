#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 28
# found online at projecteuler.net/problem=28
# Solution by Timothy Reasa
#
###############################################################################

N = 1001	# fill method works for odd N

description = \
'Starting with the number 1 and moving to the right in a clockwise\n' + \
'direction a 5 by 5 spiral is formed as follows:\n\n' + \
'\t21 22 23 24 25\n' + \
'\t20  7  8  9 10\n' + \
'\t19  6  1  2 11\n' + \
'\t18  5  4  3 12\n' + \
'\t17 16 15 14 13\n\n' + \
'It can be verified that the sum of the numbers on the diagonals is 101.\n' + \
'What is the sum of the numbers on the diagonals in a 1001 by 1001\n' + \
'spiral formed in the same way?\n'

def display(self):
    return description

###############################################################################
#
# Naive solution that actually fills an N x N grid and sums the diagonals
#
# def solve(self):
#    index = N * N
#     grid = [[-1] * N for _ in range(N)]
#     for i in reversed(range(N)):
# 	grid[0][i] = index
# 	index -= 1
# 
#     length = N - 1
#     point = (1, 0)	# next point to fill
#     while length > 0:
# 	# down
# 	for i in range(length):
# 	    grid[point[0] + i][point[1]] = index
# 	    index -= 1
# 	point = (point[0] + length - 1, point[1] + 1)
# 	
# 	# right
# 	for i in range(length):
# 	    grid[point[0]][point[1] + i] = index
# 	    index -= 1
# 	point = (point[0] - 1, point[1] + length - 1)
# 	length -= 1
# 
# 	if length > 0:
# 	    # up
# 	    for i in range(length):
# 	        grid[point[0] - i][point[1]] = index
# 	        index -= 1
# 	    point = (point[0] - (length - 1), point[1] - 1)
# 
# 	    # left
# 	    for i in range(length):
# 	        grid[point[0]][point[1] - i] = index
# 	        index -= 1
# 	    point = (point[0] + 1, point[1] - (length - 1))
# 	    length -= 1
# 
#     diagonals = 0
#     for i in range(N):
# 	diagonals += grid[i][i]
# 	diagonals += grid[i][N-i-1]
# 	if i == N-i-1:
# 	    diagonals -= grid[i][i]
# 
#     return diagonals
# 
###############################################################################

###############################################################################
#
# Optimized solution by Timothy Reasa
#
# Key realization:
# There is a pattern to the diagonals.  The upper right are squares of odd
# numbers less than or equal to N.  The lower left are squares of even numbers
# less than N, plus 1.  The lower right and upper left combine to n(n-1)+1 
# for n greater than 1
#
###############################################################################

def solve(self):
    diagonals = 0
    for n in range(1, N+1):
	if n & 1:
	    diagonals += n*n
	else:
 	    diagonals += n*n+1
	if n > 1:
	    diagonals += n*(n-1)+1

    return diagonals

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))
