'''PROGRAM TO GENERATE A RANDOM INTEGER NUMBER FROM THE GIVEN RANGE'''

#Importing random module for randint function 
from random import randint

#Inputs for range
print('\nENTER RANGE')
R1 = int(input('Enter start range: '))
R2 = int(input('Enter end range  : ')) 

#Generating floating-point number
Num = randint(R1,R2)

#Displaying the result
print('\nRandom integer number from range ({},{}) is {}'.format(R1,R2,Num))