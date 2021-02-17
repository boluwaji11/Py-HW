# This program converts temperature in degrees Celsius to Fahrenheit.

# Start
# Get the temperature in celsius from the user
# Calculate the Fahrenheit equivalent of the inputted temperature
# Check the result
    # If the result is more than 212F
        # Display "Temperature is above boiling water temperature"
            # If the result is less than 32F
                # Display "Temperature is below freezing temperature"
# End


BOILING_TEMP = 212 # A Named Constant for boiling temperature
FREEZING_TEMP = 32 # A Named Constant for freezing temperature

celsius_temperature = float(input("Please enter the temperature to convert (in Celsius): "))

convert_fahrenheit = (celsius_temperature * 1.8) + 32

print("\nThe Converted Temperature is ", format(convert_fahrenheit,'.2f'), "F", sep='')

if convert_fahrenheit > BOILING_TEMP:
    print(format(convert_fahrenheit,'.2f'), "F", " is above boiling water temperature", sep='')
elif convert_fahrenheit < FREEZING_TEMP:
    print(format(convert_fahrenheit,'.2f'), "F", " is below freezing temperature", sep='')
else:
    print(format(convert_fahrenheit,'.2f'), "F", " is neither below freezing nor above boiling temperatre", sep='')
