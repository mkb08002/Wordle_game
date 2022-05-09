# WORDLE game
import random

# list of words of varying length
with open('words.txt') as file:
    words_list = file.read().splitlines()

guess_letters = []
word_letters = []
incorrect_guesses = []

def you_win():
    pass


def validation(word, word_length):
    word_validation = word.strip()
    # length = word_length
    # valid = 'invalid'

    # while valid == 'invalid':
    #     letters = [char for char in word_validation]
    #     if not word_validation.isnumeric() and len(letters) == length:
    #         valid = 'valid'
    
    # return valid


def begin_guessing(word_letters, word, word_length):
    print('Time to submit your guesses!')
    guess = ''
    guess = input('What is your guess? ')

    # if guess is incorrect, add to incorrect guesses list and provide any correct letters
    
    if validation(guess, word_length) == 'invalid':
        while validation(guess, word_length) == 'invalid':
            guess = input('Please provide a valid guess? ')
            validation(guess, word_length)
    else:
        print('made it as far as word and one guess validation')
        print('word', word, word_letters)
        print('guess', guess, guess_letters)
        print('word length', str(word_length))
    


# random selection of word by length
def pick_random_word(word_length):
    # confirm valid selection of random word
    length = word_length
    word = random.choice(words_list)
    if validation(word, length) == 'invalid':
        while validation(word, length) == 'invalid':
            word = random.choice(words_list)
            validation(word, length)
    else:    
        word_letters = [char for char in word]

    begin_guessing(word_letters, word, length)


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