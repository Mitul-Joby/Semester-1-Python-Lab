'''PROGRAM TO CONVERT DISTANCE BETWEEN 2 CITIES IN KM INTO M, CM, FT AND IN'''

#Input for distance in KM
KM = float(input('\nEnter the distance between the two cities in kilometers: '))

#Calculating M,CM,FT and IN by multiplying with constants
M  = KM * 1000
CM = KM * 100000
FT = KM * 3280.84
IN = KM * 39370.079

#Displaying the output
print('\nDistance in meters      = ',M)
print('Distance in centimeters = ',CM)
print('Distance in feet        = ',FT)
print('Distance in inches      = ',IN)