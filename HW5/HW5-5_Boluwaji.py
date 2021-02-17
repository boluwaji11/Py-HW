# This program performs mathematical functions on random numbers

# Start
# Import the random module
# Define the main fucntion
    # Provide program instructions and call the other functions
# Define a random_values function
    # Use the random module to generate two random numbers
    # Display the values
    # Return the values to be used in other functions
# Define a display_problem function
    # Get the two random numbers from random_values function
    # Insert the values in the formula to be used
    # Display the formula to the user
# Define a display_answer function
    # Get the two random numbers from random_values function
    # Calculate the correct answer
    # Ask user to input their result based on the formula provided in display_problem function
    # Check the result from user against the correct answer
        # If there's a match, the function displays "your answer is correct"
        # If there's no match, display "your answer is not correct"
            # If answer is incorrect again, display the right answer
# End

#===============================================================================================
# Display header and program details
print('Welcome! This Program performs mathematical analysis on two random numbers')
print('------------------------------------------------------------------')
print()

# Import the random Module
import random

# Define the mainline logic function
def main():
    print('For this exercise, follow the instructions below:')
    print('1. A formula with two numbers will appear on your screen')
    print('2. Use the formula to run the calculations')
    print('3. To perform the calculation, multiply the two numbers together')
    print('4. Subtract the minimum of the two numbers from the result of the multiplication.')
    print()
    first_number = random_values()      # First Random Number defined
    second_number = random_values()     # Second Random Number defined
    print('The random numbers you will be working with are:', first_number, 'and', second_number)
    print()
    display_problem(first_number, second_number)
    display_answer(first_number, second_number)

# Define the random_values functions
def random_values():
    numbers = random.randint(0,999)
    return numbers
    

# Define the display_problem function
def display_problem(first_number, second_number):
    print('Use the Formula below for your calculations:')
    print('Formula = (', first_number, '*', second_number, \
          ') - min(',first_number, ',', second_number, ')', sep='')
    print()
    print('Remember to follow the instructions described above.')
    print('Ensure you calculate your answer without using a calculator.')
    print()
    
# Define the display_answer function
def display_answer(first_number, second_number):
    user_answer = int(input('Enter Your Answer: '))
    correct_answer = (first_number * second_number) - min(first_number, second_number)
    if user_answer != correct_answer:
        print('Sorry, you provided an incorrect answer.')
        print('Check your calculations again. Your answer should be ', format(correct_answer, ','), '.', sep='')
    else:
        print('Great Job! Your calculation was correct!')

# Call the main function
main()
