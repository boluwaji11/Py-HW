# This program computes the multiplication of two numbers

# Start

# Define a mainline logic function
# Get the first number from the user
# Get the second number from the user
# Define a function to make the multiplication
# Return the output to the user by calling the main function

# End

# ===========================================================
# The welcome message and header
print('Welcome! This program calculates multiplication of two numbers')
print('-----------------------------------------------------------------------')
print()

# Define the mainline logic (main function) of the program
def main():
    first_num = float(input('Please enter the first number: '))
    second_num = float(input('Please enter the second number: '))
    calc_multi(first_num, second_num)

# Define the calc_multi function for the multiplication
def calc_multi(num1, num2):
    result = num1 * num2
    print()
    print('The Multiplication of ', num1, ' and ', num2, ' is ',
          format(result, '.2f'), sep='')
    
# Call the main function
main()
