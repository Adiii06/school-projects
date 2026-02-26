#!/usr/bin/env python
# coding: utf-8

# $\textbf{CS128-5L - PROGRAMMING LANGUAGES FOR DATA SCIENCE LABORATORY} \\ \texttt{2Q SY2324}$
# 
# NAME: MA. ADDINE ANNE T. CARREON
#  
# SECTION: A1

# ### Laboratory Exercise 6

# # <center> Hangman Part 2: The Game

# Now that you have built some useful functions, you can turn to implementing the function *hangman*, which takes one parameter the *secret_word* the user is to guess. Initially, you can (and should!) manually set this secret word when you run this function – this will make it easier to test your code. But in the end, you will want the computer to select this secret word at random before inviting you or some other user to play the game by running this function.
# 
# Calling the *hangman* function starts up an interactive game of Hangman between the user and the computer. In designing your code, be sure you take advantage of the three helper functions, *is_word_guessed, get_guessed_word, and get_available_letters*, that you've defined in the previous part!
# 
# Below are the game requirements broken down in different categories. Make sure your implementation fits all the requirements!
# 
# 
# Game Requirements
# 
# 
# 
# ### **A.     Game Architecture:**
# 
# 
# 
# 1.     The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in hangman.py.
# 
# 2.     Users start with 6 guesses.
# 
# 3.     At the start of the game, let the user know how many letters the computer's word contains and how many guesses s/he starts with.
# 
# 4.     The computer keeps track of all the letters the user has not guessed so far and before each turn shows the user the “remaining letters”
# 
# 
# 
# Example Game Implementation:
# 
# Loading word list from file...
# 
# 55900 words loaded.
# 
# Welcome to the game Hangman!
# 
# I am thinking of a word that is 4 letters long.
# 
# -------------
# 
# You have 6 guesses left.
# 
# Available letters: abcdefghijklmnopqrstuvwxyz
# 
# 
# 
# ### **B.     User-Computer Interaction:**
# 
# 
# The game must be interactive and flow as follows:
# 
# 
# 1.     Before each guess, you should display to the user:
# 
# a.     Remind the user of how many guesses s/he has left after each guess.
# 
# b.     all the letters the user has not yet guessed
# 
# 2.     Ask the user to supply one guess at a time. (Look at the user input requirements below to see what types of inputs you can expect from the user)
# 
# 3.     Immediately after each guess, the user should be told whether the letter is in the computer’s word.
# 
# 4.     After each guess, you should also display to the user the computer’s word, with guessed letters displayed and unguessed letters replaced with an underscore and space (_ )
# 
# 5.     At the end of the guess, print some dashes () to help separate individual guesses from each other
# 
# 
# 
# Example Game Implementation:
# 
# 
# 
# (The blue color below is only there to show you what the user typed in, as opposed to what the computer output.)
# 
# 
# 
# You have 6 guesses left.
# 
# Available letters: abcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: a
# 
# Good guess: _ a_ _
# 
# ------------
# 
# You have 6 guesses left.
# 
# Available letters: bcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: b
# 
# Oops! That letter is not in my word: _ a_ _
# 
# 
# 
# ### **C.    User Input Requirements:**
# 
# 
# 1.     You may assume that the user will only guess one character at a time, but the user can choose any number, symbol or letter. Your code should accept capital and lowercase letters as valid guesses!
# 
# 2.     If the user inputs anything besides an alphabet (symbols, numbers), tell the user that they can only input an alphabet. Because the user might do this by accident, they should get 3 warnings at the beginning of the game. Each time they enter an invalid input, or a letter they have already guessed, they should lose a warning. If the user has no warnings left and enters an invalid input, they should lose a guess.
# 
# 
# 
# Hint #1: Use calls to the input function to get the user’s guess.
# 
# a.     Check that the user input is an alphabet
# 
# b.     If the user does not input an uppercase or lowercase alphabet letter, subtract one warning or one guess.
# 
# 
# 
# Hint #2: you may find the string functions *str.isalpha(‘your string’)* and *str.lower(‘Your String’)* helpful! If you don’t know what these functions are you could try typing help(str.isalpha) or help(str.lower) in your Spyder shell to see the documentation for the functions.
# 
# 
# 
# Hint #3: Since the words in words.txt are lowercase, it might be easier to convert the user input to lowercase at all times and have your game only handle lowercase.
# 
# 
# 
# Example Game Implementation:
# 
# You have 3 warnings left.
# 
# You have 6 guesses left.
# 
# Available letters: bcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: s
# 
# Oops! That letter is not in my word: _ a_ _
# 
# ------------
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: $
# 
# Oops! That is not a valid letter. You have 2 warnings left: _ a_ _
# 
# 
# ### **D.Game Rules:**
# 
# 
# 1.     The user starts with 3 warnings.
# 
# 2.     If the user inputs anything besides an alphabet (symbols, numbers), tell the user that they can only input an alphabet.
# 
# a.     If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining warnings.
# 
# b.     If the user has no remaining warnings, they should lose one guess.
# 
# 3.     If the user inputs a letter that has already been guessed, print a message telling the user the letter has already been guessed before.
# 
# a.     If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining warnings.
# 
# b.     If the user has no warnings, they should lose one guess.
# 
# 4.     If the user inputs a letter that hasn’t been guessed before and the letter is in the secret word, the user loses no guesses.
# 
# 5.     **Consonants:** If the user inputs a consonant that hasn’t been guessed and the consonant is not in the secret word, the user loses **one** guess if it’s a consonant.
# 
# 6.     **Vowels:** If the vowel hasn’t been guessed and the vowel is not in the secret word, the user loses two guesses. Vowels are a, e, i , o, and u. y does not count as a vowel.
# 
# 
# 
# Example Implementation:
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: t
# 
# Good guess: ta_ t
# 
# ------------
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: e
# 
# Oops! That letter is not in my word: ta_ t
# 
# ------------
# 
# You have 3 guesses left.
# 
# Available letters: bcdfghijklmnopqrtuvwxyz
# 
# Please guess a letter: e
# 
# Oops! You've already guessed that letter. You now have 2 warnings:
# 
# ta_ t
# 
# 
# 
# ### **E.     Game Termination:**
# 
# 
# 
# 1.     The game should end when the user constructs the full word or runs out of guesses.
# 
# 2.     If the player runs out of guesses before completing the word, tell them they lost and reveal the word to the user when the game ends.
# 
# 3.     If the user wins, print a congratulatory message and tell the user their score.
# 
# 4.     The total score is the number of guesses_remaining once the user has guessed the secret_word times the number of unique letters in secret_word.
# 
# 
# 
# **Total score = guesses_remaining* number unique letters in secret_word**
# 
# 
# 
# Example Implementation:
# 
# You have 3 guesses left.
# 
# Available letters: bcdfghijklnopquvwxyz
# 
# Please guess a letter: c
# 
# Good guess: tact
# 
# ------------
# 
# Congratulations, you won!
# 
# Your total score for this game is: 9
# 
# 
# 
# Example Implementation:
# 
# You have 3 guesses left.
# 
# Available letters: bcdfghijklnopquvwxyz
# 
# Please guess a letter: n
# 
# Good guess: dolphin
# 
# ------------
# 
# Congratulations, you won!
# 
# Your total score for this game is: 21
# 
# 
# 
# ### **F.     General Hints:**
# 
# 
# 
# 1.     Consider writing additional helper functions if you need them.
# 
# 2.     There are four important pieces of information you may wish to store:
# 
# a.     *secret_word:* The word to guess. This is already used as the parameter name for the hangman function.
# 
# b.     *letters_guessed:* The letters that have been guessed so far. If they guess a letter that is already in letters_guessed, you should print a message telling them they've already guessed that but do not penalize them for it.
# 
# c.     *guesses_remaining:* The number of guesses the user has left. Note that in our example game, the penalty for choosing an incorrect vowel is different than the penalty for choosing an incorrect consonant.
# 
# d.     *warnings_remaining:* The number of warnings the user has left. Note that a user only loses a warning for inputting either a symbol or a letter that has already been guessed.
# 
# 
# 
# ### **G.    Example Game:**
# 
# 
# 
# Look carefully at the examples given above of running hangman, as that suggests examples of information you will want to print out after each guess of a letter.
# 
# 
# 
# **Note: Try to make your print statements as close to the example game as possible!**
# 
# 
# 
# The output of a **winning** game should look like this. (The blue color below is only there to show you what the user typed in, as opposed to what the computer output.)
# 
# 
# 
# *Loading word list from file...
# 
# 55900 words loaded.
# 
# Welcome to the game Hangman!
# 
# I am thinking of a word that is 4 letters long.
# 
# You have 3 warnings left.
# 
# -------------
# 
# You have 6 guesses left.
# 
# Available letters: abcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: a
# 
# Good guess: _ a_ _
# 
# ------------
# 
# You have 6 guesses left.
# 
# Available letters: bcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: a
# 
# Oops! You've already guessed that letter. You have 2 warnings left :
# 
# _ a_ _
# 
# ------------
# 
# You have 6 guesses left.
# 
# Available letters: bcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: s
# 
# Oops! That letter is not in my word.
# 
# Please guess a letter: _ a_ _
# 
# ------------
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: $
# 
# Oops! That is not a valid letter. You have 1 warnings left: _ a_ _
# 
# ------------
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: t
# 
# Good guess: ta_ t
# 
# ------------
# 
# You have 5 guesses left.
# 
# Available letters: bcdefghijklmnopqrtuvwxyz
# 
# Please guess a letter: e
# 
# Oops! That letter is not in my word: ta_ t
# 
# ------------
# 
# You have 3 guesses left.
# 
# Available letters: bcdfghijklmnopqrtuvwxyz
# 
# Please guess a letter: e
# 
# Oops! You've already guessed that letter. You have 0 warnings left :
# 
# ta_ t
# 
# ------------
# 
# You have 3 guesses left.
# 
# Available letters: bcdfghijklmnopqrtuvwxyz
# 
# Please guess a letter: e
# 
# Oops! You've already guessed that letter. You have no warnings lef t
# 
# so you lose one guess: ta_ t
# 
# ------------
# 
# You have 2 guesses left.
# 
# Available letters: bcdfghijklnopquvwxyz
# 
# Please guess a letter: c
# 
# Good guess: tact
# 
# ------------
# 
# Congratulations, you won!
# 
# Your total score for this game is: 6
# 
# 
# 
# And the output of a losing game should look like this...
# 
# 
# 
# Loading word list from file...
# 
# 55900 words loaded.
# 
# Welcome to the game Hangman!
# 
# I am thinking of a word that is 4 letters long
# 
# You have 3 warnings left.
# 
# -----------
# 
# You have 6 guesses left
# 
# Available Letters: abcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: a
# 
# Oops! That letter is not in my word: _ _ _ _
# 
# -----------
# 
# You have 4 guesses left
# 
# Available Letters: bcdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: b
# 
# Oops! That letter is not in my word: _ _ _ _
# 
# -----------
# 
# You have 3 guesses left
# 
# Available Letters: cdefghijklmnopqrstuvwxyz
# 
# Please guess a letter: c
# 
# Oops! That letter is not in my word: _ _ _ _
# 
# -----------
# 
# You have 2 guesses left
# 
# Available Letters: defghijklmnopqrstuvwxyz
# 
# Please guess a letter: 2
# 
# Oops! That is not a valid letter. You have 2 warnings left: _ _ _ _
# 
# You have 2 guesses left
# 
# Available Letters: defghijklmnopqrstuvwxyz
# 
# Please guess a letter: d
# 
# Oops! That letter is not in my word: _ _ _ _
# 
# -----------
# 
# You have 1 guesses left
# 
# Available Letters: efghijklmnopqrstuvwxyz
# 
# Please guess a letter: e
# 
# Good guess: e_ _ e
# 
# -----------
# 
# You have 1 guesses left
# 
# Available Letters: fghijklmnopqrstuvwxyz
# 
# Please guess a letter: f
# 
# Oops! That letter is not in my word: e_ _ e
# 
# -----------
# 
# Sorry, you ran out of guesses. The word was else.
# 
# 
# 
# Once you have completed and tested your code (where you have manually provided the “secret” word, since knowing it helps you debug your code), you may want to try running against the computer. If you scroll down to the bottom of the file we provided, you will see two commented lines underneath the text *if __name__ ==“__main__”*:
# 
# *#secret_word = choose_word(wordlist)*
# 
# *#hangman(secret_word)*
# 
# 
# 
# These lines use functions we have provided (near the top of hangman.py), which you may want to examine. Try “uncommenting” these lines, and reloading your code. This will give you a chance to try your skill against the computer, which uses our functions to load a large set of words and then pick one at random.

