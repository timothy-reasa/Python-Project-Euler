#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 19
# found online at projecteuler.net/problem=19
#
###############################################################################

import sys, calendar

description = \
'You are given the following information, but you may prefer to do some\n' + \
'research for yourself.\n\n' + \
'\t1 Jan 1900 was a Monday.\n' + \
'\tThirty days has September,\n' + \
'\t\tApril, June and November.\n' + \
'\t\tAll the rest have thirty-one,\n' + \
'\t\tSaving February alone,\n' + \
'\t\tWhich has twenty-eight, rain or shine.\n' + \
'\t\tAnd on leap years, twenty-nine.\n' + \
'\tA leap year occurs on any year evenly divisible by 4, but not on a\n' + \
'\t\tcentury unless it is divisible by 400.\n\n' + \
'How many Sundays fell on the first of the month during the twentieth\n' + \
'century (1 Jan 1901 to 31 Dec 2000)?\n'

def display(self):
    return description

###############################################################################
#
# Naive solution by Timothy Reasa
#
# def isLeap(x):
#     return x % 4 == 0 and (x % 100 != 0 or x% 400 == 0)
# 
# def iterateMonths(currentDay, monthsList):
#     count = 0
#     for month in monthsList:
# 	if currentDay == 0:
# 	    count += 1
# 	currentDay += month
# 	currentDay = currentDay % 7
#     return count
# 
# def solve(self):
#     dayOfWeek = 2	# 1 Jan 1901 was a Tuesday
#     daysInWeek = 7
#     monthsInLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     monthsInYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     daysInLeap = 366
#     daysInYear = 365
# 
#     count = 0
#     for year in range(1901, 2001):
#         if isLeap(year):
# 	    count += iterateMonths(dayOfWeek, monthsInLeap)
#             dayOfWeek += daysInLeap
#         else:
# 	    count += iterateMonths(dayOfWeek, monthsInYear)
#             dayOfWeek += daysInYear
#         dayOfWeek = dayOfWeek % daysInWeek
#     
#     return count
# 
###############################################################################

###############################################################################
#
# More readable solution based on calendar class suggestion from 
# 	lassevk and ashirokov
#
###############################################################################

def solve(self):
    count = 0
    for year in range(1901,2001):
        for month in range(1,13):
	    if calendar.weekday(year, month, 1) == 6:
	        count += 1

    return count


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
