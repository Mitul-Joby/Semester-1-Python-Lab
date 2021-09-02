''' PROGRAM TO 
    FOR A GIVEN LIST OF STUDENTS, MARKS FOR PHY, CHEM, MATHS AND BIOLOGY FORM A DICTIONARY 
    WHERE KEY IS SRN AND VALUES ARE DICTIONARY CONTAINING PCMB MARKS OF RESPECTIVE STUDENT.'''

#Given lists
srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"]
p_marks = [98,99,85,92,79]
c_marks = [91,90,84,98,99]
m_marks = [78,39,60,50,84]
b_marks = [95,59,78,80,89]

#Creating the dictionary
marks = {}
PCMB_stu = {}
for i in range(len(srns)):
    #Creating a dictionary with key as subject and value as marks
    marks['Phys'] = p_marks[i]
    marks['Chem'] = c_marks[i]
    marks['Math'] = m_marks[i]
    marks['Bio']  = b_marks[i]

    #Creating a dictionary with key as SRN and value as marks dictionary
    PCMB_stu[srns[i]] = marks

#Displaying the dictionary
print('\nThe dictionary is:')
print(PCMB_stu,'\n')