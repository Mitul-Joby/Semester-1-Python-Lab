'''PROGRAM TO PRINT ALL PRIME NUMBERS FROM 2 - N'''

#Input for N
N = int(input('\nEnter a number to find prime numbers till: '))

print('\nPRIME NUMBERS FROM 2 TILL',N)
for i in range(2,N+1):                          #For loop generating number i from 2 to N
    flag = 0                                    #Set flag to 0
    for j in range(2,i):                        #For loop generating numbers from 2 to i-1
        if (i % j == 0):                        
            flag = 1                            #If i is divisible by j, set flag to 1 as not i is not prime
    if(flag==0):                                
        print(i,end=' ')                        #If flag is 0, print i as a prime number 
print('\n')