'''FROM FILE MOV1.CSV MAKE A DICTIONARY WITH KEY AS YEAR AND VALUES AS NAME OF MOVIES RELEASED IN THAT YEAR.'''

#Opening mov1.csv
ReadFile  = open('mov1.csv','r')

#Reading a line of mov1.csv
line = ReadFile.readline()

dictionary = {}

while line:
    data  = line.strip()
    List  = data.split(',')
    year  = List[0]
    movie = List[2]

    #If key as year exist, insert value movie else add entry with key as year and value as movie
    if year in dictionary:
        dictionary[year].insert(0,movie)
    else:
        dictionary[year]=[movie]

    #Reading next line
    line = ReadFile.readline()

#Displaying the dictionary
print('\nDictionary is :')
print(dictionary)
print()

#Closing files
ReadFile.close()