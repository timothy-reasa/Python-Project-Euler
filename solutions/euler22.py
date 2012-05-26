#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 22
# found online at projecteuler.net/problem=22
# Solution by Timothy Reasa
#
###############################################################################

import string
import os

description = \
'Using names22.txt, a 46K text file containing over five-thousand first\n' + \
'names, begin by sorting it into alphabetical order. Then working out\n' + \
'the alphabetical value for each name, multiply this value by its\n' + \
'alphabetical position in the list to obtain a name score.\n\n' + \
'For example, when the list is sorted into alphabetical order, COLIN,\n' + \
'which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the\n' + \
'list. So, COLIN would obtain a score of 938 x 53 = 49714.\n\n' + \
'What is the total of all the name scores in the file?\n'

def display(self):
    return description

def computeScore(name, position):
    letterSum = 0
    for letter in name:
	letterSum += string.find(string.ascii_uppercase, letter) + 1
    return letterSum * position

def solve(self):
    if os.path.exists('./names22.txt'):
    	f = open('./names22.txt', 'r')
    else:
	f = open('./solutions/names22.txt', 'r')
    names = f.read().replace('"', '').split(',')
    names.sort()
    f.close()

    totalScore = 0
    for i in range(len(names)):
 	totalScore += computeScore(names[i], i+1)

    return totalScore


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
