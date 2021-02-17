# This program saves different video running times for Kevin to the video_running_times.txt file.

# Start
# Define the main function
    # Ask Kevin for the number of short videos he's working with
    # Open a file to save the videos
    # Enter the different times and write it to file
    # Close the file
    # Notify Kevin of the written file
# Call the main function
# End

# ==================================================================================================

# The headers and introductory message
print('Welcome, Kevin! This program saves a sequence of videos running times into file.')
print('--------------------------------------------------------------------------------')
print()

# Define the main funtion
def main():
    num_videos = int(input('To begin, how many videos do you have in this project, Kevin?: '))     # Number of short videos to be saved

    video_file = open('video_running_times.txt', 'w')       # Creates the file to save the running times

    # For loop to get each video's running time and write it to the video_running_times.txt file.
    print('Please enter the running time for each video')
    print()
    for count in range(1, num_videos + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    # Close the file.
    video_file.close()
    print()
    print('The video times have been saved to video_running_times.txt')

# Call the main function.
main()