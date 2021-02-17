# This program calculates the index of strength of list of words within a paragraph of texts

# Start
    # Create a variable to hold the paragraph of texts
    # Identify words that repeat within the paragraph
    # Calculate the Strength Index
    # Display the results
# End

# ========================================================================================
def main():
    print('TEXT MINING')
    print('------------')
    # Declare the variable to hold the paragraph
    paragraph = "The concept behind gamification is not new, but certainly the advent of the word has been difficult. The term “gamification” was “coined in 2002 by British consultant Nick Pelling, as a “deliberately ugly word” to describe “apply gamelike accelerated user interface design to make electronic transactions both enjoyable and fast” . This element of gamification can be considered from two different points of view. On the one hand, we have the non-game context, which refers to the many fields where gamification can be applied. On the other hand, the context refers also to the gaming environment where the player is immersed and can fulfil game requirements. As we are going to see in the next chapters, game elements, design and context represent the three main elements characterizing all the gamified experiences."
    word_list = ['gamification', 'game', 'gamified', 'gaming']      # Words to check

    total_word = 0      # Accumulator for the total repeating words

    print('See below the output of the text mining activity on the paragraph:')
    print()

    for each_word in word_list:
        counting = paragraph.count(each_word)       # Count each repeating words
        print('The word', each_word, 'has been repeated', counting, 'time(s).')       # Display the result for each word on the list
        total_word += counting

    # Display the total repeating result
    print()
    print('Overall, the words in the list have been repeated', total_word, 'times.')

    # Calculate the strength index
    word_split = paragraph.split()          # Split each word in the paragraph to a list using the space character
    length_paragraph = len(word_split)          # Total number of words in the paragraph
    strength_index = total_word / length_paragraph      # Calculate strength of index

    # Display the result
    print('The Strength Index is', format(strength_index, '.3f'))
    print()

# Call the main function
main()