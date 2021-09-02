'''PROGRAM TO SHUFFLE STUDENTS IN A CLASS  '''

#Importing random module for shuffle function
from random import shuffle

#Assigning students in a class as a list
students = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10']

#Displaying students in the class before shuffling
print('\nStudents order before shuffling:')
for i in range(0,10):
    print(students[i],end=' ')

#Shuffling students
shuffle(students)

#Displaying students in the class after shuffling
print('\n\nStudents order after shuffling:')
for i in range(0,10):
    print(students[i],end=' ')
print('\n')