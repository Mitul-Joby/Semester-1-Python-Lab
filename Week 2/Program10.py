'''PROGRAM TO CALCULATE FULL HOURS AND MINUTES PASSED SINCE MIDNIGHT '''

#Input for number of seconds passed since midnight
N = int(input('\nEnter the number of seconds that has passed since midnight: '))

#Calcutaing Mins and Hours passed
Mins  = N // 60
Hours = Mins // 60

#Displaying the output
print('\nHours passed after midnight   : ',Hours)
print('Minutes passed after midnight : ',Mins)