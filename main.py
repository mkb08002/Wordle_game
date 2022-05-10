# WORDLE game
import random

# list of words of varying length
with open('words.txt') as file:
    words_list = file.read().splitlines()


# validation of word and guess
def validation(word, word_length):
    word_validation = word.strip()
    length = word_length
    valid = 'invalid'
    letters = [char for char in word_validation]

    if valid == 'invalid' and not word_validation.isnumeric() and len(letters) == length:
            valid = 'valid'

    return valid


def begin_guessing(letters, word_to_guess, word_length):
    word_letters = letters
    word = word_to_guess
    solution = []
    total_guesses = []
    available_letters = []
    num_guesses = 0
  

    while ''.join(solution) != word:
        guess = input('What is your guess? ')

        while validation(guess, word_length) == 'invalid':
            guess = input('Please provide a valid guess: ')
            validation(guess, word_length)
        
        guess_letters = [char for char in guess]
        
        # filling in the solution
        if len(solution) == 0:
            for i in range(len(guess_letters)):
                if guess_letters[i] == word_letters[i]:
                    solution.append(guess_letters[i])
                elif guess_letters[i] != word_letters[i]:
                    solution.append('_')
            total_guesses.append(guess)
            num_guesses += 1
        else:
            for i in range(len(guess_letters)):
                if guess_letters[i] == word_letters[i]:
                    solution[i] = guess_letters[i]
                elif guess_letters[i] != word_letters[i]:
                    solution[i] = '_'
            total_guesses.append(guess)
            num_guesses += 1

        # provide available letters that weren't in correct index        
        for i in range(len(guess_letters)):
            if guess_letters[i] in word_letters and guess_letters[i] not in available_letters:
                available_letters.append(guess_letters[i])

        print("available letters", available_letters)

        print("total guesses", total_guesses)
        print(' '.join(solution))

    if ''.join(solution) == word:
        print("Congrats! You guessed the word in", num_guesses, "guesses!")


# random selection of word by length
def pick_random_word(word_length):
    # confirm valid selection of random word
    length = word_length
    word = random.choice(words_list)

    while validation(word, length) == 'invalid':
        word = random.choice(words_list)
        validation(word, length)
    
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
    

main()