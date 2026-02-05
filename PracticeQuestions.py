"""
Create a method called last2 that accepts a string argument.
The method should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your method should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') - 1   hi xxhi
last2('xaxxaxaxx') -1  xa xx axaxx
last2('axxxaaxx') -2   a xx xx aa xx

take note of the last 2 characters
iterate through the characters
if an occurrence of the last 2 characters exist in the string (not counting the last 2), return the count
when iterating count first 2 characters, the next iteration, counts the second and third character
iteration 1 -> index 0, index 1
iteration 2 -> index 1, index 2
iteration 3 -> index 2, index 3
"""

# def last2(strings):
#     last2Char = strings[-2:] #start from the 2nd last position and give me the remaining characters
#     chosenCar = strings[:-2]  #evey character besides the last 2
#     for s in strings:
#
#             return strings[:-2].count(last2char) #count the number of occurence of the last 2 characters in the given string
#
#
strings = 'leleleaxagle'
last2Char = strings[-2:]
chosenChar = strings[:-2]
numOfChar = 1

# countList = 0
# for i in range(len(chosenChar)): #**
#     # strings[i:2]
#     numOfChar += 1
#     result = chosenChar[i:numOfChar]
#     # print(result)
#     countResult = result.count(last2Char)
#     print(type(countResult))
#     print(countResult)
#     countList += countResult
# print(countList)
# print("-------------------")


def last2(strings):
    countNum = 0  # where to store the final number of occurences of the last two characters
    last2Char = strings[-2:] #characters we are checking for...start from the 2nd last character and give me the remaining characters
    chosenChar = strings[:-2] #characters to iterate through...start from the 0 and omit the last two characters
    numOfChar = 1 #container for the number of characters we want to retrieve... 'hello' -> [0:numOfChar]
    for i in range(len(chosenChar)): #range that doesnt include the last two character's positions
        numOfChar += 1 #incremeants after each iteration... value is 2
        result = chosenChar[i:numOfChar] #chosenChar[0:2] -> chosenChar[1:3] -> chosenChar[2:4]...with each iteration
        countResult = result.count(last2Char) #counting the number of occurences of the last 2 characters for every iteration
        countNum += result.count(last2Char) #add up all the number of occurences
        # print(countNum)

        # continue #allows the for loop to loop again

    return countNum#.count(last2Char) #.count(last2Char)
#
print(last2('leleleaxagle'))
print(last2('axxxaaxx'))
print(last2('xaxxaxaxx'))
print(last2('hixxhi'))

# for every iteration give me 2 characters he, el, lo
# word = 'hello'
# counter = 1
# for w in range(len(word)):
#     counter += 1
      #print(word[w:2])#start from 0, give me two characters -> 'he'...start from 1 give me two characters -> e?? i can't, as im already at the second character 'e'...
#     print(word[w:counter])
#     print(word[w:counter].count('e'))
#
# lists = [1,2,3,4,1]
# print(lists.count(1))

# word = 'hello'
# print(word[:-2])


print("-------------------------------")
"""
Define a function that accepts a list as an argument
and returns True if one of the first 4 elements
in the list is a 6. The list length may be less than 4.

first3([1, 2, 6, 3, 4]) - True
first3([1, 2, 3, 4, 6]) - False
first3([1, 2, 3, 4, 5]) - False

it itrates through 4 times
checks the first element if it is a 6 print True, else iterate again
"""

def first3(listNum):
# 4 index positions, but 5 elements, so -1 stops the check of the 5th element
   # for n in range(len(listNum) - 1):  #wont work with a list of 1 because when len(listNum) is 1 (first element/index postion), 1 - 1 = 0
    for n in range(min(4, len(listNum))):  #min tells me to loop at most 4 times but no more than the length of the list
        if listNum[n] == 6: #if any of the values in the list == 6 in the given range, return True
            return True
    return False


print(first3([1, 2, 6, 3, 4]))
print(first3([1, 2, 3, 4, 6]))
print(first3([1, 2, 3, 4, 5]))
print(first3([1,3,4,6,8,8,5,3]))
print(first3([6]))
print(first3([6,3]))





print("--------------------------")
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') -'CCoCod Code' -- C Co Cod Code --repeat the first letter twice, repeat the second letter one
grow_string('abc') - 'aab abc'  -- a ab abc  #3 characters that iterates thrice
grow_string('ab') - 'a ab'  a ab
"""

#the first ieration give me one character
#the second iteration give me 2 characters
#the third iteration give me 3
#it iterates and gives characters depending on the length of the string -- ab iterates twice a ab


#the first ieration give me one character
#the second iteration give me 2 characters
#the third iteration give me 3
#grow_string('abc') - 'aab abc'  -- a ab abc  #3 characters that iterates thrice


def grow_string(strings):
    newString = ""  #to store the new string
    num = 0 #increamental counter that starts at 0

    for str in range(len(strings)):  #enables str in strings[str] to represent the index position of the value of the characters
        for num in range(len(strings)):  #an incremental value that doesn't exceed the strings length

            num += 1 #increaments depending on the string's length
            newString += strings[str:num]
            #strings[start this character: give me this number of characters]  slicing
            #strings['C':2] next iteration
        return newString #strings[str] + strings[str:2] + strings[str:3] + strings[str:4] #iteration is dependnat on the length of string

def growString(str):
    newStr = ""
    for i in range(len(str)):
        newStr += str[0:i+1]  #the first iteration str[0:position 0 = 'C' + 1 -> 'Co']
    return newStr

print(grow_string('Code'))
print(growString('Code'))


word = 'hello'
print(word[0+1])







print("-------------------------------------------------")
"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) - True
sequence([1, 1, 2, 4, 1]) - False
sequence([1, 1, 2, 1, 2, 3]) - True
sequence([1, 2]) - False
sequence([]) - False
"""

