# This program calculates the factorial of nonnegative integer numbers

# Start

# Get the desired number from the user
# Use a repetition control to calculate the factorial

# End

# ==============================================================

print('Welcome!')
number = int(input('\nPlease enter the desired positive number: '))

# Input validation
while number <= 0:
    print("Please ensure the number is a positive whole number")
    number = int(input('\nPlease enter the desired positive number: '))

factorial = 1 # The accumulator

for occurance in range(1, number+1, 1):
    factorial *= occurance

print()
print('The Factorial(!) of', number, 'is', factorial)
