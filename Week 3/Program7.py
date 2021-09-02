''' SUPPOSE THE COVER PRICE OF A BOOK IS $24.95, BUT BOOKSTORES GET A 40% DISCOUNT.
    SHIPPING COSTS $3 FOR THE FIRST COPY AND 75 CENTS FOR EACH ADDITIONAL COPY.
    WHAT IS THE TOTAL WHOLESALE COST FOR 60 COPIES?'''

CP = 24.95      #Cover price of book
D  = 40/100     #Discount
FC = 3.00       #Shipping cost for first copy
AC = 0.75       #Shipping cost for additional copies
NO = 60         #Number of copies of book

#Calculating total wholesale cost
CB  = CP - (CP * D)  #Cost of each book for bookstore
TCB = CB*NO          #Total cost of books for bookstore
TSC = FC + AC*(NO-1) #Total Shipping cost
TC  = TCB + TSC      #Total wholesale cost

#Displaying the rounded result
print('\nTotal wholesale cost is ${}'.format(round(TC,2)))