#Start

#Get the Total Sales Amount from the user
#Calculate Sales Tax Amount by multiplying Total Sales Amount by the sales tax percentage
#Add Sales Tax Amount and the Total Sales Amount to get the Total Payment for each customer
#Display the Total Sales Amount, Sales Tax Amount and Total Payment.

#End

total_sales_amount = float(input("Please enter the Total Sales Amount: "))
TAX_PERCENT = 0.07 #This is a Named Constant.

sales_tax_amount = total_sales_amount * TAX_PERCENT

total_payment = total_sales_amount + sales_tax_amount

print("The Total Sales Amount is:", format(total_sales_amount, ',.2f'))
print("The Sales Tax Amount is:", format(sales_tax_amount, ',.2f'))
print("The Total Payment due is:", format(total_payment, ',.2f'))
