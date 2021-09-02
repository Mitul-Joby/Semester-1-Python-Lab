''' IF A PERSON LEAVES HIS HOUSE AT 6:52 AM AND RUN 1 MILE AT AN EASY PACE (8:15 PER MILE), 
    THEN 3 MILES AT TEMPO (7:12 PER MILE) AND 1 MILE AT EASY PACE AGAIN, 
    WHAT TIME DOES THE PERSON GET HOME FOR BREAKFAST?'''
 
 
TLS = ((6*60)+ 52)*60       #Time left from home in seconds
EPS = (8*60) + 15           #Time taken in seconds to run a mile at an easy pace (8.15 per mile)
TPS = (7*60) + 12           #Time taken in seconds to run a mile at tempo (7.12 per mile)

#Calculating time reached home in seconds
TRS = TLS + EPS + (TPS*3) + EPS     

#Converting seconds into hours and minutes
Hours   = TRS//3600
Minutes = (TRS//60)-(Hours*60)  

#Displaying result
print('\nTime reached home {0}:{1}'.format(Hours,Minutes))
print('The person took {} minutes'.format((TRS-TLS)//60))