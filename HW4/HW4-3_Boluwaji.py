# This program creates a table of the energy consumption of a centrifuge

# Start

# Identify the speed to energy conversation factor
# Display the headings of the table
# Create a repetition structure for the speed and energy
# Display the result

# End

# ==========================================================================

# The named constants for conversion, speed change, minimum and maximum values
SPEED_TO_ENERGY = 10
MINIMUM = 15
MAXIMUM = 40
SPEED_CHANGE = 5

# Display Headers
print('--------------')
print('Speed\tEnergy')
print('--------------')

# The for loop iterations
for speed in range(MINIMUM, MAXIMUM, SPEED_CHANGE):
    energy = speed * SPEED_TO_ENERGY
    print(speed, '\t', energy)

print('--------------')
