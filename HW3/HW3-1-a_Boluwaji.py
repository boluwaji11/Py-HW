# This program shows insurance qualification

# Start

# Get the health condition from the user as a "YES or NO" question
# Check the health condition to be "YES".
# If the Boolean expression is True:
    # Get the salary from the user
    # Check the salary amount to be greater than or equal to $60,000
    # If the Boolean expression1 is True: 
        # Display "Congratulations! You meet our requirements for the health insurance!"
    # If the Boolean expression2 is False: 
        # Display "Sorry! You are not qualified because you do not earn up to $60,000
# If Boolean expression1 is False: 
# Display "Sorry! You are disqualified because of your health condition.

# End


MIN_SALARY = 60000.0 # A Named Constant for minimum salary required

health_condition = input("Are you currently in perfect healthly conditions (answer as exactly Yes or No)?: ")

if health_condition == "Yes":
    salary = float(input("How much do you currently earn annually (in USD)?: "))
    
    if salary >= MIN_SALARY:
        print("Congratulations! You meet our requirements for the health insurance!")
    else:
        print("Sorry! You are not qualified because you do not earn up to $", MIN_SALARY, sep='') 

else:
    print("Sorry! You are disqualified because of your health condition")
