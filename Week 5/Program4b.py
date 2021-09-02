''' GIVEN s = "bad python bad teacher bad lecture"
    i)	 REPLACE ALL OCCURRENCES OF 'bad' TO 'good'
    ii)	 REPLACE FIRST OCCURRENCE OF 'bad' TO 'good'
    iii) FIND THE LEFTMOST 'bad'
    iv)	 FIND THE SECOND 'bad' FROM LEFT
    v)	 REPLACE THE SECOND 'bad' TO 'worst' 
         AND DISPLAY FROM THAT POINT OF STRING 
         AND ALSO DISPLAY THE WHOLE STRING'''

#Given string
s = "bad python bad teacher bad lecture"
print('\nGiven string: "bad python bad teacher bad lecture"')

#i
print('\nAFTER REPLACING ALL OCCURRENCES OF \'bad\' TO \'good\'')
print(s.replace('bad','good'))

#ii
print('\nAFTER REPLACING FIRST OCCURRENCE OF \'bad\' TO \'good\'')
print(s.replace('bad','good',1))

#iii
print('\nTHE LEFTMOST \'bad\'')
print('Index:',s.find('bad'))

#iv
print('\nTHE SECOND \'bad\' FROM LEFT')
print('Index:',s.find('bad',2))

#v
print('\nAFTER REPLACING THE SECOND \'bad\' TO \'worst\'')
x = s.replace('bad','worst',2)
y = x.replace('worst','bad',1)
print(y.strip('bad python '))
print(y)
print()