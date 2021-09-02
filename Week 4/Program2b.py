''' PROGRAM TO A LIST SORT IN ASCENDING AND DESCENDING ORDER 
        i)  LIST OF STRINGS 
        ii) LIST OF NUMBERS'''

#Assigning values to
StrList = ['aaa','xxx','bbb']
NumList = [23,12,34]

#Displaying given list
print('\nList of strings:',StrList)
print('List of numbers:',NumList)

#Sorting list in ascending order	   
StrList.sort()
NumList.sort()
	   
#Displaying list sorted in ascending order
print('\nList of strings in ascending order:',StrList)
print('List of numbers in ascending order:',NumList)

#Sorting list in descending order	   
StrList.sort(reverse=True)
NumList.sort(reverse=True)	   

#Displaying list sorted in descending order
print('\nList of strings in descending order:',StrList)
print('List of numbers in descending order:',NumList)
print()