# This program computes the state and county sales taxes

# Start

# Define the mainline logic function for the entire program
# Get the purchase amount from the user
# Calculate the state and county sales taxes
# Define the showSale function
# Display the output of the different parameters
# Call the main function to execute

# End

# ===============================================================
# The welcome message and header
print('Welcome! This program computes State and County Sales Taxes')
print()

# Define the global constants
STATE_SALE_TAX = 0.05
COUNTY_SALE_TAX = 0.025

# Define the mainline logic
def main():
    purchase_amount = float(input('Please enter the purchase amount: '))
    state_tax = purchase_amount * STATE_SALE_TAX
    county_tax = purchase_amount * COUNTY_SALE_TAX
    showSale(purchase_amount, state_tax, county_tax)

# Define the showSale
def showSale(purchase, state, county):
    total_tax = state + county
    total_sale = purchase + total_tax
    print()
    print('Please see below the breakdown of your transaction:')
    print('---------------------------------------------------')
    print('\tThe Purchase Amount is: $',
          format(purchase, ',.2f'), sep='')
    print('\tThe State Tax is: $',
          format(state, ',.2f'), sep='')
    print('\tThe County Tax is: $',
          format(county, ',.2f'), sep='')
    print('\tThe Total Tax is: $',
          format(total_tax, ',.2f'), sep='')
    print('\tThe Total Sales Amount is: $',
          format(total_sale, ',.2f'), sep='')

# Call the main function
main()
    
    
