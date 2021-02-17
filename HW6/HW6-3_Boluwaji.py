# This program calculates the average of all numbers stored in a file

# Start
# Define the main function
    # Open the desired file
    #  Read each line
        # Convert the string content to floating-point numbers
        # Keep a count of all values and the total of all numbers
        # Calculate the average of all the numbers
    # Close the file
    # Notify the user of the average
# Call the main function
# End

# ==================================================================================================
print('This program calculates the average of different numbers.')
print('--------------------------------------------------------------')

# Define the main function
def main():

    number_file = open('numbers.txt', 'r')
    
    count = 0       # Declare a variable to keep count of all numbers
    total = 0.0       # Accumulator set to 0.0

    # Get the values from the file, total them and compute the average
    for num in number_file:
        # Convert each line with the video running time to a floating-point number
        numbers = float(num)

        count += 1               # 1 added to the count variable to count each value.
        total += numbers         # Add the time to running total.
    
    average = total / count           # Compute the Average of all numbers

    print('The Average of the', count, 'numbers', 'is', format(average, '.2f'))
    print('Thank You.')

    number_file.close()

# Call the main function
main()
