# In this games, user guesses the number given by the program
import random
guessesTaken = 0
print('Hello, what is your name?')
myName = input()
number = random.randint(1, 20)
print('OK, ' + myName + ' ,I quess the number from 1 to 20')
for guessesTaken in range(6):
    print('Try to guesses.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is too small.')
    if guess > number:
        print('Your number is too big.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great, ' + myName + ' You did it for ' + guessesTaken + ' attempts!')

if guess != number:
    number = str(number)
    print('Unfortunately, I quesses a number ' + number + '.')