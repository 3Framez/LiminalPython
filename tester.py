hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





wordList = [
    "apple", "river", "cloud", "music", "light",
    "forest", "dream", "stone", "ocean", "fire",
    "wind", "shadow", "star", "path", "echo",
    "flame", "leaf", "moon", "rain", "sky"]

# randomLetter = input("Enter letter: ")

#step 1 pick a random word

import random
from random import randint

randomWordIdx = random.randint(0, len(wordList) -1)
randomWord = wordList[randomWordIdx]
print(randomWord)





#step 2 get blank spaces the length of the chosen random word

blankContainer = ''
for i in range(len(randomWord)):
        i = '_'
        blankContainer += i
print(blankContainer)

        # step 3 convert blankcontainer into a list. because strings are immutable
blankList = list(blankContainer)
    # print(blankList)

    # letterPos = randomWord.index(randomLetter)  #doesn't work if letter is not found
    # print(letterPos)
# for hang in hangman:
#     pass


countHang = 0 #starts off with showing the gallow of the hangman
counter = 0
# step 6 loop after guessing a letter
# while counter <= len(randomWord): #there are 7 tries counter < 7 because counter starts at 0
# while counter <= max(len(randomWord), 7) and blankList[counter] != ['-']:
# while counter <= min(7, len(randomWord)) and blankList[counter] != ['-']:
# while counter <= len(randomWord) and blankList[counter] != ['-']:

# while counter <= min(7, len(randomWord)):
while counter <= 20: # and '-' not in blankList:
# while blankList[counter] != '-':
    randomLetter = input("Enter letter: ")

    #step 4 assign the random letter into a blenk space if it exists in the random word
    if randomLetter in randomWord :# and blankList[counter] != '':

                #step 5 get the position of the random Letter within the random word
                letterPos = randomWord.index(randomLetter)
                # print(letterPos)



                blankList[letterPos] = randomLetter
                print(blankList)

                if blankList == list(randomWord):
                    print("You guessed the word: " + randomWord)
                    break

    elif randomLetter not in randomWord and countHang < len(hangman):# and randomLetter == '':




            print("You lost a life: ")
            print(hangman[countHang])
            countHang += 1
            # break



            if countHang == len(hangman) - 1: #exits the loop || ran out of lives
                print("You ran out of lives: \n"+hangman[-1])
                break





    counter += 1


#issues and fixes
#it takes a life on every entry
#it should exit the loop if the blank spaces have all been filled
#every iteration shouldn't take a life
#words with repeating letters dont get checked apple...the next p doesnt work

