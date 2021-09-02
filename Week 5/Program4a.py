'''GIVEN 'mohanDas Karamchand gandhi',  PRINT  
        i)   m K gandhi 
        ii)  M K GANDHI  
        iii) M K Gandhi   
        iv)  Mohandas Karamchand Gandhi'''

#Given string
string  = 'mohanDas Karamchand gandhi'

#Creating New string
words   = string.split()
newstr  = ''
intial1 = (words[0])[0]
intial2 = (words[1])[0]
newstr  = intial1 +' '+ intial2 +' '+ words[2]

#Displaying outputs
print('\nOutput:')
print(newstr)           #Printing m K gandhi
print(newstr.upper())   #Printing M K GANDHI
print(newstr.title())   #Printing M K Gandhi
print(string.title())   #Printing Mohandas Karamchand Gandhi
print()