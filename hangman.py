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

randomWordIdx = random.randint(0, len(wordList) -1) #points to a random word's index position
randomWord = wordList[randomWordIdx] #assigns an index position to a random word
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




countHang = 0 #starts off with showing the gallow of the hangman
counter = 0 #starting position of the entire loop

while counter <= 20:
    randomLetter = input("Enter letter: ")

    #step 4 assign the random letter into a blenk space if it exists in the random word
    if randomLetter in randomWord :

                #step 5 get the position of the random Letter within the random word
                letterPos = randomWord.index(randomLetter) #the letter's index position within the word
                # print(letterPos)



                blankList[letterPos] = randomLetter #the letters index position within
                print(blankList)

                if blankList == list(randomWord):
                    print("You guessed the word: " + randomWord)
                    break

    #step 6 catch when the random letter is not in the random word
    elif randomLetter not in randomWord and countHang < len(hangman):# every time this condition is met, you lose a life


            #gives you 6 tries
            lifeRemaining = len(hangman) - 1 - countHang
            print(f"You lost a life: {lifeRemaining} remaining")
            print(hangman[countHang])
            countHang += 1
            # break



            if countHang == len(hangman): #exits the loop || ran out of lives
                print("You ran out of lives: \n"+hangman[-1])
                break





    counter += 1


#issues and fixes
#it takes a life on every entry
#it should exit the loop if the blank spaces have all been filled
#every iteration shouldn't take a life
#words with repeating letters dont get checked apple...the next p doesnt work

