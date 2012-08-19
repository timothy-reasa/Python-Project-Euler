#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 59
# found online at projecteuler.net/problem=59
# Solution by Timothy Reasa
#
###############################################################################

from operator import xor
import os

space = 32

description = 'Each character on a computer is assigned a unique code\n' + \
'and the preferred standard is ASCII (American Standard Code for\n' + \
'Information Interchange). For example, uppercase A = 65, asterisk (*)\n' + \
'= 42, and lowercase k = 107.\n\n' + \
'A modern encryption method is to take a text file, convert the bytes\n' + \
'to ASCII, then XOR each byte with a given value, taken from a secret\n' + \
'key. The advantage with the XOR function is that using the same\n' + \
'encryption key on the cipher text, restores the plain text; for example,\n' +\
'65 XOR 42 = 107, then 107 XOR 42 = 65.\n\n' + \
'For unbreakable encryption, the key is the same length as the plain\n' + \
'text message, and the key is made up of random bytes. The user would\n' + \
'keep the encrypted message and the encryption key in different\n' + \
'locations, and without both "halves", it is impossible to decrypt the\n' + \
'message.\n\n' + \
'Unfortunately, this method is impractical for most users, so the\n' + \
'modified method is to use a password as a key. If the password is\n' + \
'shorter than the message, which is likely, the key is repeated\n' + \
'cyclically throughout the message. The balance for this method is using\n' + \
'a sufficiently long password key for security, but short enough to be\n' + \
'memorable.\n\n' + \
'Your task has been made easy, as the encryption key consists of three\n' + \
'lower case characters. Using cipher19.txt, a file containing the\n' + \
'encrypted ASCII codes, and the knowledge that the plain text must\n' + \
'contain common English words, decrypt the message and find the sum\n' + \
'of the ASCII values in the original text.\n'

def display(self):
    return description

def solve(self):

    # read in the ciphertext
    if os.path.exists('./cipher59.txt'):
	f = open('./cipher59.txt', 'r')
    else:
	f = open('./solutions/cipher59.txt', 'r')

    cipher = map(int, f.read().split(','))

    # partition the ciphertext into three groups corresponding to key letters
    cipher1 = []
    cipher2 = []
    cipher3 = []
    for i in range(len(cipher)):
	if i % 3 == 0:
	    cipher1.append(cipher[i])
	elif i % 3 == 1:
	    cipher2.append(cipher[i])
   	elif i % 3 == 2:
	    cipher3.append(cipher[i])

    # get the letter frequencies
    cipherCounts1 = {}
    for l in cipher1:
	cipherCounts1[l] = cipherCounts1.get(l, 0) + 1

    cipherCounts2 = {}
    for l in cipher2:
	cipherCounts2[l] = cipherCounts2.get(l, 0) + 1

    cipherCounts3 = {}
    for l in cipher3:
	cipherCounts3[l] = cipherCounts3.get(l, 0) + 1


    # from the letter frequencies in the ciphertext, determine the key
    # the most common character in English is the space
    key1 = sorted(cipherCounts1, key=cipherCounts1.get, reverse=True)[0]
    key1 = xor(key1, space)

    key2 = sorted(cipherCounts2, key=cipherCounts2.get, reverse=True)[0]
    key2 = xor(key2, space)

    key3 = sorted(cipherCounts3, key=cipherCounts3.get, reverse=True)[0]
    key3 = xor(key3, space)

    # sum up the characters in the plaintext
    letterSum = 0
    for l in cipherCounts1.keys():
	letterSum += xor(l, key1) * cipherCounts1[l]

    for l in cipherCounts2.keys():
	letterSum += xor(l, key2) * cipherCounts2[l]

    for l in cipherCounts3.keys():
	letterSum += xor(l, key3) * cipherCounts3[l]

    return letterSum


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print str(solve(None))


