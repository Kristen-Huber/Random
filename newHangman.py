def hangman(secretWord):
    def getAvailableLetters(lettersGuessed):
        count=0
        length=len(lettersGuessed)
        while length>count:
            if lettersGuessed[count] in lettersLeft:
                lettersLeft=lettersLeft.replace(lettersGuessed[count], ' ')
                count+=1
        
    def getGuessedWord(secretWord, lettersGuessed):
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
    
    def isWordGuessed(secretWord, lettersGuessed):
        count=0
        length=len(secretWord)
        while count<length:
            if secretWord[count] in lettersGuessed:
                count+=1
                if count==length:
                    return True
            else:
                return False
    
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
    lettersGuessed=" "
    mistakesMade=0
    availableLetters="abcdefghijklmnopqrstuvwxyz"
    guess=""
    guessInLowerCase = guess.lower()
    lettersLeft=""
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord)) + " letters long."
    while mistakesMade < 9:
        print "You have " + str(8-mistakesMade)+ "guesses left."
        print "Available letters: "+ getAvailableLetters(lettersGuessed)
        print "Please guess a letter: "+ raw_input(guess)
       
        guess=raw_input("Please guess a letter: ")
        lettersGuessed+=guessInLowerCase
       
        if guessInLowerCase in availableLetters:
            if guessInLowerCase in secretWord:
                print "Good guess: " + isWordGuessed(secretWord,lettersGuessed)
                isWordGuessed(secretWord,lettersGuessed)
                return bool
                if bool==True:
                    mistakesMade=9
                    print "Congratulations, you won!"    
            else:
                print "Oops! That letter is not in my word."
                mistakesMade+=1
        elif guessInLowerCase in lettersGuessed:
            print "Oops! You've already guessed that letter: "+ guessedWord(secretWord)
        else:
            print "That is not a valid character. Please try again."
    print "Sorry, you ran out of guesses. The word was "+ secretWord
    
hangman("apple")