'''PROGRAM TO FIND THE SUM OF DIGITS OF A 4-DIGIT INT NO. AND ITS INDIVIDUAL DIGITS'''

#Input for an integer number
Number = int(input('\nInput a four digit number : '))

#Calculating the digits of the number
Digit1 = Number//1000
Digit2 = (Number - Digit1*1000 ) // 100 
Digit3 = (Number - Digit1*1000 - Digit2*100) // 10   
Digit4 = (Number - Digit1*1000 - Digit2*100 - Digit3*10)

#Calculating the sum of the digits
Sum = Digit1 + Digit2 + Digit3 + Digit4 

#Displaying the output
print('\nFirst Digit  : ',Digit1)
print('Second Digit : ',Digit2)
print('Third Digit  : ',Digit3)
print('Fourth Digit : ',Digit4)
print('\nThe sum of the digits in the number',Number,'is',Sum)