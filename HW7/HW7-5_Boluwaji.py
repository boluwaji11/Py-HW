# This program performs text mining

# Start
# Define the main function
# Declare the string variable "paragraph"
# Declare the list of characters to be removed
# Convert all characters to lowercase
# Convert the string variable "paragraph" to a list
# Compute the text mining for each element in the list
# Display the result
# Call the main function
# End

# ==========================================================================================
def main():
    print('Welcome! This program performs text mining.')
    print()

    paragraph = "The concept behind gamification is not new, but certainly the advent of the word has been difficult. The term “gamification” was “coined in 2002 by British consultant Nick Pelling, as a “deliberately ugly word” to describe “apply gamelike accelerated user interface design to make electronic transactions both enjoyable and fast”. This element of gamification can be considered from two different points of view. On the one hand, we have the non-game context, which refers to the many fields where gamification can be applied. On the other hand, the context refers also to the gaming environment where the player is immersed and can fulfil game requirements. As we are going to see in the next chapters, game elements, design and context represent the three main elements characterizing all the gamified experiences."

    special_characters = ['“' ,'”' , ',' , '.' , '-' ]          # List of characters to be removed

    for every_character in special_characters:
        paragraph = paragraph.replace(every_character, '')

    paragraph = paragraph.lower()           # Converts block of strings to lowercase characters
    paragraph = paragraph.split()           # Converts string to list

    # Compute the text mining
    mining_output = [['Word','Count']]

    for each_word in paragraph:
        word_count = paragraph.count(each_word)
        mining_output.append([each_word, word_count])

    # Display the result
    print('The result of the text mining is:')
    print()
    print(mining_output)

# Call the main function 
main()

