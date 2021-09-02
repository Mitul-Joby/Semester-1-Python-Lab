'''PROGRAM TO CALCULATE WHEN THE USER WILL TURN 100 YEARS OLD'''

#Current Year
Year = 2020                                             

#Input for name and age
Name = input('\nWhat is your name?: ')                    
Age  = int(input('How old are you?: '))   

#Calculating year of birth      
YOB  = Year-Age      

#Displaying the output               
print('\n'+Name,'will be 100 years in the year',YOB + 100,"\n")   