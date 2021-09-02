'''PROGRAM CALCULATE MULTIPLICATION OF TWO RANDOM FLOAT NUMBERS'''

#Importing random module for random function 
from random import random

#Random floats
No1 = random()
No2 = random()

#Product of random float numbers
Product = No1 * No2

#Displaying the result
print('\nMULTIPLICATION OF TWO RANDOM FLOAT NUMBERS')
print('{} X {} = {}'.format(No1,No2,Product))