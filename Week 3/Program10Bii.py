'''PROGRAM TO CHOOSE ONE STUDENT WHO WOULD BECOME A CLASS REPRESENTATIVE'''
 
#Import random module for choice function
from random import choice

#Assigning students in a class as a list
students = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10']

#Displaying students in the class
print('\nStudents in the class:')
for i in range(0,10):
    print(students[i],end=' ')

#Choosing the class representative
CR = choice(students)

#Displaying the class representative
print('\n\n{} selected to be the class representative.'.format(CR))
print()