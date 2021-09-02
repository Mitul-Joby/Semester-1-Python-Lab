'''PROGRAM TO CALCULATE THE NUMBER OF SECONDS BETWEEN TWO  GIVEN TIMESTAMPS'''

#Input for timestamp 1
print('\nTIMESTAMP 1')
Hour1 = int(input('Enter Hour1: '))
Min1  = int(input('Enter Min1 : '))
Sec1  = int(input('Enter Sec1 : '))

#Input for timestamp 2
print('\nTIMESTAMP 2')
Hour2 = int(input('Enter Hour2: '))
Min2  = int(input('Enter Min2 : '))
Sec2  = int(input('Enter Sec2 : '))

#Converting timestamps into seconds
TotalSec1 = (((Hour1 * 60) + Min1 ) * 60) + Sec1
TotalSec2 = (((Hour2 * 60) + Min2 ) * 60) + Sec2

#Displaying the output
print('\nSeconds passed between both timestamps: ',TotalSec2 - TotalSec1)