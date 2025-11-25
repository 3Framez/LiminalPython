"""
Password Generator
input amount of letters you want in password
input amount of symbols you want in password
input amount of numbers you want in password


#figure out how...
...to get random letters, numbers and symbols from each list depending on the number you input.
If i ask for 4 letters, choose 4 random letters from the 'letters' list

"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#we have an empty list, and we need to put a number of letters into this list, the value of nr_letters is the number...
#...of letters we put in the list. if nr_letters = 4, we put 4 random letters in the emptylist
ChosenLetters = []
numOfTimes = range(0, nr_letters - 1) #

for letter in letters:
    ChosenLetters = letter[]
print(ChosenLetters)


#length of entire list
countOfList = 0
for num in len(letters)
    countOfList += num
print(countOfList)
    # if nr

# getletter = random.randint(0, nr_letters)