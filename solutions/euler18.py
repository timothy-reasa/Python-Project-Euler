#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 18
# found online at projecteuler.net/problem=18
# Solution by Timothy Reasa
#
###############################################################################

description = \
'By starting at the top of the triangle below and moving to adjacent\n' + \
'numbers on the row below, the maximum total from top to bottom is 23.\n\n' + \
'\t   3\n' + \
'\t  7 4\n' + \
'\t 2 4 6\n' + \
'\t8 5 9 3\n\n' + \
'That is, 3 + 7 + 4 + 9 = 23.\n\n' + \
'Find the maximum total from top to bottom of the triangle below:\n\n' + \
'\t                            75\n' + \
'\t                          95  64\n' + \
'\t                        17  47  82\n' + \
'\t                      18  35  87  10\n' + \
'\t                    20  04  82  47  65\n' + \
'\t                  19  01  23  75  03  34\n' + \
'\t                88  02  77  73  07  63  67\n' + \
'\t              99  65  04  28  06  16  70  92\n' + \
'\t            41  41  26  56  83  40  80  70  33\n' + \
'\t          41  48  72  33  47  32  37  16  94  29\n' + \
'\t        53  71  44  65  25  43  91  52  97  51  14\n' + \
'\t      70  11  33  28  77  73  17  78  39  68  17  57\n' + \
'\t    91  71  52  38  17  14  91  43  58  50  27  29  48\n' + \
'\t  63  66  04  68  89  53  67  30  73  16  69  87  40  31\n' + \
'\t04  62  98  27  23  09  70  98  73  93  38  53  60  04  23\n\n' + \
'NOTE: As there are only 16384 routes, it is possible to solve this\n' + \
'problem by trying every route. However, Problem 67, is the same\n' + \
'challenge with a triangle containing one-hundred rows; it cannot\n' + \
'be solved by brute force, and requires a clever method! ;o)\n'

magic = [[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20,  4, 82, 47, 65],
	[19,  1, 23, 75,  3, 34],
	[88,  2, 77, 73,  7, 63, 67],
	[99, 65,  4, 28,  6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

def display(self):
    return description

###############################################################################
# 
# Key realization:
# This problem is well suited to dynamic programming.  Each cell can be
# overwritten with the total of the most expensive path to reach that
# cell.
#
###############################################################################

def solve(self):
    for i in range(1,len(magic)):
	# left side
        magic[i][0] += magic[i-1][0]
	# center
        width = len(magic[i])
        for j in range(1, width-1):
            magic[i][j] += max(magic[i-1][j], magic[i-1][j-1])
	# right side
        if width > 1:
	    magic[i][width-1] += magic[i-1][width-2]

    return max(magic[len(magic)-1])


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
