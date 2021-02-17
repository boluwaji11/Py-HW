# This program describes the Macy's loyalty program

# Start
# Ask the user if they have the Macy's credit card with a Yes or No question
# Check the user answers Yes
    # If the expression is True
        # Get the amount of purchase from the user
        # Check the amount against the loyalty levels
                # Check if the amount of purchase is greater than or equal to $1200
                    # If the expression is True
                    # Display "You are enrolled in the Platinum level loyalty program in the upcoming year"
                        # If the expression is False
                            # Check if the amount of purchase is greater than or equal to $500
                            # If the expression is True
                            # Display "You are enrolled in the Gold level loyalty program in the upcoming year"
                                # If the expression is False
                                # Display "You are enrolled in the Silver level loyalty program in the upcoming year"
    # If the expression is False
    # Display "You are not eligible for the loyalty program. Get a Macy's credit card"
# End

PLATINUM_AMOUNT = 1200  # Named constant for platinum level
GOLD_AMOUNT = 500       # Named constant for platinum level

credit_card_availability = input("Do you have a Macy's credit card? (answer as exactly Yes or No): ")

if credit_card_availability == "Yes":
    
    purchase_amount = float(input("\nPlease enter amount of purchase made last year (in USD): "))

    if purchase_amount > PLATINUM_AMOUNT:
        print("\nThanks for shopping with us! \nYou are enrolled in the Platinum level loyalty program in the upcoming year.")
    elif purchase_amount > GOLD_AMOUNT:
        print("\nThanks for shopping with us! \nYou are enrolled in the Gold level loyalty program in the upcoming year.")
    else:
        print("\nThanks for shopping with us! \nYou are enrolled in the Silver level loyalty program in the upcoming year.")
else:
    print("\nYou are not eligible for the loyalty program. Kindly get a Macy's credit card.")
