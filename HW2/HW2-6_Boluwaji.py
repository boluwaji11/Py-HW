#Start
#Get the Number of Hours to be traveled from the user
#Calculate the Distance traveled by multiplying the Speed by the Number of Hours
#Display the Distance traveled
#End

number_of_hours = int(input("Please enter the Number of Hours: "))
SPEED = 70 #This is a Named Constant.

distance = SPEED * number_of_hours

print("The Distance the car will travel in", number_of_hours, "Hours:", distance, "Miles")
