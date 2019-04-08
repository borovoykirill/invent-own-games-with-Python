# A game where you need to guess where the cave is located with a good dragon and his treasure
import random
import time

def displayIntro():
    print('''You are in the lands inhabited by dragons. In front of you, you see two calves. 
    In one of them there is a friendly dragon, who is ready to share with you his treasures.
    In the second calve, a greedy and hungry dragon, who instantly eats you''')
    print()

def chooseCave():
    cave=''
    while cave !='1' and cave !='2':
        print('Which cave you will enter? (input 1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('Her darkness makes you afraid...')
    time.sleep(2)
    print('The dragon appears before you and opens its mouth and ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...share with you treasures!')
    else:
        print('...eat you!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print(' Do you want to play again? (input yes or not)')
    playAgain = input()