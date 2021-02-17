# This program checks elements in one list against another list

# Start
# Declare the elements in variable A & B
# Create an empty list in C
# Create an accumulator to count the elements
# Display the results
# End

# =============================================================================
def main():
    # Define variable lists A & B
    A = ['Sam', 'Eric', 'Don', 'Glenn', 'Jaeki', 'Melissa', 'Fred', 'Jannette', 'Maria']
    B = ['Sara', 'Eliza', 'Sam', 'Glenn', 'Maria' , 'Alex']

    C = []      # An empty list to hold the new list

    count = 0       # An accumulator to hold the count of students

    for full_students in A:
        for students in B:
            if full_students == students:
                count += 1
                C.append(students)

    # Display the results
    print('There were', count, 'students from the Python class who attended the career fair.')
    print('The students are:')
    print(C)

# Call the main function
main()