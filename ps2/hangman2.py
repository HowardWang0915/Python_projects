import random
import string

WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'
# This function simply opens the txt file
def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# loaded wordlist 
wordlist = load_words()

# This function will choose a random word from txt
def choose_word(wordlist):
    return random.choice(wordlist)


'''
#   secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
#   letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
#   returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
'''
# This function will determine whether the game ended or not
def is_word_guessed(secret_word, letters_guessed):
    same = 0
    for secret_char in secret_word:
        if secret_char in letters_guessed:
            same += 1
    if same == len(secret_word):
        return True
    else:
        return False

'''
#   secret_word: string, the word the user is guessing

#   letters_guessed: list (of letters), which letters have been guessed so far

#   returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
'''
# This function will print out the guessed alphabet and underscore for those not guessed
def get_guessed_word(secret_word, letters_guessed):
    answer = ""
    for secret_char in secret_word:
        if secret_char in letters_guessed:
            answer += secret_char
        else:
            answer += "_ "
    return answer

# This function will return a string of characters that is not guessed
def get_availiable_letters(letters_guessed):
    answer = ""
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            answer += char
    return answer

#################################################
# Helper functions

# This function will determine if two words pair up
def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
    corresponding letters of other_word, or the letter is the special symbol
    _ , and my_word and other_word are of the same length;
    False otherwise: 
    '''
    match = 0           # If this number == len(other_word), then match
    my_word = my_word.replace(" ", "")
    if (len(my_word) != len(other_word)):
        return False
    for i in range(len(my_word)):
        if my_word[i] == other_word[i] or (my_word[i] == "_" and other_word[i] not in letters_guessed):
            match += 1
    
    if match == len(other_word):
        return True
    else:
        return False


# This function should display all the possible words
def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.
    '''
    no = 0
    for words in wordlist:
        if match_with_gaps(my_word, words, letters_guessed):
            print(words, end = " ")
            no += 1
    print("")
    if no == 0:
        print("No matches found")

    
# The main game function
def hangman(secret_word):
    guess = 6               # initial guesses
    warnings = 3            # initial warnings
    letters_guessed = []    # a list to store all the guessed letters
    print("Welcome to the game of hangman!")
    print("I am thinking of a word that is", len(secret_word), "long")
    print("You have", warnings, "warnings left.")
    while (not is_word_guessed(secret_word, letters_guessed) and warnings > 0 and guess > 0):
        print("-------------")
        print("You have", guess, "guesses left.")
        print("Availiable letters:", get_availiable_letters(letters_guessed))
        # Input the characters here
        user_input = input("Please guess a letter: ")
        if (str.isalpha(user_input)):   # is a valid character
            user_input = str.lower(user_input)
            if (user_input not in letters_guessed and user_input in secret_word):
                letters_guessed.extend([user_input])
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            elif (user_input not in letters_guessed and user_input not in secret_word):
                letters_guessed.extend([user_input])
                if user_input in VOWELS:
                    guess -= 2
                else:
                    guess -= 1
                print("Oops! That letter is not my my word:", get_guessed_word(secret_word, letters_guessed))
            elif (user_input in letters_guessed):
                warnings -= 1
                guess -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings", get_guessed_word(secret_word, letters_guessed))
        else:   # not a valid character
            warnings -= 1
            guess -= 1
            print("Oops! That is not a valid letter. You have", warnings, "warnings left")
    print("-------------")
    if (guess == 0 or warnings == 0):
        print("Sorry, you ran out of guesses. The word was", secret_word)
    else:
        print("Congratilations, you won!")
        print("Your total score for this game is: ", (guess + 1) * len(secret_word))

# Ths hinted version of the game
def hangman_with_hints(secret_word):
    guess = 6               # initial guesses
    warnings = 3            # initial warnings
    letters_guessed = []    # a list to store all the guessed letters
    print("Welcome to the game of hangman!")
    print("I am thinking of a word that is", len(secret_word), "long")
    print("You have", warnings, "warnings left.")
    while (not is_word_guessed(secret_word, letters_guessed) and warnings > 0 and guess > 0):
        print("-------------")
        print("You have", guess, "guesses left.")
        print("Availiable letters:", get_availiable_letters(letters_guessed))
        # Input the characters here
        user_input = input("Please guess a letter: ")
        if (user_input == "*"):
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
        elif (str.isalpha(user_input)):   # is a valid character
            user_input = str.lower(user_input)
            if (user_input not in letters_guessed and user_input in secret_word):
                letters_guessed.extend([user_input])
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            elif (user_input not in letters_guessed and user_input not in secret_word):
                letters_guessed.extend([user_input])
                if user_input in VOWELS:
                    guess -= 2
                else:
                    guess -= 1
                print("Oops! That letter is not my my word:", get_guessed_word(secret_word, letters_guessed))
            elif (user_input in letters_guessed):
                warnings -= 1
                guess -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings", get_guessed_word(secret_word, letters_guessed))
        else:   # not a valid character
            warnings -= 1
            guess -= 1
            print("Oops! That is not a valid letter. You have", warnings, "warnings left")
    print("-------------")
    if (guess == 0 or warnings == 0):
        print("Sorry, you ran out of guesses. The word was", secret_word)
    else:
        print("Congratilations, you won!")
        print("Your total score for this game is: ", (guess + 1) * len(secret_word))

##########################################################

# main

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    # secret_word = "airplane"
    # hangman(secret_word)
    hangman_with_hints(secret_word)