# WORDLE game
import random

# list of words of varying length
with open('words.txt') as file:
    words_list = file.read().splitlines()


def begin_guessing(word):
    pass

# random selection of word by length
def pick_random_word(word_length):
    word_valid = 'invalid'

    # confirm valid selection of random word
    while word_valid == 'invalid':
        word = random.choice(words_list)
        letters = [char for char in word]
        if len(letters) == word_length:
            word_valid = 'valid'

    begin_guessing(word)

def main():
    # user input to select length of word (3-5)

    valid_input = 'invalid'

    while valid_input == 'invalid':
        word_length = input("Select a word length by typing 3, 4, or 5: ")

        if (len(word_length.strip()) == 0) or not word_length.isnumeric() or (int(word_length) < 3) or (int(word_length) > 5):
            print("Please provide a valid entry")
            valid_input = 'invalid'
        else:
            valid_input = 'valid'
            word_length = int(word_length)
            pick_random_word(word_length)
    




# break down selected word and input word
# mark correct/incorrect for individual letters
# provide results back to user i.e. [selected: CORE] [input: CURT] [result: C_R_] 
# provide prompt to see previous guesses (list format)
# prompt to user continues until word is guessed correctly
# count number of guesses/restrict based on number of guesses 

main()