# In[2]:


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letter_guessed_string = ""
    for i in secret_word:
      if i in letters_guessed:
          letter_guessed_string+=i
      else:
          letter_guessed_string+="_"
    return letter_guessed_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_not_guessed = ""
    for i in alphabet:
        if i in letters_guessed:
            continue
        else:
            alphabet_not_guessed+=i
    return alphabet_not_guessed


def beautify_print_word(secret_word, word):
  for i in secret_word:
      if i in word:
          print(i.lower(), end= "")
      else:
          print("_ ", end= '')
  print()
      
    
def hangman(secret_word):
    run = True 
    guess = 6
    warnings = 3
    vowel_arr = ['a','e','i','o','u']
    choose_letter = ''
    guess_letter_arr = list()
    all_guess_arr = list()
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    while(run):
        print("-"*10)
        
        if is_word_guessed(secret_word,guess_letter_arr):
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guess * len(guess_letter_arr)}")
            break
        
        
        if guess == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word.lower()}")
            break
        
        
        print(f"You have {guess} guesses left.")
        print(f"Available letters: {get_available_letters(all_guess_arr)}")
        choose_letter = str(input("Please guess a letter:")).lower()

        
        if choose_letter not in "abcdefghijklmnopqrstuvwxyz" or len(choose_letter) != 1:
            print("Oops! That is not a valid letter.", end ='')
            if warnings <= 0:
                print(f"You have no warnings left")
                print(f"so you lose one guess:",end='')
                beautify_print_word(secret_word,guess_letter_arr)
                guess-=1
                continue
            warnings-=1
            print(f"You have {warnings} warnings left")
            continue

        if choose_letter in all_guess_arr:
            print("Oops! You've already guessed that letter.", end = '')
            if warnings <= 0:
                print(f"You have no warnings left")
                print(f"so you lose one guess:",end='')
                beautify_print_word(secret_word,guess_letter_arr)
                guess-=1
                continue
            warnings-=1
            print(f"You have {warnings} warnings left")
            beautify_print_word(secret_word,guess_letter_arr)
            continue

        if  choose_letter not in get_available_letters(get_guessed_word(secret_word,choose_letter)):
            if choose_letter not in guess_letter_arr:
                guess_letter_arr.append(choose_letter)
                all_guess_arr.append(choose_letter)
                print(f"Good guess:",end='')
                beautify_print_word(secret_word,guess_letter_arr)
                continue
        else:
            print(f"Oops! That letter is not in my word:",end='')
            beautify_print_word(secret_word,guess_letter_arr)

            all_guess_arr.append(choose_letter)
            if choose_letter in vowel_arr:
                guess-=2
            else:    
                guess-=1
            continue


if __name__ == "__main__":
    temp_word = "else"
    secret_word = choose_word(wordlist)
    hangman(temp_word)

