'''PROGRAM TO GET A SINGLE RANDOM CHARCTER FROM A SPECIFIED STRING'''

#Importing random module for choice function
from random import choice

#Input for string
String = input('\nEnter a string: ')

#Choosing a random character from the specified string 
Ch = choice(String)

#Displaying the character
print('\nA random character from {} is {}'.format(String,Ch))