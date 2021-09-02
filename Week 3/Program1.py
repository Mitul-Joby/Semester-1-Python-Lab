'''PROGRAM TO CALCULATE THE SIMPLE INTEREST FOR THE AMOUNT THE USER HAS TAKEN FOR A SPECIFIED NUMBER OF YEARS'''

#Input principal amount, no. of years, and interest rate 
P = float(input('\nEnter principal amount: '))
Y = int(input('Enter number of years : '))
R = float(input('Enter rate % per year : '))

#Calculating Total Amount using formula 
A = P * (1 + ((R/100) * Y))

#Displaying the amount and interest
print('\nTotal Amount is',A)
print('Interest Amount is',(A-P))