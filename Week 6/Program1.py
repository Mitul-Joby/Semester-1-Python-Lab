'''PROGRAM TO PRINT A DICTIONARY WHERE THE KEYS ARE NUMBERS BETWEEN 1 AND 15 AND THE VALUES ARE CUBE OF KEYS'''

#Accepting input
N = int(input('\nEnter range till you need to generate cubes: '))

#Creating a dictionary
D = dict()

#Starting a loop to add key as number and value as cube of key
for i in range(1,N+1):
    D[i]=i**3

#Displaying dictionary D
print('\nThe dictionary with values between 1 and',N,'is\n{}\n'.format(D))