#Start
#Get the Total Square Feet of the tract of land from the user
#Calculate Number of Acres by dividing Total Square Feet by 43560
#Display the Number of Acres
#End

total_square_feet = float(input("Please enter the Total Square Feet: "))
CONVERSION_NUMBER = 43560 #This is the Named Constant for the conversion

acres = total_square_feet / CONVERSION_NUMBER

print("The Number of Acres in the tact is:", format(acres,'.2f'))
