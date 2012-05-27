#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 371
# found online at projecteuler.net/problem=371
#
###############################################################################

description = \
'Oregon licence plates consist of three letters followed by a three\n' + \
'digit number (each digit can be from [0..9]).\n\n' + \
'While driving to work Seth plays the following game:\n\n' + \
'Whenever the numbers of two licence plates seen on his trip add to\n' + \
'1000 that\'s a win.\n\n' + \
'E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500\n' + \
'too. (as long as he sees them in the same trip).\n\n' + \
'Find the expected number of plates he needs to see for a win. Give\n' + \
'your answer rounded to 8 decimal places behind the decimal point.\n\n' + \
'Note: We assume that each licence plate seen is equally likely to\n' + \
'have any three digit number on it.\n'

def display(self):
    return description

###############################################################################
#
# Optimized solution by xantoscguin
#
# Let Expected[k] be the expected number of license plates needed to win if
# Seth hasn't yet won and has seen n distinct plates that aren't 000 or 500.
# Let Expected500[k] be the expected number of license plates needed to win if
# Seth hasn't yet won, has seen n distinct plates that aren't 000 or 500, and 
# has seen 500
#
###############################################################################

def solve(self):
    Expected = [0.0] * 500
    Expected500 = [0.0] * 500

    Expected[499] = 2.0	# It doesn't really matter what your initial conditions
    Expected500[499] = 2.0	# are.  Error is gemoetrically removed

    for i in range(498, -1, -1):
        Expected500[i] = (1000 + (998-2*i)*Expected500[i+1]) / (999-i)
	Expected[i] = (1000 + (998-2*i)*Expected[i+1] + Expected500[i]) \
		 / (999-i)
    return '{0:.8f}'.format(Expected[0])


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
