#A
List = [(36,4),(13,7),(64,8),(25,5),(81,4),(24,8)]

print('\nGiven list of strings:')
print(List)
List = list(filter(lambda x: x[0]%x[1]==0,List))
print('\nList now:')
print(List)

#B
L1 = [14,73,41,46,93,68,26,51,84,33] 
L2 = [73,82,37,35,41,91,33,10,14,61]
print('\nGiven lists:')
print(L1)
print(L2)
Int = list(filter(lambda x:x in L2,L1))
print('\nIntersection of lists:')
print(Int)