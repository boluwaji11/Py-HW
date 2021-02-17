# This program supports a technician with a temperature check in a vat

# Start

# Get the substance's temperature from the technician
# Check the substance's temperature against the maximum temperature
    # If the substance's temperature is greater than the maximum temperature
    # Display "The temperature is too high.
            # "Turn the thermostat down and wait 5 minutes."
            # "Then take the temperature again and enter it in the system."

# Repeat the process by getting the new temperature
    # until the substance temperature is less than maximum temperature

# Once substance's temperature is less than maximum temperature
# Display "The temperature is acceptable."
        # "Please Check again in 15 minutes. Thank You!"


# End

# ====================================================================

# Create a Named Constant for the maximum temperature
MAX_TEMP = 102.5

# Request substance's temperature from technician
sub_temp = float(input("Please enter the substance's temperature (in Celsius): "))

# Continue to repeat the process until temperature changes
while sub_temp > MAX_TEMP:
    print()
    print("Hello Technician!")
    print("The Temperature is too high.")
    print("Turn the thermostat down and wait 5 minutes.")
    print("Then, take the temperature again and enter it in the system.")
    sub_temp = float(input("\nPlease enter the new temperature (in Celsius): "))

# If the substance's temperature is less than maximum temperature
print()
print("Hello Technician!")
print("The temperature is acceptable.")
print("Please check again in 15 minutes. Thank You!")
