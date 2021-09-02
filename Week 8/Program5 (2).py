def Length(L):
    C = 0
    for _ in L:
        C+=1
    return C

N = int(input('\nEnter number of elements in list to be entered: '))
L = []
for i in range(0,N):
    L.append(input('Enter an element: '))
print('\nLength of list:',Length(L))