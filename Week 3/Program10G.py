'''PROGRAM TO ROLL A DICE IN SUCH A WAY THAT EVERY TIME YOU GET THE SAME NUMBER'''

#Importing random module for seed and randint function 
from random import seed,randint

#Seeding the generator
seed(0)

#Generating random number with possibility of 1 2 3 4 5 6
Num = randint(1,6)           

#Displaying the result
print('\nNumber rolled is',Num)