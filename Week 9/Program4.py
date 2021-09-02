#A
def mymap(func,List):
    Result = []
    for x in List:
        Result.append(func(x))
    return Result

words = ['Sleep','Eat','Repeat','Sing']
print('\nGiven list:')
print(words)
ing = list(mymap(lambda x: x + 'ing',words))
print('\nNew list:')
print(ing)

#B
def tuplen(x):
    return (x,len(x))

Words = ['Apple','Pineapple','Orange','Pear']
print('\nGiven list:')
print(Words)
TupLen = list(mymap(tuplen,Words))
print('\nNew list:')
print(TupLen)