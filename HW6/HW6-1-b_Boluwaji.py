# This program reads different video running times from the video_running_times.txt file.

# Start
# Define the main function
    # Open the video_running_times file with the videos running times
    # Read each line
        # Convert the string content to floating-point number
        # Keep a count of all times and the total recording time
    # Close the file
    # Notify Kevin of the content of the file and the total
# Call the main function
# End

# ==================================================================================================
print('This program shows all the videos running times and the total.')
print('--------------------------------------------------------------')
print()

# Define the main function
def main():
    # Open the video_running_times.txt for reading
    video_file = open('video_running_times.txt', 'r')

    total = 0.0       # Accumulator set to 0.0
    count = 0         # Declare a variable to keep count of the videos.

    print('Kevin, here are the running times for each video:')

    # Get the values from the file and total them.
    for line in video_file:
        # Convert each line with the video running time to a floating-point number
        run_time = float(line)
        
        count += 1      # 1 added to the count variable to count each video.

        # Display the time.
        print('Video #', count, ': ', run_time, sep='')
        

        # Add the time to running total.
        total += run_time

    # Close the file.
    video_file.close()

    # Display the total of the running times.
    print()
    print('For all videos, the total running time is', format(total, '.2f'), 'seconds.')
    print('Thank You.')

# Call the main function
main()