def sequence(numList):
    idxNum = len(numList)
    #iterates through the entire list and checks 3 positions
    for i in range(len(numList) - 2): #i, an integer stands for the index position within the list # -2 prevents an index out of range error because we are checking for 2 extra positions
        #numList[i] is the value 1 at index 0|| i + 1 at index position 1 || i+2 at index position 2
        if numList[i] == 1 and numList[i+1]  == 2 and numList[i+2] == 3:
        # if numList[i] == 2 and numList[i+1] == 3:
            return True
    return False

print(sequence([1, 1, 2, 3, 1]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
print(sequence([]))





print("----------------------------")
"""
Create a method called pay_Ixtra that accepts 2 parameters:
working, and hour. This method will be used to decide whether
an employee will receive extra pay or not. If an employee is working
during the hrs of 8pm until 8am in the morning, that means they
should be paid extra. In that situation the method should return true,
otherwise it should return false.

NOTE: the hour parameter should be from 0-23.
So 8AM is hour 8, and 8PM is hour 20.
hour < 8 or hour > 20

Example:
pay_extra(true, 11) -> false
pay_extra(false, 5) -> false
pay_extra(true, 6) -> true
"""
def pay_extra(working,hour):
    # return (((hour >= 20 and hour <= 23) or (hour >= 0 and hour <= 8)) and working)
    if (((hour >= 20 and hour <= 23) or (hour >= 0 and hour <= 8)) and working):
        return True
    return False

print(pay_extra(True, 11))
print(pay_extra(False, 5))
print(pay_extra(True, 6))





print("--------------------------------------")
"""
Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) - True
twelver(4, 9) - False
twelver(9, 3) - True
"""

def twelver(a,b):
    return  (a == 12 or b == 12 or a+b == 12) #instead of using an if/else condition. return the Boolean expression's result
print(twelver(12,5))
print(twelver(10,3))
print(twelver(6,6))
print(twelver(12,12))


print("---------------------------")
"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second to last item in the specific list specified by the user of the function.

Example:

For example, the below function call should return: jan

key_list_items("people", things=['book', 'tv' ], people=['pete', 'mike', 'jan', 'tom' ])

-> if you specify people, it will return jan
"""

def key_list_items(string1, **kwargs):
    value = kwargs[string1]    #key word arg[value of passed string]
    return value[-2] #within the passed string's container [go to the second to last position]

print(key_list_items( "people", things=['book', 'tv' ], people=['pete', 'mike', 'jan', 'tom' ]))


def last_lists(*args):
    return args[-1] #the value of the index position

print(last_lists([1,2,3,4,5], ['a', 'b', 'c'], ['drew', 'jake']))



print("--------------------------------------")
"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:
For example, the below function call should return ['mike', 'john' ]
last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])
"""

def last_list(*args):
    argsList = list(args)
    return argsList.pop()

print(last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john']))



print("-----------------------------------")
"""
Create a function called multi merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in the string argument
in addition to each of the characters in the string argument as individual elements in the list.

Q. nested functions
input: list([1,2,3]) , 'hello' , 'h','e','l','l','o'
output: [1,2,3,hello,'h','e','l','l','o']
"""

def multi_merge(string1, list1):

    finalStr = []
    for char in string1:
        finalStr += char
    return finalStr + string1.split() + list1

print(multi_merge('hello me', [1,2,3,4]))





print("------------------------------------")
"""
create a function called separate() that accepts a string as an argument
and returns a list containing each of the characters of
the string separated as individual items in the list.

input = hello
output = [h,e,l,l,o]
"""

#function definition that accepts a parameter
def seperates(string):
    stringsList = []
    for str in string:
        stringsList += str
    return stringsList

#funtion call that accepts an arguments
print(seperates('hello'))


#function definition that accepts no parameters
def seperate():
    stringList = []  #an empty storage container to store each characterin the list
    string = input("Enter a string: ") #asks the user to enter any string
    for str in string: #iterates through the string
        stringList += str  #adds each character within the string to a list
    return stringList  #returns the value of the once empty storage now filled with elements


#funtion call that accepts no arguments
print(seperate())




print("-----------------------------------------")
"""
Create a function named merge_lists that accepts 2 lists.
The function is supposed to merge both of those lists together
and return the result.
"""
#funtion definition with parameters
def merge_lists(list1,list2):
    return list1 + list2

#function call that takes arguments
print(merge_lists([1,2,3],['a','b','c']))


# function definition without parameters
def merge_list():
    list1 = input("Enter each elements in the first list followed by a space: ").split(" ")
    list2 = input("Enter each elements in the second list followed by a space: ").split(" ")
    return list1+list2

print(merge_list()) #function call






print("-----------------------------------------")
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
    print(numbers[randNum]) #select a random letter from the given string, then iterate 2 more times and repeat


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


