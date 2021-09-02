def Max(L):
    M = L[0]
    for x in L:
        if M < x:
            M = x
    return M

N = int(input('\nEnter number of elements in list to be entered: '))
L = []
for _ in range(N):
    L.append(input('Enter an element: '))
print('\nMaximum:',Max(L))