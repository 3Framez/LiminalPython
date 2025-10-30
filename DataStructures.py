#Lists -a collection of multiple elements. Unlike strings, They are mutable (can be changed)
myList = [3,2,4,1,5]
print(myList.index(4)) #locating the index position of a specific element
countList = myList.count(3) #number of times a specific elements occurs
print(countList) #count() returns a value, which should be captured

myList.reverse() #reverses the given order of the list
print(myList)
myList.sort() #sortd the list in order
print(myList)

# pop() returns a value so it can be captured
popped = myList.pop() #removes the last element in the list and changes the contents of the list
print(myList) #updated list
print(popped) #popped value has been captured

myList[0] = 'S' #first element at the oth index position changed
print(myList)

myList[1] = ['hello', 'bye'] #list within a list
print(myList)

#append function adds a single element to the last index position, but it returns no value, so unlike pop(), it cant be captured
myList.append("hi")
print(myList)

#slicing lists
print(myList[1][0:2])  #[identify  the 1st index position][start a 0th position: give me two elements]

listLength = len(myList)
print(listLength) #length of entire list

#merging two lists together
list1 = [1,2,3,4,5,6]
list2 = ["b","d","a","z","x"]
newList = list1 + list2
print(newList)
newList.extend([6,7]) #unlike append which puts the entire list as a single element [...,[6,7]]. extend, adds the elements 6,7 seperately into the list
print(newList)
"""
from the 2 lists above get the result: ['d','b','a',3,2,1]
"""
list1.reverse()
list2.sort()
list2.reverse()
print(list2 + list1)
# combinedList = list2 + list1
print(list2[2:5]+list1[-3:]) #start slicing from the 2nd position : include elements up to the 5th one] + [start slicing from the 3rd last element : give me the remaing elements]



list1 = [1,2,3,4,5,6]
print(list1[2:5]) #start slicing from the second index position: and give me 5 elements starting from the beginning of the list





print(" ")
#Randomisation

import random  #random library invoked when using random


import myModule
print(myModule.pi)

randomInt = random.randint(1,10) #random integers ranging from 1 to 10. random *module* . randint() *function*
print(randomInt)
randomFloat = random.random() #returns floating value from 0.0 to 1.0 (excluding 1.0)
print(randomFloat)
randomFloat = random.random() * 5 #returns floating value from 0.0 to 5.0 (excluding 5.0)
print(randomFloat)

#COIN FLIP
"""
heads = 1
tails = 0
depending on the random number, print out heads or tails
"""

randomChoice = random.randint(0,1)
print(randomChoice)
if randomChoice == 1:
    print("Heads")
else:
    print("Tails")


#PAY THE BILL
"""
iput: 4 names
output: single name...*name* is going to buy the meal today
"""
import random

#with given names
names = ["Angela", "Stacy", "Sunny", "Johnny"]
#to use randint, we need to get the first and last position of the list as integers
pos1 = names.index("Angela")   #index() gives the position as a numeric value
pos2 = len(names) - 1 #length of the list -> 4, but we have 3 index positions [0,1,2,3], so '-1' is used
randNames = random.randint(pos1,pos2) #given range
print(names[randNames]) #output names[*numeric value*] randNames represents the numeric value's index position

#input the names manually
# name = input("Enter multiple names seperated by a comma and space\n").split(", ") #.split(", ") tells the program what to plit the names with a comma and space
# print(name) #outputs the names sperated by a comma and space
# startPosition = name.index(name[0]) #index function to give the numeric value of index position '0'
# finishPosition = len(name) - 1
# randName = random.randint(startPosition, finishPosition)
# print(name[randName])


#COME BACK TO THIS SOON
# # #TREASURE MAP
# """
#
# """
# row1 = [" "," "," "] #
# row2 = [" "," "," "]
# row3 = [" "," "," "]
# map = [row1, row2, row3]
# print(map)
# value = 'x'
# # print(map)
# #column1
# map[0][0] = 'x' #column 1 row 1
# map[1][0] = 'x' #column 1 row 2
# map[2][0] = 'x' #column 1 row 3
#
# #column2
# map[0][1] = 'x'   #column 2 row 1
# map[1][1] = 'x'   #column 2 row 2
# map[2][1] = 'x'   #column 2 row 3
#
# #column3
# map[0][2] = 'x' #column 3 row 1
# map[1][2] = 'x' #column 3 row 2
# map[2][2] = 'x' #column 3 row 3
#
# position = int(input("Where do you want to put the treasure?"))
#
# if position == 11:
#
#     print(map[map.index(1)])
#
#     # print(f"{row1}\n{row2}\n{row3}")
#     # print(map[0][0])
#
#
#
# print(" ")
# print(" ")
# # row1
# map[0][0] = 'x'   #column 1 row 1
# map[0][1] = 'x'   #column 2 row 1
# map[0][2] = 'x'   #column 3 row 1
#
# # row2
# map[1][0] = 'x' #column 1 row 2
# map[1][1] = 'x' #column 2 row 2
# map[1][2] = 'x' #column 3 row 2
#
# # row3
# map[2][0] = 'x' #column 1 row 3
# map[2][1] = 'x' #column 2 row 3
# map[2][2] = 'x' #column 3 row 3
#
#
#
# print(map)
#
# print(f"{row1}\n{row2}\n{row3}")
#
# # print(len(row1))
#
# position = input("Where do you want to put the treasure?")
#
# #map[map[2]][3-2] X
# #where column and row meet
#
#





#ROCK PAPER SCISSORS

import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.  (___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.  (___)
'''

'''
rock's chances of winning 
1 > 3 == win

paper's chances of winning 
2 > 1

scissors's chances of winning 
3 > 2
'''

choices = [rock, paper, scissors]  #we turned the string to indeces, giving them a numeric value, by putting them in a list


rockNum = 0
paperNum = 1
scissorsNum = 2

computerChoice = random.randint(0,2)


userChoice = int(input("Choose a number between 0 to 2!\n"))
#MY WINS
#rock wins
if userChoice == 0 or userChoice == 1 or userChoice == 2:  #catches wrong input

    if userChoice == 0 and computerChoice == 2:
        print("You chose\n "+rock)

        print("Computer chose\n "+scissors)

        print("Win!")
    # paper win
    elif userChoice == 1 and computerChoice == 0:
        print("You chose\n "+paper)

        print("Computer chose\n "+rock)

        print("Win!")
    # scissors win
    elif userChoice == 2 and computerChoice == 1:
        print("You chose\n " +scissors)

        print("Computer chose\n " +paper)


    # MY LOSS
    if userChoice == 2 and computerChoice == 0:
        print("You chose\n " + scissors)

        print("Computer chose\n " + rock)

        print("Lose!")
    # paper win
    elif userChoice == 0 and computerChoice == 1:
        print("You chose\n " + rock)

        print("Computer chose\n " + paper)

        print("Lose!")
    # scissors win
    elif userChoice == 1 and computerChoice == 2:
        print("You chose\n " + paper)

        print("Computer chose\n " + scissors)

        print("Lose")


    elif userChoice == computerChoice:
        print(f"You chose\n {choices[userChoice]}")  #choices are [rock,paper,scissors] [0,1,2]

        print(f"computer chose\n {choices[computerChoice]}")

        print("Draw!")

else:
    print("Wrong Number! Choose either 0,1,2")

