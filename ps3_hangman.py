# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=0
    length=len(secretWord)
    while count<length:
        if secretWord[count] in lettersGuessed:
            count+=1
            if count==length:
                return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    count=0
    length=len(secretWord)
    list=[]
    while count<length:
        if secretWord[count] in lettersGuessed:
            list.append(secretWord[count])
            count+=1
        else:
            list.append( '_' )
            count+=1
    guess=" ".join(list)
    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersLeft='abcdefghijklmnopqrstuvwxyz'
    count=0
    length=len(lettersGuessed)
    while length>count:
        if lettersGuessed[count] in lettersLeft:
            lettersLeft=lettersLeft.replace(lettersGuessed[count], ' ')
            count+=1
        else:
            print "You already guessed that!"
    return lettersLeft
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed=[]
    mistakesMade=0
    guessInLowerCase=" "
    remainingGuesses=8
    availableLetters="abcdefghijklmnopqrstuvwxyz"
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long"
    while remainingGuesses > 0 and isWordGuessed(secretWord,lettersGuessed)==False:
        print "-----------"
        print "You have " + str(remainingGuesses) + " guesses left"
        print "Available Letters: " + availableLetters
        guessInLowerCase=raw_input('Please guess a letter: ').lower()
        if guessInLowerCase in availableLetters:
            if guessInLowerCase in secretWord:
                lettersGuessed.append(guessInLowerCase)
                availableLetters = availableLetters.replace(str(guessInLowerCase), "")
                print "Good guess: " + str(getGuessedWord(secretWord,lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print "-----------"
                    print "Congratulations, you won!" 
                    break
            else:
                print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guessInLowerCase)
                availableLetters = availableLetters.replace(str(guessInLowerCase), "")
                mistakesMade+=1
                remainingGuesses-=1
        elif guessInLowerCase in lettersGuessed:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
        else:
            print "That is not a valid character. Please try again."
    if remainingGuesses==0:
        print "-----------"
        print "Sorry, you ran out of guesses. The word was " + str(secretWord)

secretWord=chooseWord(wordlist)
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
