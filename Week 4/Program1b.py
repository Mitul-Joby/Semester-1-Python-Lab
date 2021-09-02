'''PROGRAM TO FIND FACTORIAL OF A NUMBER'''

#Input for N
N = int(input('\nEnter a number to find factorial: '))

#Assigning values
Fact = 1
i = 1

#While loop to find factorial
while i <= N :
    Fact = Fact * i        #Calculating Factorial by multiplying 1,2... till N
    i +=1                  #Updating i for loop

#Displaying result
print('\n{}! = {}'.format(N,Fact))
print()