#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 17
# found online at projecteuler.net/problem=17
# Solution by Timothy Reasa
#
###############################################################################

description = \
'If the numbers 1 to 5 are written out in words: one, two, three, four,\n' + \
'five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.\n\n' + \
'If all the numbers from 1 to 1000 (one hundred) inclusive were written\n' + \
'out in words, how many letters would be used?\n\n' + \
'NOTE: Do not count spaces or hyphens. For example, 342 (three hundred\n' + \
'and forty-two) contains 23 letters and 115 (one hundred and fifteen)\n' + \
'contains 20 letters. The use of "and" when writing out numbers is in\n' + \
'compliance with British usage.\n'

def display(self):
    return description

# would be more useful if it returned the string representation of
# the word, and then counted the length

def numLetters(x):
    # irregular and base cases
    if x < 20:
	if x == 0:
	    return 0	# not written
	if x == 1 or x == 2 or x == 6 or x == 10:
	    return len("one")
	if x == 4 or x == 5 or x == 9:
	    return len("four")
	if x == 3 or x == 7 or x == 8:
	    return len("three")
	if x == 11 or x == 12:
	    return len("eleven")
	if x == 15 or x == 16:
	    return len("fifteen")
	if x == 13 or x == 14 or x == 18 or x == 19:
	    return len("thirteen")
	if x == 17:
	    return len("seventeen")
    # less than one hundred
    elif x < 100:
	if x >= 90:
	    return len("ninety") + numLetters(x-90)
	if x >= 80:
	    return len("eighty") + numLetters(x-80)
	if x >= 70:
	    return len("seventy") + numLetters(x-70)
	if x >= 60:
	    return len("sixty") + numLetters(x-60)
	if x >= 50:
	    return len("fifty") + numLetters(x-50)
	if x >= 40:
	    return len("forty") + numLetters(x-40)
	if x >= 30:
	    return len("thirty") + numLetters(x-30)
	if x >= 20:
	    return len("twenty") + numLetters(x-20)
    # less than one thousand
    elif x < 1000:
	if x > 900:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-900)
	if x == 900:
	    return numLetters(x//100) + len("hundred")
	if x > 800:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-800)
	if x == 800:
	    return numLetters(x//100) + len("hundred")
	if x > 700:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-700)
	if x == 700:
	    return numLetters(x//100) + len("hundred")
	if x > 600:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-600)
	if x == 600:
	    return numLetters(x//100) + len("hundred")
	if x > 500:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-500)
	if x == 500:
	    return numLetters(x//100) + len("hundred")
	if x > 400:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-400)
	if x == 400:
	    return numLetters(x//100) + len("hundred")
	if x > 300:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-300)
	if x == 300:
	    return numLetters(x//100) + len("hundred")
	if x > 200:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-200)
	if x == 200:
	    return numLetters(x//100) + len("hundred")
	if x > 100:
	    return numLetters(x//100) + len("hundredand") + numLetters(x-100)
	if x == 100:
	    return numLetters(x//100) + len("hundred")
    elif x == 1000:
	return numLetters(x//1000) + len("thousand")

def solve(self):
    totalLetters = 0
    for i in range (1, 1001):
        totalLetters += numLetters(i)
    return totalLetters


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
    
