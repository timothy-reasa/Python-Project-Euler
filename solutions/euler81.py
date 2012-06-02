#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 81
# found online at projecteuler.net/problem=81
# Solution by Timothy Reasa
#
###############################################################################

import os

dimension = 80
description = \
'In the 5 by 5 matrix below, the minimal path sum from the top left to\n' + \
'the bottom right, by only moving to the right and down, is indicated in\n' + \
'bold red and is equal to 2427.\n\n' + \
'\t131\t673\t234\t103\t18\n' + \
'\t201\t96\t342\t965\t150\n' + \
'\t630\t803\t746\t422\t111\n' + \
'\t537\t699\t497\t121\t956\n' + \
'\t805\t732\t524\t37\t331\n\n' + \
'Find the minimal path sum, in matrix81.txt, a 31K text file containing\n' + \
'an 80 by 80 matrix, from the top left to the bottom right by only\n' + \
'moving right and down.\n'

def display(self):
    return description

def solve(self):
    if os.path.exists('./matrix81.txt'):
	f = open('./matrix81.txt', 'r')
    else:
	f = open('./solutions/matrix81.txt', 'r')

    matrix = []
    for line in f:
	matrix.append([int(r) for r in line.split(',')])
	
    f.close()

    # initialize the top row of the matrix
    for i in range(1, len(matrix[0])):
	matrix[0][i] += matrix[0][i-1]
   
    # initialize the first column of the matrix
    for i in range(1, len(matrix)):
	matrix[i][0] += matrix[i-1][0]

    # fill in the rest of the matrix 
    for i in range(1, len(matrix)):
	for j in range(1, len(matrix[1])):
	    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[dimension-1][dimension-1]

	

###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
