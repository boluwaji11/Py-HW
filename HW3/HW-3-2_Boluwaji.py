# This program calculates the average test scores
# and provides a lette grade to the student.

# Start

# Get the values of each test score
# Calculate the average score of all the tests
# Check the average score is greater than or equal to 90
    # If the expression is True
    # Display "Your Letter Grade is A"
    # If the expression is False
        # Check if the average score is greater than or equal to 80
        # If the expression is True
        # Display "Your Letter Grade is B"
        # If the expression is False
            # Check if the average score is greater than or equal to 70
            # If the expression is True
            # Display "Your Letter Grade is C"
            # If the expression is False
                # Check if the average score is greater than or equal to 60
                # If the expression is True
                # Display "Your Letter Grade is D"
                # If the expression is False
                # Display "Your Letter Grade is F"

# End

test1 = float(input("What is the first score?: "))
test2 = float(input("What is the second score?: "))
test3 = float(input("What is the third score?: "))
test4 = float(input("What is the fourth score?: "))

average = (test1 + test2 + test3 + test4)/4
print("\nYour Average Score is", average)

if average >= 90:
    print("Your Letter Grade is A!")
elif average >= 80:
    print("Your Letter Grade is B!")
elif average >= 70:
    print("Your Letter Grade is C!")
elif average >= 60:
    print("Your Letter Grade is D!")
else:
    print("Your Letter Grade is F!")

print("\nLet's look at other scores.")
