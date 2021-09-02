'''PROGRAM TO ACCEPT THE RADIUS OF A SPHERE AND COMPUTE ITS VOLUME AND SURFACE AREA'''

#Importing π from Math
from math import pi

#Input radius of sphere
Radius = float(input('\nEnter radius of sphere:'))

#Calculating volume and surface area of a sphere
Volume   = (4/3) * pi * (Radius**3)
SurfArea = 4 * pi * (Radius**2)

#Displaying volume and surface area
print('\nVolume of the sphere is',Volume)
print('Surface area of the sphere is',SurfArea)