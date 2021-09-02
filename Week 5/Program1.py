'''PROGRAM TO SEPERATE THE FOLLOWING LIST TO DIFFERENT LISTS BASED ON FOLLOWING CRITERIA
   i) STARTS WITH 'pizza' 
  ii) ENDS WITH 'puri' 
 iii) ENDS WITH 'dosa' '''

#Given list of strings
l=['pani puri','dosa','bhel puri','masala dosa','dahi puri','rava dosa','pizza topings','pizza mania']

#Criteria based lists
pizza = [];puri  = [];dosa  = []

#Start loop for element x in list l
for x in l:
    if x.startswith('pizza'):       #If element starts with pizza, add that element to list pizza
        pizza.append(x)             
    if x.endswith('puri'):          #If element ends with puri, add that element to list puri
        puri.append(x)              
    if x.endswith('dosa'):          #If element ends with dosa, add that element to list dosa
        dosa.append(x)              

#Display criteria based list as result
print('\nStrings in different lists')
print('List of strings starting with pizza:',pizza)
print('List of strings ending with puri   :',puri)
print('List of strings ending with dosa   :',dosa)
print()