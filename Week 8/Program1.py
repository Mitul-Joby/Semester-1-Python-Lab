'''PROGRAM TO GENERATE PRIME NUMBERS USING FUNCTIONS USING METHOD OF SIEVE OF ERATOSTHENES.'''

#Importing sqrt from math module
from math import sqrt 

def sieve(n): 
    #Creating list with values from 2 to n
    l=[]
    for i in range(2,n+1):
        l.append(i)

    #Displaying first element and removing all multiples of it from the list
    while len(l)>0:
        x = l[0]
        print(x,end=' ')
        i=0
        while i<len(l):
            if l[i]%x==0:
                l.remove(l[i])
                i-=1
            i+=1

#Accept input from user
n=int(input('\nEnter number to find prime numbers till: '))

#Call function sieve
sieve(n)
print('\n')