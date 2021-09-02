#A
lang = ['ws3sw','C++','Python','ada','daa','FAAF']
print('\nGiven list of strings:')
print(lang)
pal = list(filter(lambda x: x == x[::-1],lang))
print('\nList of pallnidromes:')
print(pal)

#B
l    = ['DIGICOM','4GB','RAM','16TB','HD','LCD'] 
print('\nGiven list of strings:')
print(l)
l = list(filter(lambda x: not x[0].isdigit(),l))
print('\nList now:')
print(l)