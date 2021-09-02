'''PROGRAM TO GENERATE FIBONACCI SERIES TILL N TERMS'''

#Input for N
N = int(input('\nEnter a number to generate required number of terms Fibonacci series: '))

#Assigning values
T1 = 0
T2 = 1
i  = 1

print('\nFIBONACCI SERIES:')
while i <= N :          #While loop to print the series
    print(T1,end=' ')   #Displaying term 1
    NT = T1 + T2        #Calculating next term
    T1 = T2             #Term 1 becomes term 2
    T2 = NT             #Term 2 becomes next term
    i+=1                #Updating i for while loop
print('\n')