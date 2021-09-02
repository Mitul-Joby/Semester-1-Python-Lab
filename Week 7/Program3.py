'''PROGRAM TO USE CALLBACK TO FIND SUM, DOUBLE AND TRIPLE THE GIVEN NUMBER'''

#Function for callback
def outer(func,n):
    func(n)

#Function to find sum of digits
def Sum(n):
    s = 0
    s = 0
    while (n != 0):
        s = s + int(n % 10)
        n = int(n/10)
    print('Sum: ',s)

#Function to double number
def Double(n):
    print('Double: ',2*n)

#Function to triple number
def Triple(n):
    print('Triple: ',3*n)

#Accept input n from user 
n = int(input('\nEnter a number: '))

#Using callback
outer(Sum,n) 
outer(Double,n) 
outer(Triple,n)

print()