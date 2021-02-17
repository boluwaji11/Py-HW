# This program allows the user to add, show and search records within a file

# Start
# Define the main function and call other functions
    # Create and open the coffee.txt file
    # Input all the necessary fields
    # Write the fields for each record into the file
    # Read the file
    # Search the file for specific records
# End

# =================================================================================
print('This Program saves, displays and searches coffee file records.')
print('---------------------------------------------------------------')
print()

# Define the main function and call the other functions
def main():
    append_field()
    read_record()
    search_record()

############################ To create and add records into the file
def append_field():
    coffee_file = open('coffee.txt', 'a') # Create and add information to the file

    print('Welcome! Do you want to add a new record to the file?')
    keep_going = input('Indicate Y = Yes or Anything Else = No: ')      # To check what operation the user wants to perform

    # Add records to the file.
    while keep_going == 'y' or keep_going == 'Y' or keep_going == 'Yes' or keep_going == 'yes':
        
        # Get the coffee record data.
        print('Please enter the following coffee data:')
        description = input('Description: ')
        quantity = int(input('Quantity (in pounds): '))
        # Append the data to the file.
        coffee_file.write(description + '\t') # Quantity will be presented in the same line as description
        coffee_file.write(str(quantity) + '\n') # new line new coffee
        print()

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        keep_going = input('Y = Yes, Anything Else = No: ')
    
    # Close the file.
    coffee_file.close()
    if keep_going == 'y' or keep_going == 'Y':
        print()
        print('Data Appended to coffee.txt.')
    else:
        print()
        print('No need data was added to coffee.txt')
    print('====================================')
    print('====================================')


############################# To read the file
def read_record():
    print("Now, let's see what is the coffee inventory")
    print('Description\t', 'Quantity')
    print('--------------------------')

    coffee_file = open('coffee.txt', 'r')       # Open the coffee.txt file.

    # Read the first records' fields.
    record = coffee_file.readline()

    # Read the rest of the file.
    while record != '':
        
        # Strip the \n from the record.
        record = record.rstrip()

        # Display the record.
        print(record)
        
        # Read the next record.
        record = coffee_file.readline()

    # Close the file.
    coffee_file.close()

############################ To search for records within the file
def search_record():   
    print()
    interest_search = input('Are you interested in searching for a record?: ')      # Check if the user wants to search for a record

    while interest_search == 'y' or interest_search == 'Y' or interest_search == 'Yes' or interest_search == 'yes':

        found = False       # A bool variable to use as a flag.

        print()
        # Get the search value.
        search = input('Enter the coffee description to search for: ')
        coffee_file = open('coffee.txt', 'r')   # Open the coffee.txt file

        # Read the first record
        record = coffee_file.readline()

        while record != '':
            record = record.rstrip('\n')
            split_record = record.split('\t')      # Placeholder variable for spliting the description from the quantity field
            field_list_descr = split_record[0]            # Placeholder variable for listing the description field
            field_list_qty = float(split_record[1])        # Placeholder variable for listing the quantity field
            
            if field_list_descr == search:            # Check the search against the field list
                print()
                print('Record Found....')
                print('Description\t', 'Quantity')
                print('--------------------------')
                print(field_list_descr, '\t', field_list_qty)
                found = True
            
            # Read the next record
            record = coffee_file.readline()
    
        # Close the file.
        coffee_file.close()

        # If the search value was not found in the file display a message.
        if not found:
            print('That record was not found in the file.')

        print()
        print('Want to search for another record?')
        interest_search = input('Yes = Y, No = N: ')
    
    print()
    print('Thanks for using the Program!')


# Call the main function.
main()
