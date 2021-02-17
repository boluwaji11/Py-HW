# This program compares the area of two rectangles

# Start
# Get the lengths and widths for all rectangles
# Calculate the areas by multiplying the lengths by the widths in both cases
# Check the values of the areas.
    # If the first area is greater than the second area
    # Display "The First Rectangle has a greater area than the second."
        # If the first area is smaller than the second area
        # Display "Rectangle 2 is bigger than Rectangle 1"
            # If the first area is the equal to the second area
            # Display "Both rectangles have the same areas."            
# End

# Define the variables
length1 = float(input("Please enter the length of the first rectangle: "))
width1 = float(input("Please enter the width of the first rectangle: "))

length2 = float(input("\nPlease enter the length of the second rectangle: "))
width2 = float(input("Please enter the width of the second rectangle: "))

area1 = length1 * width1
area2 = length2 * width2


        
# Declare the terms of the flags for bigger rectangle
if area1 > area2:
    area1_greater = True

else:
    area1_greater = False
    
# Declare the terms of the flags for equal rectangles
if area1 == area2:
    areas_equal = True
else:
    areas_equal = False

# Display Results
if area1_greater:
    print("\nThe first rectangle has a greater area than the second rectangle.")
  
if area1_greater == False and areas_equal == False:
    print("\nThe second rectangle has a greater area than the first rectangle.")

if areas_equal:
    print("\nBoth rectangles have the same areas.")
