'''PROGRAM TO 
    a) STRING ENCODE 
         i)	THE FIRST LETTER OF EACH LETTER OF EACH WORD IS PRINTED AT THE END
        ii)	AFTER EACH CHARACTER p IS PRINTED
 
    b)reverse a string'''

#A) STRING ENCODING
#Accepting input
string = str(input('\nEnter a string to encode: '))
last = ''

#Splitting the string into list of words
words = string.split()

#THE FIRST LETTER OF EACH LETTER OF EACH WORD IS PRINTED AT THE END
print('\nTHE FIRST LETTER OF EACH LETTER OF EACH WORD IS PRINTED AT THE END: ')
for x in words:
    print(x.strip(x[0]),end=' ')
    last = last + x[0]
print(last)

#AFTER EACH CHARACTER p IS PRINTED
print('\nAFTER EACH CHARACTER p IS PRINTED: ')
for i in string:
    print(i+'p',end='')

#B) REVERSING A STRING
string = str(input('\n\nEnter a string to reverse:'))
words = string.split()
x = 1

#Displaying the words of string in reverse
print('\nAFTER REVERSING WORDS')
while x <= len(words):
    print(words[ len(words) -x ],end=' ')
    x+=1 
print('\n')