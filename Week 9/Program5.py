def myfilter(func,List):
    Result = []
    for x in List:
        if func(x):
            Result.append(x)
    return Result

l = ['DIGICOM','4GB','RAM','16TB','HD','LCD'] 
print('\nGiven list:')
print(l)
l = list(myfilter(lambda x: not x[0].isdigit(),l))
print('\nNew list:')
print(l)