'''PROGRAM TO DISTRIBUTE K APPLES AMONGST N STUDENTS EQUALLY'''

#Input for number of students and apples
N = int(input('\nEnter the number of students: '))
K = int(input('Enter the number of apples  : '))

#Caluculating number of apples per student and remaining apples
StuApple     = K//N
AppleRemain  = K%N

#Displaying the output
print('\nNo. of apples each student will get =',StuApple)
print('Remaining apples =',AppleRemain)