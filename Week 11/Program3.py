S=['Bob','Peter','Steve','Alex']
M=[]
for name in S:
    marks = int(input(str(name)+' marks: '))
    if marks>100:
        raise Exception('Marks should not exceed 100.')
    else:
      M.append(marks)  
try:
    i=int(input('Enter index: '))
    print(M[i])
    avg=int(input('Enter no. of subjects to calculate average: '))
    print(M[i]/avg)
except IndexError as error:
        print('Invalid record',error)
except ZeroDivisionError as e:
        print('No. of subjects cannot be 0',e)