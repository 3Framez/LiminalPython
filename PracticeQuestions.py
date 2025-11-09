

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


