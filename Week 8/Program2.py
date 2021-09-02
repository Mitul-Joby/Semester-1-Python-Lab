'''PROGRAM TO 
   A) REVERSE THE GIVEN STRING USING RECURSION
   B) SOLVE TOWER OF HANOI PROBLEM
   C) USE RECURSION TO RAISE A NUMBER TO A GIVEN POWER n'''

#A REVERSE THE GIVEN STRING USING RECURSION
#Function to reverse the string
def rev(string):
    if len(string) ==0:
        return string
    else:
        return rev(string[1:]) + string[0]

#Accept input from user
string = input('\nEnter string to be reversed: ')
print('Reversed string is :',rev(string))


#B SOLVE TOWER OF HANOI PROBLEM
def tower(n,From,To,Aux): 
    if n == 1:
        print('Move',n,'from',From,'to',To)
        return
    tower(n-1,From,Aux,To)
    print('Move',n,'from',From,'to',To)
    tower(n-1,Aux,To,From)
         
#Accept input from user 
n = int(input('\n\nEnter number of disk: '))

#Call function tower
tower(n,'A','C','B') 


#C USE RECURSION TO RAISE A NUMBER TO A GIVEN POWER n
def power(b,p):
    if(p==0):       #When power is zero
        return 1
    elif(p%2==0):   #When power is even
        return( power(b,int(p/2)) * power(b,int(p/2)) )
    else:           #When power is odd
        return( b * power(b,int(p/2)) * power(b,int(p/2)) )

#Accept inputs for base and power from the user 
x = int(input('\nEnter base : '))
y = int(input('Enter power: '))

#Call function power
print(power(x,y),'\n')