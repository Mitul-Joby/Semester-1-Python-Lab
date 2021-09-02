'''PROGRAM TO READ 4 CHARACTERS SEPARATELY FROM THE USER AND CONVERT EVERY CHARACTER TO ITS NEXT ALPHABET'''
 
#Inputs for characters
Char1 = input('\nEnter a character: ')
Char2 = input('Enter a character: ')
Char3 = input('Enter a character: ')
Char4 = input('Enter a character: ')

#Display the output by:
# Converting given character value into ordinate value
# Adding 1 to the value
# Converting back the value into String
print('\nThe character after',Char1,'is :',chr(ord(Char1) + 1))
print('The character after',Char2,'is :',chr(ord(Char2) + 1))
print('The character after',Char3,'is :',chr(ord(Char3) + 1))
print('The character after',Char4,'is :',chr(ord(Char4) + 1))