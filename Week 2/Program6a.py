'''PROGRAM TO SWAP CONTENTS OF TWO MEMORY LOCATION WITH TEMP VARIABLE'''

#Inputs for two integers
x = int(input('Enter an integer X :'))
y = int(input('Enter an integer Y :'))

#Displaying values of variables before swapping
print('\nThe value of X before swapping:',x)
print('The value of Y before swapping:',y)

#Swapping variables with the help of a temp variable
temp = x
x = y
y = temp

#Displaying values of variables after swapping
print('\nThe value of X after swapping:',x)
print('The value of Y after swapping:',y)