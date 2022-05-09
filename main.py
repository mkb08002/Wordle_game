# WORDLE game

# list of words of varying length
with open('words.txt') as file:
    words_list = file.read().splitlines()

# random selection of word by length
def pick_random_word(length_num):
    print('next step')

def main():
    # user input to select length of word (3-5)

    word_length = input("Select a word length by typing 3, 4, or 5: ")
    print(word_length)

    # valid_input = 'invalid'

    # while valid_input is 'invalid':
    #     if (len(word_length.strip()) == 0) or isinstance(word_length, str):
    #         print("Please provide a valid entry")
    #         valid_input = 'invalid'
    #     else:
    #         valid_input = 'valid'
    #         pick_random_word(int(word_length))



# break down selected word and input word
# mark correct/incorrect for individual letters
# provide results back to user i.e. [selected: CORE] [input: CURT] [result: C_R_] 
# provide prompt to see previous guesses (list format)
# prompt to user continues until word is guessed correctly
# count number of guesses/restrict based on number of guesses 

main()