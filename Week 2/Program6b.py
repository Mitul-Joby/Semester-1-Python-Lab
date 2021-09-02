'''PROGRAM TO SWAP CONTENTS OF TWO MEMORY LOCATION WITHOUT A TEMP VARIABLE'''

#Inputs for two integers
x = int(input('Enter an integer X :'))
y = int(input('Enter an integer Y :'))

#Displaying values of variables before swapping
print('\nThe value of X before swapping:',x)
print('The value of Y before swapping:',y)

#Swapping variables without a temp variable
x = x + y
y = x - y
x = x - y

#Displaying values of variables after swapping
print('\nThe value of X after swapping:',x)
print('The value of Y after swapping:',y,"\n")