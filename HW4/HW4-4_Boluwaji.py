# This program calculates the running total for a withdrawal system

# Start

# Get the initial balance from the user
# Get the number of withdrawals made by the user
# Define the repetition terms
# Get the amount to be withdrawn on each withdrawal
# Check the amount to be withdrawn against the current balance
    # If the amount to be withdrawn is greater than the current balance
    # Display the message: "Your current balance is not sufficient. Try another amount."
    # Get the new withdrawal amount from the user
        # If the new amount to be withdrawn is less than or equal to the current balance
        # Allow the withdrawal

# End

# =======================================================================================

# Get the initial balance and number of withdrawals
balance = float(input('Please indicate the balance in your account (in $): '))
WithdrawalNumber = int(input('How many withdrawals do you want to make?: '))

# Define the accumulator
totalwithdraw = 0

# Define the repetition terms
for withdrawing in range(WithdrawalNumber):
    withdrawal = float(input('\nHow much would you like to withdraw?: '))

    while withdrawal > balance:
        print('Your current balance is not sufficient. Try another amount.')
        withdrawal = float(input('\nHow much would you like to withdraw?: '))
        
    balance -= withdrawal
    print('After withdrawing $', format(withdrawal,',.2f'), ', your new balance is $', format(balance,',.2f'), sep='')
    totalwithdraw += withdrawal

        
print('\nOn withdrawing ',WithdrawalNumber, ' time(s)' ', your total withdrawal was $', format(totalwithdraw,',.2f'), \
      ' and your current balance is $', \
      format(balance,',.2f'), sep='')
print('Have a great day!')
