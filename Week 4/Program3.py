'''PROGRAM TO GENERATE HEART RATE RANDOMLY BETWEEN 50 TO 120 AT TIME INTERVAL OF 3 HOURS FOR 24 HOURS.
    (i)	    IF HEART RATE IS BETWEEN 50-65 PRINT AS BRADYCARDIA(LOWER HEART RATE) 
            IF GREATER THAN 100 PRINT AS TACHYCARDIA(HIGHER HEART RATE).
            ELSE PRINT AS NORMAL.
    (ii)	COUNT NUMBER OF BRADYCARDIA AND TACHYCARDIA IF ANY OF THIS IS GREATER THAN 3 DISPLAY AS RISK.
    (iii)	PRINT THE HIGHEST HEART RATE AND LOWEST HEART RATE'''

#Importing random module for randint function
from random import randint

#List for heart rates
HR = [] 
B=0;T=0;i = 0

print('\nHeart Rate:')
while i < 24:
    hr = randint(50,120)        #Generating a random integer between 50 and 120
    if 50 <= hr <= 65:          #If heart rate is between 50-65 increase count of B and display Bradycardia
        B+=1
        print(hr,' : Case of Bradycardia (Lower Heart Rate)')
    elif 100 <= hr:             #If heart rate is greater than 100 increase count of T and display Tachycardia
        T+=1
        print(hr,': Case of Tachycardia (Higher Heart Rate)')
    else:
        print(hr,' : Normal Heart Rate')
    HR.append(hr)               #Append the random integer to the list
    i+=3

#Display heart rate
print('\nHeart Rates:',end=' ')
for i in HR:
    print(i,end=' ')
print()

#Display the number of cases 
print('\nNUMBER OF CASES BRADYCARDIA:',B) 
print('NUMBER OF CASES TACHYCARDIA:',T)
     
#If cases are greater than 3 displaying case of risk
if B+T > 3:
    print('CASE OF RISK!')

#Display lowest and highest Heart Rate
HR.sort()
print('\nLowest Heart Rate :',HR[0])
print('Highest Heart Rate:',HR[-1])
print()