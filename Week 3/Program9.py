'''PROGRAM TO CLEAR THE RIGHTMOST SET BIT OF A NUMBER'''
 
#Input for number
Num = int(input('\nEnter number: '))

#Clearing rightmost set bit
Num = Num & (Num-1)

#Displaying the result
print('\nAfter clearing rightmost set bit the number is:',Num)