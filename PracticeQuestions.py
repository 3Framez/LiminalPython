"""
Generate a random password of length 8 using:
letters, numbers, and symbols
"""
import random

# letters  = input("Enter some letters: \n")
# numbers  = input("Enter some numbers: \n")
# symbols  = input("Enter some symbols: \n")

letters  = input("Enter some letters: \n")
letterLength = len(letters)  #gets the total length of letters being entered
for x in range(0,3):  #iterates 3 times
    randLetter = random.randint(1,letterLength - 1)  #the 1st iteration it selects a random letter, and reiterates to get another random
    print(letters[randLetter] ) #as it iterates three times


numbers  = input("Enter some numbers: \n")
numLength = len(numbers) #prevents index out of range, and gets length of all numbers
for x in range(0,3):
    randNum = random.randint(1,numLength - 1)  #iterates thrice and each time, gets a different random number
    print(randnumbers[randNum]) #select a random letter from the given string, then iterate 2 more times and repeat


symbols  = input("Enter some symbols: \n")
symbolLength = len(symbols) #prevents index out of range and gets entire length of symbols
for x in range(0,2): #2 iterations
    randSymbol = random.randint(1,symbolLength - 1) #iterates twice, and each time gets a different random number
    print(symbols[randSymbol]) #based on 2 iterations, it prints 2 symbols with differnt index positions

print("Your random password is :")
print(letters[randLetter]+numbers[randNum]+symbols[randSymbol])


print("--------------------")
"""
Create a list of 5 fruits and print a random choice.
"""
import random


fruits = input("Enter fruits: \n").split()

fruitLength = len(fruits) #to prevent errors like index out of range, we get the length of the entire list
randNum = random.randint(1,fruitLength -1) #lenght of list - 1 = index positions
print(fruits[randNum])



print("------------------------")
"""
Generate a random number between 1 and 10 and ask the user to guess it.
"""
import random

randNum = random.randint(1,3)

# for x in range(1):
guess = int(input("Enter guess: "))
print(guess)
if guess == randNum:
    print("You guessed correctly!")
else:
    print("Try again")



print("------------------")
"""
Print only the numbers between 1–100 that are divisible by both 3 and 7.
"""
for num in range(1,100):
    if num % 3 == 0 and num % 7 == 0:
        print(num)




print("------------------")
"""
Print all numbers from 1 to 50 but skip numbers divisible by 4 (continue).
"""
for num in range(1,50):
    if num > 0 and num % 4 != 0: #it iterates and when it gets to 4's it skips and checks the condition below, then reiterates again
        print(num)
    if num % 4 == 0:
        print("continue")

print("-------------------")
"""
Ask for a number and print its multiplication table from 1 to 10.
"""
num = int(input("Enter number: \n"))

for x in range(1,10):
   print(num * x)




print("---------------------")
"""
Print numbers from 100 down to 1 using range with a negative step.
"""
for num in range(100,0,-1): #to use a negative step, the start has to be the biggest (100) and the end has to be the smallest
    print(num)



print("------------------")
"""
Print all multiples of 5 from 1 to 100.
"""
for num in range(0,101,5):
    print(num)





print("-----------------")
"""
Given a dictionary of items and prices, ask the user for an item and print its price.
If not found, print "Item not available".
"""
person = {"name": "John", "age": 25, "city": "Toronto"}
print(person["name"]) #gives the value john
print(person.values())

diction = {} #empty storage

for x in range(3):  #iterate 3 times
    item = input("Enter an item: \n")
    price = input("Enter its price: \n")
    diction[item] = price #assign a value to a key
print(diction)
print(diction.keys())
print(diction.items())
request = input("What item do you want?\n ") #request a key
if request in diction.keys(): #if the request is present in the keys then...
    print("The item is "+request+" and its price is "+diction[request]) #request, represents the key/item, diction[] retrieves the value of the specified item
else:
    print("Item not found!")



print("------------------")
"""
Count how many times each word appears:
"""

dicto = {}  #empty dictionary to store the key value pair
words = ["hi", "hello", "hi", "bye", "hello", "hi"]

for word in words:  #iterate through the list
    countWord = words.count(word) #counting the occurence of each word in the words list, and
    #print(countWord) #shows the number of occurence of a word in relation to their position in the list
    dicto[word] = countWord #assigning a value to a key, for every iteration of a word within the list
print(dicto) #prints the entire dictionary

