#Lists
"""
Remove all occurrences of a specific value from a list.
"""

list1 = [1,2,3,4,4,5,6,7,4,8]

countOfNum = list1.count(4)
print(countOfNum)

for x in list1:
    if x == x:




print("-------------------------------")
"""
Insert a number at index 2 of a list.
"""

numList = input("Enter 3 numbers seperatd with a space: ").split(" ")
print(numList)
numReplace = int(input("Enter a number you want to use to replace the number at the 2 index: "))
numList[2] = numReplace
print(f"Your new list including your number is: {numList}")




print("-----------------------------------")
"""
Ask the user for 5 numbers; store in a list and print the largest one (without max())
"""

numbers = input("Enter 5 numbers with a space: ").split(" ")   #puts integers within the list
# print(numbers[0]))
# numAsInt = []
if len(numbers) == 5:  #validates the list to have 5 elements/numbers
    maxNum = 0
    for n in numbers:
        nAsInt = int(n)
        if maxNum < nAsInt:
            maxNum = nAsInt
    print(maxNum)

else:
    print("You need to enter 5 numbers followed with a space")





