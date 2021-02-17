# This program calculates dietary information

# Start

# Define main function
    # In the main function,get fat and carbohydrate information from the user
    # Pass fat to calories_fat and call it
    # Pass carbohydrate to calories_carbs and call it
    # Call calories_fat and calories_carbs in main 
# Define the calories_fat function
    # Calculates the calories using fat and displays the result
# Define the calories_carbs function
    # Calculates the calories using carbohydrate and displays the result
# Call the main function

# End

#==================================================================
# The welcome message and header
print('Welcome! This program calculates dietary information')
print('------------------------------------------------------')
print()

# Define the global constants
FAT_CONVERSION_FACTOR = 9.0
CARB_CONVERSION_FACTOR = 4.0

# Define the main function of the program
def main():
    fat = float(input('Please enter your daily fat consumption (in grams): '))
    carbohydrate = float(input('Please enter your daily carbohydrate consumption (in grams): '))
    print()
    calories_fat(fat)
    calories_carb(carbohydrate)

# Define the calories_fat function
def calories_fat(fat_amount):
    calories_from_fat = fat_amount * FAT_CONVERSION_FACTOR
    print('The Amount of Calories in', fat_amount, 'gram(s) of Fat consumed is',
          format(calories_from_fat, '.2f'))

# Define the calories_carb function
def calories_carb(carbs):
    calories_from_carbs = carbs * CARB_CONVERSION_FACTOR
    print('The Amount of Calories in', carbs, 'gram(s) of Carbohydrate consumed is',
          format(calories_from_carbs, '.2f'))

# Call the main function
main()
    
    
