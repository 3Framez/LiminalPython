





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


