'''PROGRAM TO SWAP THE CONTENTS OF TWO MEMORY LOCATIONS USING BITWISE XOR OPERATION'''
 
#Inputs for A and B
A = int(input('\nEnter number 1: '))
B = int(input('Enter number 2: '))

#Displaying values of A and B before swapping
print('\nValues before swapping')
print('A :',A)
print('B :',B)

#Swapping contents using XOR
A = A^B
B = A^B
A = A^B

#Displaying values of A and B after swapping
print('\nValues after swapping')
print('A :',A)
print('B :',B)