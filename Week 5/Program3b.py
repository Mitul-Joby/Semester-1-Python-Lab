'''PROGRAM TO, FOR A GIVEN LIST OF TUPLES, WHERE EACH TUPLE TAKES PATTERN (NAME,MARKS) OF A STUDENT, DISPLAY ONLY NAMES.'''

#Given list
scores = [("akash", 85), ("arind", 80), ("asha",95), ('bhavana',90), ('bhavik',87)]

#Seperaing names and marks
sep   = list(zip(*scores))
names = sep[0]

#Displaying names
print('\nNames of students:')
for x in names:
    print(x.title())
print()