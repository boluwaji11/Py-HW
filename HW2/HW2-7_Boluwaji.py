#This program performs stock market return analysis.

#Following code analysis shares purchasing
SHARES = 2000
COMMISSION_PERCENT = 0.03
purchase_price = float(input("Please indicate the purchasing share price: "))

amount_paid = format((SHARES * purchase_price), ',.2f')
commission_paid_buying = SHARES * purchase_price * COMMISSION_PERCENT
purchasing_total = (SHARES * purchase_price) + commission_paid_buying


#Selling Shares analysis
selling_price = float(input("Please indicate the selling share price: "))

amount_received = SHARES * selling_price
commission_paid_selling = SHARES * selling_price * COMMISSION_PERCENT
selling_total = (SHARES * selling_price) - commission_paid_selling

leftOver = selling_total - purchasing_total

#Displaying the output
print("\nThe Amount paid for buying the shares: ", "$", amount_paid, sep='')
print("The Brokerage commission paid for buying shares: ", "$", commission_paid_buying, sep='')
print("The Amount received for selling the shares: ","$", amount_received, sep='')
print("The Brokerage commission paid for selling shares: ", "$", commission_paid_selling, sep='')
print("\nThe Amount left-over after selling: ", "$", leftOver, sep='')

#Conditional Analysis 
if leftOver < 0:
    print("Sorry, You lost money!")
else:
    print("Yay! You made a profit!")
