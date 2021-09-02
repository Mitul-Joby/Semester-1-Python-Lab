'''PROGRAM TO CONVERT TEMPERATURES IN FAHRENHEIT TO CELSIUS '''

#Input for temperature in Fahrenheit
TempF = float(input('Enter temperature in Fahrenheit :'))

#Calculating temperature in Celsius with formula
TempC = ( TempF - 32 )  * (5/9)

#Displaying the output
print(TempF,'degree Fahrenheit is equal to',TempC,'degree Celsius')