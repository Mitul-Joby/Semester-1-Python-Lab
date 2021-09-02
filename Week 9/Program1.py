IPL = [{'RCB':'Kohli','Matches':116,'Runs':1000},{'CSK':'MSD','Matches':120,'Runs':994},
        {'MI':'Rahul','Matches':100,'Runs':1150}]
print('\nList before sort:')
print(IPL)
IPL = sorted(IPL,key= lambda x:x['Matches'])
print('\nList after sort:')
print(IPL) 