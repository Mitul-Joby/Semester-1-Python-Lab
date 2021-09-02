List = [[1390,'John', [95,78,99]],
        [2385,'Bob',  [93,82,73]],
        [1835,'Steve',[85,89,93]]]

L = [(List[i][1],sum(List[i][2])) for i in range(len(List))]
print('\nNew List:')
print(L)