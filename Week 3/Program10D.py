'''PROGRAM TO GENERATE A FLOATING-POINT NUMBER WITHIN A RANGE'''

#Importing random module for uniform function 
from random import uniform

#Inputs for range
print('\nENTER RANGE')
R1 = int(input('Enter start range: '))
R2 = int(input('Enter end range  : ')) 

#Generating floating-point number
Num = uniform(R1,R2)

#Displaying the result
print('\nRandom floating-point number from range ({},{}) is {}'.format(R1,R2,Num))