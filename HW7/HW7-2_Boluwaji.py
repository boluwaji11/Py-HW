# This program calculates the annual total, its average, lowest and highest months of rainfall

# Start
# Get the amount of rainfall for each month of the year
# Calculate the total, average, lowest and highest
# Display the result
# End

# =======================================================================================

# A constant list to hold the months of the year
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# The NUM_OF_MONTHS constant holds the number of numbers that we will want to
# collect rainfall percipitation for.

NUM_OF_MONTHS = len(MONTHS)


def main():
    rainfall = [0] * NUM_OF_MONTHS  # Define the variable list

    index = 0       # Variable to hold each index of the list
    
    print('Welcome! This program will compute various rainfall statistics.')
    print()
    print('In the following prompt, please enter the rainfall amount for each month.')
    print()

    while index < NUM_OF_MONTHS:        # To get the monthly rainfall amount
        print('Enter the rainfall for Month ', index + 1, ': ', sep='', end='')
        rainfall[index] = float(input())
        index += 1
    
    total = 0           # An accumulator for the running total
    
    for value in rainfall:
        total += value
    
    print()
    print('See below the rainfall statistics for the year:')
    print('------------------------------------------------')
    # Display the total amount of rainfall
    print('The Total Amount of Rainfall for the Year is:', format(total, '.2f'))

    # Calculate the average amount of rainfall
    average = total / index         # Define the variable for the average rainfall
    
    # Display the average amount of rainfall
    print('The Average Amount of Rainfall for the Year is:', format(average, '.2f'))

    # Display the month with the highest amount of rainfall
    highest = MONTHS[rainfall.index(max(rainfall))]
    print('The Month with the highest amount of rainfall:', highest)
    
    # Display the month with the lowest amount of rainfall
    lowest = MONTHS[rainfall.index(min(rainfall))]
    print('The Month with the lowest amount of rainfall:', lowest)
   
# Call the main function
main()