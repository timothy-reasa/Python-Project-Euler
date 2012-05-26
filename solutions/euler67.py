#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 67
# found online at projecteuler.net/problem=67
#
###############################################################################

import os

description = \
'By starting at the top of the triangle below and moving to adjacent\n' + \
'numbers on the row below, the maximum total from top to bottom is 23.\n\n' + \
'\t   3\n' + \
'\t  7 4\n' + \
'\t 2 4 6\n' + \
'\t8 5 9 3\n\n' + \
'That is, 3 + 7 + 4 + 9 = 23.\n\n' + \
'Find the maximum total from top to bottom in triangle67.txt, a 15K\n' + \
'text file containing a triangle with one-hundred rows.\n\n' + \
'NOTE: This is a much more difficult version of Problem 18. It is not\n' + \
'possible to try every route to solve this problem, as there are 2^99\n' + \
'altogether! If you could check one trillion (10^12) routes every\n' + \
'second it would take over twenty billion years to check them all.\n' + \
'There is an efficient algorithm to solve it. ;o)\n'

def display(self):
    return description

def solve(self):
    tri = [] 

    # read in the file
    if os.path.exists('./triangle67.txt'):
	f = open('./triangle67.txt', 'r')
    else:
	f = open('./solutions/triangle67.txt', 'r')

    for line in f:
	tri.append([int(i) for i in line.strip().split(' ')])
    f.close()

    # compute the result
    for i in range(1,len(tri)):
        tri[i][0] += tri[i-1][0]
        width = len(tri[i])
        for j in range(1, width-1):
	    tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
        if width > 1:
	    tri[i][width-1] += tri[i-1][width-2]

    return max(tri[len(tri)-1])


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)

