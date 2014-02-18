#!/usr/bin/python

from random import choice 

# choose a number
dont_look = [1,2,3,4,5,6,7,8,9,10]
secret_number = choice(dont_look)

# ask user to guess a number 
some_number = raw_input() 

# compare the number that they guessed to the random number 
if secret_number == int(some_number):
	print "good job ps you still suck"
else:
	print " you are bad at life"
