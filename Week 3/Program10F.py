'''PROGRAM TO GENERATE THE SAME RANDOM NUMBER EVERY TIME'''

#Importing random module for seed and random function 
from random import seed,random

#Seeding the generator
seed(0)

#Generating random number
Num = random()

#Displaying the result
print('\nRandom number is',Num)