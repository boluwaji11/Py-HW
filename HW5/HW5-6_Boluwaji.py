# This function uses the equaltriangle module to perform area and perimeter computations

# Start

# Define the main function
# Get the length of the triangle from the user
# Call the area and perimeter functions into the main function
# Define the area and perimeter functions using the equaltriangle module
# Display the area and perimeter of the triangle

# End

# ==================================================================
# Display the program header
print("Welcome! This program runs basic computations for an equilateral triangle.")
# print('--------------------------------------------------------------------------')
print()

# Import the equal_triangle module
import equaltriangle

# Display a menu list
AREA = 1
PERIMETER = 2
QUIT_MENU = 3

# Define the main function
def main():
    menu()
    choice = 0  # Placeholder variable for the while loop
    while choice != QUIT_MENU:

        print()
        choice = int(input("From the list, select your desired computation (1 to 3): "))

        # Run the desired computation
        if choice == AREA:
            length = float(input("Enter the length of the triangle: "))
            print(
                "\nThe area of the triangle is",
                format(equaltriangle.area(length), ".2f"),
            )
            print()
            input("Press Enter to see the menu list again... ")
        elif choice == PERIMETER:
            length = float(input("Enter the length of the triangle: "))
            print(
                "\nThe perimeter of the triangle is",
                format(equaltriangle.perimeter(length), ".2f"),
            )
            print()
            input("Press Enter to see the menu list again... ")
        elif choice == QUIT_MENU:
            print("Program is exiting.....")
        else:
            print("\nError: Invalid selection!")
            print("Enter a number between 1 and 3")
            input("\nPress Enter to make selection again... ")


# Deine the menu function
def menu():
    print("MENU")
    print("----")
    print("1. Area of the Equilateral Triangle")
    print("2. Perimeter of the Equilateral Triangle")
    print("3. Quit Program")


# Call the main function
main()
