'''PROGRAM TO CREATE A RANDOM SAMPLE OF SIZE 2 
   FROM THE AVAILABLE NUMBER OF POPULATION WHO ARE THE POTENTIAL CANDIDATES TO BECOME EVENT COORDINATORS'''

#Importing random module for sample function
from random import sample

#Input for population
population = int(input('\nEnter population size: '))

#Choosing 2 event coordinators from the population
print('\nChoosen event coordinator IDs are:',sample(range(1,population+1),2))