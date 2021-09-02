'''PROGRAM TO, FOR A GIVEN LIST OF CAPTAINS AND TEAMS (IN RESPECTIVE ORDER) ASSIGN THEM TO IPL TEAMS.'''

#Given lists
cap_list  = ['Koli','Dhoni','RohitS',]
team_list = ['RCB', 'CSK', 'MI']

#Assigning list of captains to IPL teams
cap_team  = list(zip(cap_list,team_list))

#Displaying output
print('\nCaptains and their respective teams:')
for x in cap_team:
    print(x)
print()