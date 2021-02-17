# This program iterates the myClassmates list using a while loop
# Start
# Define the main function
    # Define the myClassmates variable with an empty list
    # Get the first names from the users
    # Check if users want to add more names
    # Display the list to the user
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
    print('The initial list of first names is:', myClassmates)
    
    myClassmates[len(myClassmates)-1] = 'XXX'    # Replace the last element on the list

    print()
    print("Your updated classmates' first names are:")

    index = 0       # Indexing for the elements within the myClassmates list

    while index < len(myClassmates):
        print('Classmate #', index + 1, ': ', myClassmates[index], sep='')
        index += 1              # Accumulates on each iteration to outline classmate's index number
        
# Call the main function
main()