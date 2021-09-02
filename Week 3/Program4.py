'''PROGRAM TO FIND THE GRAVITATIONAL FORCE ACTING BETWEEN TWO OBJECTS'''

#Assigning value to G as Gravitational Constant
G = 6.674 * (10**-11)

#Inputs for calculation
Mass1 = float(input('\nEnter mass of object 1 (kg):'))
Mass2 = float(input('Enter mass of object 2 (kg):'))
Dist  = float(input('\nEnter distance between the objects (m):'))

#Calculating the gravitational force using formula
Force = (G * Mass1 * Mass2)/(Dist**2)

#Displaying the force between the two objects
print('\nThe Gravitational Force between the two objects is {} N'.format(Force))