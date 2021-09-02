'''PROGRAM TO ENTER MARKS OF STUDENTS TILL YOU NEED TO STOP. 
    a)	FIND HIGHEST MARKS
    b)	FIND NUMBER OF STUDENTS WHO HAVE SCORED HIGHEST
    c)	FIND SECOND HIGHEST MARKS
    d)  ENTER FAIL MARKS AND REMOVE IF FAIL MARKS PRESENT IN LIST'''

#Create Marks List
MARKS=[]
count = 0

print('\nEnter marks of students. Enter non-digit to quit.')
#Start while loop which is always true
while 0==0:
    Marks = input()                             #Accept input
    if (not Marks.isdigit()) or ( int(Marks)<0):#If input is not a number then break from the loop
        break
    MARKS.append(int(Marks))                    #If input is a number, append to mark list
MARKS.sort()                                    #Sort list

#Start for loop to check number of students with highest marks
for i in MARKS:
    if i == max(MARKS):
        count+=1

#Display results
print('\nMarks of students:',MARKS)
print('\nHighest Marks:',max(MARKS))
print('Number of students with Highest Marks:',count)

#Create loop while element is not equal to the element before it 
i=1
while MARKS[-i]==MARKS[-(i+1)]:
        i+=1
#Display second last unique element
print('Second Highest Marks:',MARKS[-(i+1)])

#Accept Input for fail marks
Fail = int(input('\nEnter fail marks: '))

#Create new list which will contain no fail marks
NMARKS=[]

#For all elements in the mark list, check if they are greater than fail marks. If they are append to the new list
for i in MARKS:
    if i>Fail:
        NMARKS.append(i)

#Display the list without fail marks
print('\nNew List without fail marks:',NMARKS)
print()