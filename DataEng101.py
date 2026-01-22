#password generator
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

idxLetters = len(letters) - 1
idxNumbers = len(numbers) - 1
idxSymbols = len(symbols) - 1

#assiging an index number to their respective letters
randomLetter = random.randint(0, idxLetters)  #prevents index out of range error
print(letters[randomLetter])

for letter in letters:
    # for letter in range(0, nr_letters):
        print(letter)

# chosenLetters = []
# for letter in letters:
#     chosenLetters += letter
# print(chosenLetters)


    # if nr_letters < idxLetters:   #if its in range




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