print("------------------")
"""
Ask the user for three fruits and their prices. Store them in a dictionary, then print it.
"""
fp = {} #empty dictionary to store these key value pairs
for x in range(3):  #iterates thrice to give you three entries of a fruit and its price
    fruits = input("Enter a fruit: \n")
    prices = input("Enter its price:\n")
    fp[fruits] = prices  #with each iteration, it assigns a value to a key
print(fp)





print("--------------------")
"""
Update the age to 26 and add "country": "Canada".
"""
person = {"name": "John", "age": 25, "city": "Toronto"}
person['age'] = 26
person['country'] = 'Canada'
print(person)


print("---------------------")
"""
Create a dictionary of 3 students and their scores. Print only the students who scored above 80.
"""
dict1 = {"student1": 90 , "student2": 70 , "student3": 81}
print(dict1.items()) #items() a method used with dictionaires to return the key and value pairs together

for key, value in dict1.items():  #for x, y in dictionary.items()
    if value > 80:
        print(key, value)

print("----------------")
"""
Count how many times 20 appears in the tuple.
"""
t = (10, 20, 30, 20, 40)
print(t.count(20))



print("---------------------")
"""
Create a tuple of 5 numbers and print:
First element
Last element
Length of the tuple
"""
myTuple = (1,2,3,4,5)
print(myTuple[0])
print(myTuple[-1])
print(len(myTuple))


print("--------------------")
"""
Ask the user for 5 names, store them in a list, then print only names longer than 4 characters.
"""
names = input("Enter 5 names:\n ").split()
for name in names:
    if len(name) > 4:
        print(name)



print("----------------------")
"""
Insert "yellow" at index 1 and delete "blue".
"""
colors = ["red", "blue", "green"]
colors[1] = 'yellow'
print(colors)


print("-------------------")
"""
Ask the user for 5 numbers and store them in a list. Then print:
The list sorted
The max number
The min number
"""
numbers = input("Enter 5 numbers: ").split()
numbers.sort()
print(numbers)
print(max(numbers))
print(min(numbers))

#max without max function
maxNum = 0
for num in numbers:
    numInt = int(num)
    if numInt > maxNum:
        maxNum = numInt
print(maxNum)

#min without min function
minNum = int(numbers[0])  #minNum = 0 cant be, because 0 is ultimately the lowest number
for num in numbers:
    numInt = int(num)
    if numInt < minNum:
        minNum = numInt
print(minNum)



print("---------------------")
"""
Ask for 3 numbers and print the largest
"""
nums = input("Enter 5 numbers: ").split()

# numbers = []
# numInt = nums
num = 0  #starting position
for x in nums:
    intX = int(x)
    if intX > num:
        num = intX #iterate through, and if you find a bigger number replace it with the current one
print(num)

print("---------------------")
"""
Ask the user for two numbers and print:
Sum
Difference
Product
Quotient
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(sum([num1,num2]))
print(num1-num2)
print(num1*num2)
print(num1**num2)



print("---------------------")
"""
Ask the user for a month and print how many days it has (February = 28).
"""
month = input("Enter month: ")

if month in ["January", "March", "May", "July", "August", "October", "November", "December"]:
    print("31 days")
elif month in ["April", "June", "September"]:
    print("30 days")
elif month in ["February"]:
    print("28 days")

print("---------------------")
"""
Ask for a number and print whether it is even, odd, or divisible by 5 (nested conditions).
"""
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("This number is even")
    if number % 5 == 0:
        print("This number is divisible by 5")
elif number % 2 != 0:
    print("This number is odd")
    if number % 5 == 0:
        print("This number is divisible by 5")


print("---------------------")
"""
Ask the user for an integer and check if it’s positive, negative, or zero.
"""
number = int(input("Enter an integer: "))
if number > 0:
    print(f"The number {number} is positive")
elif number < 0:
    print(f"The number {number} is negative")
elif number == 0:
    print(f"The number {number} is zero")



print("---------------------")
"""
Ask the user for their score (0–100) and print:
"A" for 90+
"B" for 80–89
"C" for 70–79
"D" for 60–69
"F" for below 60
"""
score = int(input("What is your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score < 60:
    print("F")

print("---------------------")
"""
Write a program that prints the sum of all integers from 1 to 100.
"""
numRange = range(0,101)
startNum = 0
for num in numRange:
    startNum += num
print(startNum)




print("---------------------")
"""
Given a list of numbers, print only those that are greater than 10.
"""
number = input("Enter a list of numbers: ").split()  # put numbers in a list
print(number)

for num in number:      #num (type string) number (type list)
    intNum = int(num)   #convert num to type int
    if intNum > 10:
        print(intNum)

print("---------------------")
"""
Ask the user for a word and print each letter on a new line.
"""
word = input("Enter a word: ")
for w in word:
    print(w)


print("---------------------")
"""
Print all even numbers between 1 and 30 using a for loop and range().
"""

evenNum = range(0,31,2)
for num in evenNum:
    print(num)



print("---------------------")
"""
Write a program that prints all numbers from 1 to 50 using a for loop.
"""
numbers = range(1, 51)
for num in numbers:
    print(num)

print("---------------------")
"""
Merge two dictionaries into one.
"""
#key["letter"] = "a"

collection1 = {}
collection2 = {}

key1 = input("Enter the keys pair of first dictionary: ").split(" ")
value1 = input("Enter the values of the first dictionary: ").split(" ")




newCollection = collection1 + collection2


"""
Write a program that counts how many times each word appears in this list:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

