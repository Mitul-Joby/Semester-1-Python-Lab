'''PROGRAM TO FIND nTH FIBONACCI NUMBER USING CONCEPT OF DECORATOR'''
#Function fun
def func(fun):
    print('nth Fibbonacci number:',fun())
    return ''
#Decorator
@func
def outer(): 
    a = 1
    b = 1
    n = int(input('\nEnter n to find nth fibbonaci number: '))
    if n == 1:
        return 0
    for _ in range(2,n):
        a,b = b,b+a
    return b
    
print(outer)