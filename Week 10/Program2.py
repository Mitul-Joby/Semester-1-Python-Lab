#A
L1 = [10, 25, 35, 45, 55, 65, 75, 85, 95]
print('\nList before:')
print(L1)
L1 = [L1[i] for i in range(len(L1)) if i not in [0,6,7]]
print('\nList after:')
print(L1)

#B
L2 = [10,25,35,25,55,65,245,85,95]
print('\n\nList before:')
print(L2)
L2 = [x for x in L2 if x !=25]
print('\nList after:')
print(L2)