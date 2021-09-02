'''PROGRAM TO REPLACE PESU IN PLACE OF PE IN FIRST 3 SRN’S FOR GIVEN SRN’S AS STRINGS EACH SEPARATED BY SPACE.
   ALSO FIND IF USER GIVEN SRN IS PRESENT OR NOT.'''

#String of SRNS
srn = "PE01 PE02 PE03 PE04 PE05 PE06 PE07 PE08 PE09 PE10"

#SRNs before replacing
print('\nSRNs before replacing PE with PESU:',srn)
#SRNs after replacing PE with PESU
print('SRNs after replacing PE with PESU:',srn.replace('PE','PESU'))

#Input to find SRN
x = str(input('\nEnter SRN to be searched: '))

#Seacrhing for SRN
r = srn.find(x)         #Returns index if found, -1 if not

#Result
if r>=0:
    print('\nSRN IS PRESENT\n')
else:
    print('\nSRN NOT FOUND\n')