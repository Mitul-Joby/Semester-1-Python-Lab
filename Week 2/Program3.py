'''PROGRAM TO CALCULATE THE DISTANCE BETWEEN TWO POINTS'''

#Input for point 1
print('\nPoint 1:')
x1 = float(input('Enter X1 :'))
y1 = float(input('Enter Y1 :'))

#Input for point 2
print('\nPoint 2:')
x2 = float(input('Enter X2 :'))
y2 = float(input('Enter Y2 :'))

#Claculating distance between two point using formula
distance = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5

#Displaing the output
print('\nDistance between (',x1,',',y1,') and (',x2,',',y2,') is',distance) 