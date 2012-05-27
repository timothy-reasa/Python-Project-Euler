#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 31
# found online at projecteuler.net/problem=31
#
###############################################################################

description = \
'In England the currency is made up of pound, and pence, p, and there\n' + \
'are eight coins in general circulation:\n\n' + \
'\t1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.\n\n' + \
'It is possible to make 200p in the following way:\n\n' + \
'\t1 100p  + 1 50p + 2 20p + 1 5p + 1 2p + 3 1p\n\n' + \
'How many different ways can 200p be made using any number of coins?\n'

def display(self):
    return description

def solve(self):
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    possibilities = [0] * (target+1)
    possibilities[0] = 1

    for coin in coins:
	for i in range(coin, target+1):
	    possibilities[i] += possibilities[i-coin]

    return possibilities[target]


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
