def sort(L):
    for _ in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L
    
N = int(input('\nEnter number of elements in list to be entered: '))
L = []
for i in range(0,N):
    L.append( int(input('Enter an element: ')) )
print('\nList before sorting:')
print(L)
L = sort(L)
print('\nList after sorting:')
print(L)