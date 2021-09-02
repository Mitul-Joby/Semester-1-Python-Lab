'''PROGRAM TO CALCULATE SMALLEST POSSIBLE NUMBER OF DESKS TO BE PURCHASED'''

#Inputs for number of students in each class
Class1 = int(input('\nEnter number of students in class 1 : '))
Class2 = int(input('Enter number of students in class 2 : '))
Class3 = int(input('Enter number of students in class 3 : '))

#Calculating number of benches required
C1Bench = (Class1 + 1)//2
C2Bench = (Class2 + 1)//2
C3Bench = (Class3 + 1)//2
TBench  = C1Bench + C2Bench + C3Bench

#Displaying the output
print('\nNumber of benches for Class 1:',C1Bench)
print('Number of benches for Class 2:',C2Bench)
print('Number of benches for Class 3:',C3Bench)
print('Total number of benches:',TBench)