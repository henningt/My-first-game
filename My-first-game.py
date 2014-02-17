#!/usr/bin/python

from random import choice 

# choose a number
secret_number = 5

# ask user to guess a number 
some_number = raw_input() 

# compare the number that they guessed to the random number 
if secret_number == int(some_number):
	print "good job ps you still suck"
else:
	print " you are bad at life"
