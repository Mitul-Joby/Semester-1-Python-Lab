'''PROGRAM TO 
   a)	Increment a given number by 5 for n number of times using Closure.
   b)	Find Nth root of a given Number By Closure'''

#-----A-----
def process1(no,n): #Closure function
    def add5(no,n): #Inner function which is returned
        for _ in range(n):
            no=no+5
        return no
    return add5(no,n) 

#Accept inputs no,n
no = int(input('\nEnter number : '))
n = int(input('Enter number of times to increment by 5: '))

#Using inner function through closure
closure = process1(no,n)
print(closure)

#-----B-----
def process2(b,N):  #Closure function
    def nroot(b,N): #Inner function to be returned
        print(b**(1/N))
    return nroot(b,N) 

#Accept inputs b,N 
b = int(input('\nEnter base: '))
N = int(input('Enter nth root value: '))

#Using inner function through closure
closure = process2(b,N)
print()