# This program calculates retirement contributions

# Start
# Define the main function
    # Get the employee's annual gross pay
    # Get the amount of bonues paid to the employee
    # Pass gross pay to the show_pay function and call it
    # Pass bonues to the show_bonus function and call it
    # Pass the gross and bonus pay to the total_contribution function and call it
# Define the show_pay function
    # Calculate and display the contribution for the gross pay
# Define the show_bonus function
    # Calculate and display the contribution for the bonus pay
# Define the total_contrib function
# Call the main function to execute the function
# End

#=================================================================
# The welcome message and header
print()
print('Welcome! This program calculates retirement contribution')
print('------------------------------------------------------')
print()

# Define the global constant
CONTRIBUTION_RATE = 0.05

# Define the main function
def main():
    gross_pay = float(input("Please enter the employee's annual gross pay (in USD): "))
    bonus = float(input("Please enter the employee's bonus pay (in USD): "))
    print()
    show_pay(gross_pay)
    show_bonus(bonus)
    total_contribution(bonus, gross_pay)

# Define the show_pay function
def show_pay(gross):
    gross_contrib = gross * CONTRIBUTION_RATE
    print('With an annual Gross Pay of $', format(gross, ',.2f'), ', the retirement contribution is $',
          format(gross_contrib, ',.2f'), sep='')

# Define the show_bonus function
def show_bonus(bonus_pay):
    bonus_contrib = bonus_pay * CONTRIBUTION_RATE
    print('With a Bonus Pay of $', format(bonus_pay, ',.2f'), ', the retirement contribution is $',
          format(bonus_contrib, ',.2f'), sep='')

# Define the total_contribution
def total_contribution(bonus_pay, gross):
    total_contrib = (bonus_pay + gross) * CONTRIBUTION_RATE
    print("The company's Total Retirement contribution to the employee is $",
          format(total_contrib, ',.2f'), sep='')

# Call the main function to execute
main()
