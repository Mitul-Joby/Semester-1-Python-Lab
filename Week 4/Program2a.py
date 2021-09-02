'''PROGRAM TO CREATE SEPARATE LISTS FOR DIFFERENT TYPES OF DATA FOR A GIVEN HETEROGENOUS LIST'''

#Given list
GList=[1,2,3.4,5.6,(1,2,3),[11,12],{23,34},'aaa','123',3,4,[13]]

IList  = []     #List of integers
FList  = []     #List of floats
StrList= []     #List of strings
TList  = []     #List of tuples
LList  = []     #List of lists
SetList= []     #List of sets

#Seperating elements into lists based on data type
for i in GList:
    T = type(i)
    if T == int:
        IList.append(i)
    elif T == float:
        FList.append(i)
    elif T == str:
        StrList.append(i)
    elif T == tuple:
        TList.append(i)
    elif T == list:
        LList.append(i)
    elif T == set:
        SetList.append(i)

#Displaying all lists
print('\nGiven list:',GList)
print()
print('List contaning integers:',IList)
print('List contaning floats  :',FList)
print('List contaning strings :',StrList)
print('List contaning tuples  :',TList)
print('List contaning lists   :',LList)
print('List contaning sets    :',SetList)
print()