
# Name: Ana Camba Gomes


import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    
    for i in secret_word:
        if i not in letters_guessed:
            return False #player has not won if the letters_guess are different from the ones in secret_word
    return True #player won
    
    

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    split_word = list(secret_word)
    guessing = ''
    for letter in split_word:
        if letter in letters_guessed:
            guessing = guessing + letter
        else:
            guessing = guessing + '*' #we add this symbol when we have not guess the word yet
    return guessing #our guessing progress is returned


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    split_alphabet = list(string.ascii_lowercase)
    remaining_alphabet = ''
    for letter in split_alphabet:
        if letter not in letters_guessed: 
            remaining_alphabet = remaining_alphabet + letter # your remaining alphabet will have everything except the letters you have guessed
    return remaining_alphabet 

def helper_function(secret_word, get_available_letters): 
        
      """
      secret_word: string, the lowercase word the user is guessing
      get_available_letters: string of available letters

      returns: string, revealed_letter that represents the letter that will help the user
      """
      choose_from = ''
      for char in secret_word:
          if char in get_available_letters:
              choose_from = choose_from + char
      new = random.randint(0, len(choose_from)-1) 
      revealed_letter = choose_from[new]  
      return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 10
    letters_guessed = ''
    vowels = 'aeiou'
    length_word = len(secret_word)
    #This section introduces the user to the game and gives the length of the word the user is guessing
    print('Welcome to Hangman!')
    print('I am thinking of a word that is', length_word, 'letters long.')
        
    
    while guesses <= 10 and guesses > 0 and has_player_won(secret_word, letters_guessed) != True : #the while runs from when the user has 10 guesses until it has 1
        print('-------')
        print(secret_word)
        print('You have',guesses,'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        users_letter = input('Please guess a letter:')
        users_letter = users_letter.lower() #allows the user to input a capital letter and turns it into a lower case so the program can run it
        
        
        if users_letter in letters_guessed: #if user already guessed the letter enter in the if statement - no guesses taken out
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
        
        elif users_letter in secret_word: # user guessed a letter in the secret word - no guesses taken out
            letters_guessed = letters_guessed + users_letter
            print('good guess:', get_word_progress(secret_word, letters_guessed))
            
        elif users_letter not in secret_word and users_letter in get_available_letters(letters_guessed):
            if users_letter in vowels: # checks for vowels inputted by user | (-2 guesses)
                letters_guessed = letters_guessed + users_letter
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
                guesses = guesses - 2   
                    
            else: # consonants | (-1 guess)
                letters_guessed = letters_guessed + users_letter
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
                guesses = guesses - 1
                
        elif users_letter not in secret_word and users_letter not in get_available_letters(letters_guessed):
            #evaluates for symbols and numbers
            if users_letter == '!': #this is the exception symbol for the help function
                if guesses >= 3: #user needs to have more than or 3 guesses to use the help function
                    revealed_letter = helper_function(secret_word, get_available_letters(letters_guessed)) #we need to save the random word as variable to use it later
                    letters_guessed = letters_guessed + revealed_letter
                    print('Letter revealed:',revealed_letter)
                    
                    print(get_word_progress(secret_word, letters_guessed))
                    guesses = guesses - 3 # in order to use the help function -3 guesses are taken from your guess count
                else:
                    print('Oops! Not enough guesses left:', get_word_progress(secret_word, letters_guessed))
                    #when user has less than 3 guesses left then helper does not run
                    
                
            else:
                letters_guessed = letters_guessed + users_letter #this evaluates for when it is a symbol except !
                print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letters_guessed))
    
    if has_player_won(secret_word, letters_guessed) == True: #when player won since the letters they guessed is the same as the letters in secret word
        unique_letters = ''
        for i in secret_word:
            if i not in unique_letters:
                unique_letters = unique_letters + i
        #we create a unique_letters variable to use it when taking the total_score
                total_score = (guesses + (4* len(unique_letters)) + (3*len(secret_word)))
        print('-------')
        print('Congratulations, you won!')
        print('Your total score for this game is:', total_score)
            
    elif guesses == 0: #player ran out of guesses before guessing the correct letter
        print('-------')
        print('Sorry, you ran out of guesses. The word was', secret_word)
            
            
      
        
        
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