"""
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
#SIMPLE
apple = words.count("apple")
print(f"apple ocurs {apple} times")
banana = words.count("banana")
print(f"banana ocurs {banana} times")
orange = words.count("orange")
print(f"orange ocurs {orange} times")
#COMPLEX





print("----------------------------")
"""
Create a dictionary with keys: name, age, city. Print each key and value.

Add a new key "email" to the dictionary.

Update the value of "city" to "Toronto".
"""
person = {"name": "Ephraim", "age": 28, "city": "Calgary"}
print(person)
person["email"] = "email.com"
print(person)
person["city"] = "Toronto"
print(person)

print("----------------------------")
"""
Ask for a sentence and print how many words it contains (use .split()).
"""
sentence = input("Enter sentence\n").split(" ")
countOfWords = len(sentence)
print(countOfWords)



print("----------------------------")
""" ***
Given "Hello World", print only the vowels.
"""
word = "hello world"
newWord = word[1]+word[4]+word[7]
print(newWord)

print("----------------------------")
"""
Replace all spaces in a string with underscores (_).
"""
word = "hello all how are you"
newWord = word.replace(" ","_") #replace(old,new)
print(newWord)



print("----------------------------")
"""
Reverse a string without using slicing.
"""
word = "hello world"
wordList = list(word)
wordList.reverse()
newWord = "".join(wordList)  #join() method is used to combine all the elements into a single string ; "seperator".join(list)
print(newWord)

print("----------------------------")
"""
Check if a string starts with "Py" and ends with "on".
"""
word = input("Enter a string: ")

if word[0:2] == "Py" and word[-2:]:
    print(f"The word '{word}' starts with '{word[0:2]}' and ends with '{word[-2:]}' ")


print("----------------------------")
"""
Write a program that counts how many times the letter "a" appears in a string.
"""
word = input("Enter word: ")
print(f"a appears in {word}, {word.count('a')} times")


print("----------------------------")


"""
Ask the user for their full name and print it in title case (each word capitalized).
"""
name = input("Enter full name\n")
print(name.upper())

print("----------------------------")

"""
Find the index position of a specific element in a tuple.
"""
tuples = ('a','b','c','d')
indexNumber = tuples.index('c')
print(indexNumber)

"""
Create two tuples and concatenate them.
"""
tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
print(tuple1 + tuple2)

print("----------------------------")
"""
Write a program to check if a given value exists inside a tuple.
"""
value = input("Enter elements: ").split(" ")
tupleValue = tuple(value)
print(tupleValue)

element = input("Enter value you want to check: ")

if tupleValue.count(element) >= 1:  #count the number of times 'element' occurs in 'tupleValue'
    print(f"{element} exists in {tupleValue}")
else:
    print("Doesn't exist")



print("----------------------------")
"""
Given a tuple (5, 10, 15, 20, 25), 
convert it to a list, 
change the middle element to 100, 
and convert it back to a tuple.
"""

myTuple  = (5, 10, 15, 20, 25)
myList = list(myTuple)
myList[2] = 100
newTuple = tuple(myList)
print(newTuple)


print("----------------------------")
"""
Create a tuple with 5 elements and print the second and last elements.
"""
#SIMPLE
myTuple = ("h","i",4,6,8)
print(myTuple[1], myTuple[4])
#COMPLEX
myElements = input("Enter a number of elements: ").split(" ")
myTuple = tuple(myElements)
print(myTuple)
lengthOfTuple = len(myTuple)
print(myTuple[1], myTuple[lengthOfTuple - 1])






print("----------------------------")
"""
Write a program that removes all duplicate elements from a list.
"""
elements = input("Enter numbers with duplicates: ").split(" ")
print(elements)
uniqueElements = set(elements)  #set function identifies unique elements in an unordered way
print(f"Unique elements: {uniqueElements}")



print("----------------------------")
"""
Sort a list of integers in descending order and print the result.
"""
numbers = input("Enter a bunch of numbers to be sorted: ").split(" ")
print(numbers)
numbers.sort() #sorts numbers from small to large
numbers.reverse() #largest first smalesst last
print(numbers)




print("----------------------------")
"""
Given fruits = ["apple", "banana", "cherry", "apple"], count how many times "apple" appears.
"""

fruits = ["apple", "banana", "cherry", "apple"]
numOfApples = fruits.count("apple")
print(numOfApples)


print("----------------------------")
"""
Sort a list of integers in descending order and print the result.
"""

"""
Write a program that asks for 5 names and stores them in a list. Then print only those names that start with "A".
"""
# for loop
#ifelse .count()

#
# names = input("Enter 5 names seperated by a comma and space: ").split(", ")
# print(names)
# name1 = names[0][0]
# name2 = names[1][0]
# name3 = names[2][0]
# name4 = names[3][0]
# name5 = names[4][0]
#
# print(name1, name2)
# print(name1.count("A"))
#
# # if name1 == "A" or name2 == "A"
# # print(names)
#
# if name1.count("A") == 1 or name2.count("A") == 1:
#     print(names.startswith("A"))




print("----------------------------")
"""
Replace the last element of any list with "Python".
"""


elements = input("Enter elements within a list followed by a comma and space: ").split(", ") # split() method to show the what seperates each element, and store the contents in a list

lengthOfList = len(listOfElements) #to get the total length count of 'elements'
print(f"original list: {listOfElements}")
listOfElements[lengthOfList - 1] = "Python" #referncing the last element of the entire list
print(f"final list: {listOfElements}")


print("----------------------------")
"""
Given numbers = [10, 20, 30, 40, 50], insert 25 between 20 and 30.
"""
numbers = [10, 20, 30, 40, 50]
num1 = numbers[0:2]
num2 = numbers[2:]
num1.append(25)
print(num1 + num2)
numbers.insert(2,25)  #using the insert method. insert 25 at the second index position
print(numbers)


print("----------------------------")
"""
Create a list of 5 numbers. Print the sum, maximum, and minimum.
"""
listNumbers = [10,13,5,9,12]
num1 = listNumbers[0]
num2 = listNumbers[1]
num3 = listNumbers[2]
num4 = listNumbers[3]
num5 = listNumbers[4]

numbers = num1, num2, num3, num4, num5
print(sum(numbers))   # WRONG : listNumbers.sum() means (sum()) is a method, belonging to a list object; RIGHT: but 'sum()' is a function, so it wraps around an object
print(sum(listNumbers))
print(min(listNumbers))
print(max(listNumbers))





print("----------------------------")
"""
Write a program that checks if a number is divisible by both 3 and 5 using logical operators.
"""

divideNumber = int(input("Enter number: "))

if divideNumber % 3 == 0 and divideNumber % 5 == 0:
    print(f"{divideNumber} is divisible by 3 and 5")
else:
    print(f"{divideNumber} is NOT divisible by 3 and 5")

print("----------------------------")
"""
Ask for a password. If it’s "python123" or "PYTHON123", print “Access Granted”; otherwise “Denied”.
"""
password = input("Enter password: ")

if password == "Python123".upper() or password == "PYTHON123".lower():
    print("Access granted!")
else:
    print("Access Denied!")




print("----------------------------")
"""
Take three numbers and print the largest using if/elif/else.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number!")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest number!")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the largest number!")

print("----------------------------")
"""
Ask the user for their age — if age ≥ 18 and ≤ 65, print “Eligible for work”, otherwise “Not eligible.”
"""
age = int(input("Enter age: "))
if age >= 18 and age <= 65:
    print("Eligible for work!")
else:
    print("Not eligible!")


print("----------------------------")
"""
Write a program that checks whether a year is a leap year using one if statement.

leap year is...
1..year evenly divisible by 4
2..except year evenly divisible by 100
3..unless year is also divisible by 400
"""

year = int(input("Enter year: "))

if year % 4 == 0 or (year % 100 == 0 and year % 400 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




"""
Take a number input and print:

“Positive” if it’s > 0

“Negative” if it’s < 0

“Zero” if it’s 0

"""
import random

num = random.randint(-1,1)
# num = int(input("Enter number: "))

print(num)
print(" ")
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("----------------------------")
"""
Write a program that asks the user for a number and prints whether it’s even or odd.
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


