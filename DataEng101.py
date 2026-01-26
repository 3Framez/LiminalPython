#zip combines multiple elements into a tuple
num = [1,2,3,4,5]
word = ['a','b','c','d']
word2 = ['z','x','y','v']

for x in zip(num,word,word2): #for every iteration it combines multiple elements into a single tuple
    print(x)

#unpacking a zipped list

zippedList = list(zip(num,word,word2))

for a,b,c in zippedList:
    print(a)
    print(b)
    print(c)

print("--enumerate--")
#enumerate assigns numbers to elements in a list
for w in enumerate(word, 1):
    print(w)


print("----------------------------")
#looping through dicrtionries and tuples
employees = {'mike': 27000, 'john': 65000, 'rebecca': 60000, 'tom': 10000}

#items()/keys()/values() areexclusive to dictionaries

for data in employees.items():  #items returns the key,value pair
    print(data) #returns the key,value pair together in a tuple

for data in employees.values():  #values returns the values
    print(data)

for data in employees.keys():  #keys returns the key
    print(data)

for key, value in employees.items():  #items returns the key,value pair
    #returns the key,value pair sperately value
    print(key)
    print(value)

print("--tuples--")
employees = [('mike', 27000, 33), ('john', 65000, 36), ('rebecca', 60000, 30), ('tom', 10000, 29)]
for (k,v,a) in employees:
    print(k)
    print(v)
    print(a)



print("---------------------")
#while loop

#while some condition is true, do something, else do another thing

x = 0
while x < 10:
    #print(x) wont skip when it gets to (if x == 6: continue), as the 'continue' just redirects the flow to the start of the loop
    x += 3

    if x == 6:
        continue #it skips 6 as it is after the 'continue'
    print(x)  #prints 12, because it skips 6 and goes to 9 and restarts the loop as x is still < 10, then 9 + 3 = 12

else:
    print("x is not less than 10")






#password generator

"""
step 1: assign an index number to their respective letter
step 2: assign a range that stays in the parameters of the requested number of letters/numbers/symbols
step 3: give me a random element from the list

"""
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

idxLetters = len(letters) - 1
idxNumbers = len(numbers) - 1
idxSymbols = len(symbols) - 1

#assiging an index number to their respective letters
# randomLetter = random.randint(0, idxLetters)  #prevents index out of range error
# print(letters[randomLetter])

chosenLetters = []  #empty list to store the chosen random elements
for x in range(0, nr_letters):  #x is a placeholder for the number of times it iterates depending on nr_letters given
        randomLetter = random.randint(0, idxLetters)  # prevents index out of range error
        chosenLetters += letters[randomLetter]  #for every iteration, it adds a letter to the list
        # print(letters[randomLetter])

# chosenLetters = letters[randomLetter]
print(chosenLetters)  #the list with the random chosen letters

chosenSymbols = []
for x in range(0, nr_symbols):
    randomSymbol = random.randint(0, idxSymbols)  # a numeric value that represents a random index position within the list
    chosenSymbols += symbols[randomSymbol]  #for every iteration a randomSymbol is chosen and added to the list
    # print(symbols[randomSymbol])

print(chosenSymbols)


chosenNumbers = []
for x in range(0, nr_numbers): #iterate through a range that starts with 1 ends with the requested count of numbers
    randomNumber = random.randint(0, idxNumbers)  #selects a random numbers within the list
    chosenNumbers += numbers[randomNumber] #for every iteration a randomNumber is added to the list
    # print(numbers[randomNumber]) #prints a random number
print(chosenNumbers)



randomChar = chosenLetters + chosenSymbols + chosenNumbers
print(randomChar)

#converting the list with the selected characters to a string format
finalChar = " "  #an empty string to store the selected characters
for char in randomChar:  #iterate through the list of characters
    print(char)
    finalChar += char  #for every iteration we add a character to the empty string

print(f"Your password is: {finalChar}")  #print out the password












print("-----------------------------------")
#FizzBuzz

"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100...

But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""


for num in range(1,101):
    # print(num)
    if num % 3 == 0 and num % 5 != 0:  #num % 5 != 0 is needed to catch the condition from printing fiiz when it reaches a number like 15
        # num = fizz
        print('fizz')
    elif num % 5 == 0 and num % 3 != 0:
        print('buzz')
    elif num % 3 == 0 and num % 5 == 0:
        print('fizzBuzz')
    else:
        print(num)





print("----------------------------")
print("Hello",1,"World",sep = ' ')  #adding delimiters


#loops

scores = [44,55,66,77,88,99,24,75,63,88,21,66]

#finding the maximum number within the list
maxNum = 0
for score in scores:
    if score > maxNum:  #anytime score is greater than maxNum, the value score becomes the new maxNum
        maxNum = score
print(maxNum)


# sum total of the entire list
sumOfScores = 0
for score in scores:
    sumOfScores += score
print(sumOfScores)

