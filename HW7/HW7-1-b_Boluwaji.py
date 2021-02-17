# This program appends and displays the first names on the list
# Start
# Define the main function
    # Define the myClassmates variable with an empty list
    # Get the first names from the users
    # Check if users want to add more names
    # Display each element on individual lines
# End

# ========================================================================
print('Welcome!')
print('This program creates and displays a list of first names.')
print('--------------------------------------------')

def main():
    myClassmates = []       # Defined empty list

    name_again = 'y'     # Placeholder to check while loop

    

    while name_again == 'y' or name_again == 'Y' or name_again == 'Yes' or name_again == 'yes' :
        first_name = input("Please enter your classmate's first name: ")
        myClassmates.append(first_name)
        print()
        print('Do you want to add another name?')
        name_again = input('Y = Yes, Anything Else = No: ')         # Check if user wants to add another name
        print()
    
    count = 0       # Variable to hold each classmate

    print("Your classmates' first names are:")
    for first_name in myClassmates:
        print('Classmate #', count + 1, ': ', first_name, sep='')
        count += 1              # Accumulates on each iteration

# Call the main function
main()