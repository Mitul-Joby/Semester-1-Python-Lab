''' PROGRAM TO CONSTRUCT A DICTIONARY phone_book WITH :
    KEY: NUMBER OF ENTRIES    VALUES: (NAME, PHONE NUMBER, EMAIL , ADDRESS) 
    PERFORM THE FOLLOWING OPERATIONS:
     I)  ADD A NEW NUMBER TO PHONE BOOK
    II)  DELETE ENTRY FROM PHONE BOOK.'''

#Given values 
values = [("Rashma",8105731555,"rashma@gmail.com","bangalore"),("Saritha",9582161900,"saritha@gmail.com","Mangalore"),
("Bharathi",9276895311,"bharathi@yahoo.com","Coimbatore"),  ("deepthi",8976885553,"deepthi@gmail.com","bangalore"),
("kakoli",8816121598,"kakili@gmail.com","dispur")]

#Creating dictionary phone_book
phone_book = dict(enumerate(values,1))

#Display phone_book
print('\nPhone book is:')
print(phone_book)

#I)  ADD A NEW NUMBER TO PHONE BOOK
#Accepting input for new entry
Name     =input('\nEnter name: ')
Phone_no =input('Enter phone number: ')
email    =input('Enter email ID: ')
address  =input('Enter address: ')

#Adding entry as key length of dictionary + 1, value as tuple to phone_book
phone_book[len(phone_book)+1]= (Name,Phone_no,email,address)

#Display phone_book
print('\nPhone book after adding new entry is:')
print(phone_book)


#II)  DELETE ENTRY FROM PHONE BOOK.
#Accept key of entry to be deleted
key = int(input('\nEnter the key of entry to be deleted: '))

#If key is present in the dictionary, delete that entry, else display key not found
if key in phone_book:
    del phone_book[key]
    print('\nAfter deletion of entry',key,end=', ')
else:
    print('\nKey not found!')

#Display phone_book
print('Phone book is:')
print(phone_book,'\n')