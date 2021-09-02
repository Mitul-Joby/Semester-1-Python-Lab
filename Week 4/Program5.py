'''PROGRAM WHICH ACCEPTS A SEQUENCE OF COMMA-SEPARATED VALUES FROM CONSOLE AND GENERATE IT AS A LIST AND AS A TUPLE'''

#Accepting comma seperated values
CSV=input('\nEnter comma seperated values: ')

#Converting the sequence into a list and a tuple
List=list(CSV.split(','))
Tuple=tuple(CSV.split(','))

#Displaying the list and tuple
print('\nList :',List)
print('Tuple:',Tuple)
print()