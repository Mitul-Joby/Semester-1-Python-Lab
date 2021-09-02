'''PROGRAM TO 
  A) READ MOVIE DATA FROM mov1.csv FILE. 
     CSV FILE mov1.csv HAS THREE COLUMNS C1 HAS YEAR,C2 HAS RATING,C3 HAS MOVIE NAME.
 
  B) WRITE THE YEAR OF RELEASE AND MOVIE NAME FROM mov1.csv TO A TEXT FILE'''

# A) READING MOVIE DATA FROM mov1.csv FILE. 
#Opening file mov1.csv
ReadFile  = open('mov1.csv','r')

#Reading the file
data = ReadFile.read()
ReadFile.close()

#Displaying the file
print('\nFiles contents:')
print(data)


# B) WRITING THE YEAR OF RELEASE AND MOVIE NAME FROM mov1.csv TO A TEXT FILE
#Opening mov1.csv, data.txt file
ReadFile  = open('mov1.csv','r')
WriteFile = open('data.txt','w')

#Reading a line of mov1.csv
line = ReadFile.readline()

#Writing year of release and movie name
while line:
    lineData = line.strip()
    dataList = lineData.split(',')
    #Writing to file data.txt
    print(dataList[0],dataList[2],file=WriteFile)
    #Reading next line
    line = ReadFile.readline()

#Closing files
ReadFile.close()
WriteFile.close()