import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей выдра голубь гусь жаба зебра змея индюк кит кобра коза козёл койот корова кошка кролик крыса курица лама лебедь лев лиса орёл панда паук питон попугай собака сова тигр тюлень утка форель хорёк черепаха ястреб'.split()

def getRandomWord(worldList):
    # This function returns a random string from given list.
    wordIndex = random.randint(0, len(worldList) - 1)
    return worldList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replaces missions letters with guesses letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret world with spaces between letters.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns letter entered by player. This function will verify that player has entered only one letter and nothing else.
        while True:
            print('Введите букву.')
            guess = input()
            guess = guess.lower()
            if len(guess) !=1:
                print('Пожалуйста, введите одну букву.')
            elif guess in alreadyGuessed:
                print('Вы уже называли эту букву. Назовите другую.')
            elif guess not in 'абвгдёежзийклмопрстуфхцчшщъьыэюя':
                print('Пожалуйста, введите букву')
            else:
                return guess

def playAgain():
    # This function returns True, if player wants play again, otherwise returns False.
    print('Хотите сыграть еще, да или нет?')



print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # The player can enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # checks whether the player won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check whether the player has exceeded attempts
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(
                len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True

        # Asks if the player wants to play again (only if the game is over).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
