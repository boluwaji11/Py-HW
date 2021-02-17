# This program shows insurance qualification

# Start

# Get the health condition from the user as a "YES or NO" question
# Check the health condition to be "YES".
# If the expression is True:
    # Get the salary from the user
    # Check the salary amount to be greater than or equal to $60,000
        # If the expression is True: 
            # Display "Congratulations! You meet our requirements for the health insurance!"
                # Ask the user if they are willing to pay the $500 insurance premium as a "YES or NO" question
                # Check the response to be "YES"
                    # If the expression holds True:
                        # Display "Congratulations on making this wise choice!"
                    # If the expression is False:
                        # Ask what is the maximum they are willing to pay
                        # Display "Thank You for the information. We will reach out to you as soon as possible."
        # If the expression is False: 
            # Display "Sorry! You are not qualified because you do not earn up to $60,000
# If Boolean expression1 is False: 
# Display "Sorry! You are disqualified because of your health condition.

# End


MIN_SALARY = 60000.0 # A Named Constant for minimum salary required
INSURANCE_PREMIUM = 500.0 # A Named Constant for the insurance premium

health_condition = input("Are you currently in perfect healthly conditions (answer as exactly Yes or No)?: ")

if health_condition == "Yes":
    salary = float(input("How much do you currently earn annually (in USD)?: "))
    
    if salary >= MIN_SALARY:
        print("Congratulations! You meet our requirements for the health insurance!")
        premium_question = input("\nAre you willing to pay the $500 insurance premium (answer as exactly Yes or No)?: ")
        if premium_question == "Yes":
            print("Congratulations on making this wise choice!")
        else:
            max_premium_question = float(input("\nWhat is the maximum amount you are willing to pay (in USD)?: "))
            print("Thank You for the information. We will reach out to you as soon as possible.")
    else:
        print("Sorry! You are not qualified because you do not earn up to $", MIN_SALARY, sep='') 

else:
    print("Sorry! You are disqualified because of your health condition")
