# This program controls a thermostat device

# Start

# Get the room temperature from the device
# Check the room temperature against the desired room temperature
# Calculate a 10% decrease of the room temperature on every cycle
# Repeat the process by getting the new temperature and making the 10% decrease
    # until the room temperature is less than desired temperature of 50F

# Once room temperature is less than desired temperature
# Display "The temperature is acceptable"


# End

# ==========================================================================

# Create named constants for the desired temperature and decrease factor
TARGET_TEMP = 50
DECREASE_FACTOR = 0.1

# Get room temperature from device
room_temp = float(input('Indicate the room temperature (in Fahrenheit): '))

# Check the room temperature against the target temperature
while room_temp > TARGET_TEMP:
    print()
    print('Room temperature is high at ', format(room_temp,'.2f'), 'F', sep='')
    print('Please wait while the temperature reduces.')
    print('Thermostat in operation....')
    room_temp *= (1-DECREASE_FACTOR)
    
# If the substance's temperature is less than maximum temperature
print()
print('Room temperature is acceptable at ', format(room_temp,'.2f'), 'F', sep='')
print('Enjoy the comfort!')
