def prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    else:
        return True

List = range(2,int(input('\nEnter a number:')))
L = [x for x in List if prime(x)]
print(L)