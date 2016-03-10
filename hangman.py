secretWord='apple'



def hangman(secretWord):
    lettersGuessed=[]
    mistakesMade=0
    guess=' '
    
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
        print "Good job! The Secret Word is "+ guess
    def isWordGuessed(secretWord, lettersGuessed):
        count=0
        length=len(secretWord)
        while count<length:
            if secretWord[count] in lettersGuessed:
                return True
                getGuessedWord(secretWord, lettersGuessed)
            else:
                return False
                mistakesMade+=1
                print 'You have ' + 8-mistakesMade + 'more chances.'    
    def getAvailableLetters(lettersGuessed):
        lettersLeft='abcdefghijklmnopqrstuvwxyz'
        if guess in lettersLeft:
            lettersLeft=lettersLeft.replace(guess, ' ')
            return lettersLeft
        elif lettersGuessed in lettersGuessed:
            print "You already guessed that!"
        else:
            print"Sorry, that letter is not in the secret word"
            mistakesMade+=1
            return lettersLeft
    
    print "Welcome to Hangman!!"
    print"The Secret Word has " + str(len(secretWord))+" characters!"
    while mistakesMade<8:
        print"Please choose a letter:"
        guess=raw_input()
        lettersGuessed.append(guess)
    
        getAvailableLetters(lettersGuessed)
        isWordGuessed(secretWord, lettersGuessed)
        getGuessedWord(secretWord, lettersGuessed)
        
    
hangman('apple')