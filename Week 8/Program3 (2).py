def length(string):
    L = list(string.split())
    lon = 0
    word = L[0]
    for x in L:
        C = 0
        for _ in x:
            C+=1
        if C > lon:
            lon = C
            word = x
    return lon,word

string = input('\nEnter a string: ')
longest,Word = length(string)
print('\nLength of longest string',Word,'is',longest)