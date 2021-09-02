'''PROGRAM TO IN THE GIVEN DICTIONARY FIND TOTAL MARKS AND PERCENTAGE'''

#Given Dictionary
Marks = {'PECS001': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84},
         'PECS015': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84},
         'PECS065': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 
         'PECS035': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 
         'PECS038': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}}

#Dictionary containing total and percentage
TP = {}

#Dictionary of students' total and percentage
Stu_TP = {}

#Creating the dictionary
for i in Marks:
    phy  = Marks[i]['phy']
    chem = Marks[i]['chem']
    math = Marks[i]['mat']
    bio  = Marks[i]['Bio']
    Total = phy + chem + math + bio
    Per   = (Total/400) * 100
    TP['Total'] = Total
    TP['Percentage'] = Per
    Stu_TP[i] = TP
    
#Displaying the new dictionary
print('\nDictionary of students\' total and percentage')
print(Stu_TP,'\n')