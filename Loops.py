# for loops



#using for loops with the range function
for num in range(1,11, 2):  #start from 1 to 11, but skip 1 number
    print(num)
print("------------------------")




"""
print number from 1 to 100
if number % 3 == 0 -> Fizz
if number % 5 == 0 -> Buzz
if number % 3 == 0 and number % 5 -> FizzBuzz
"""

finalNum = 0
for n in range(1,101):
    if n > 0 and n % 3 != 0 and n % 5 != 0:  #if this is true, print the number but also conside the followiing conditions
        print(n)
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    elif n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")


print("------------------------")
"""
calculate all the even numbers between 0 and 100, inlcuding 100
"""
totalEvenNum = 0
for n in range(0,102,2): #start from 0 to 102, and skip a number...0 -> 2 -> 4
    totalEvenNum += n
print(totalEvenNum)
#print out entire list to make sure ther is no odd number
listOfNum = range(0,102,2)
print(list(listOfNum))



print("------------------------")
"""
add all the numbers between 0 and 100
"""
totalNum = 0
for num in range(1,101):
    totalNum += num
print(totalNum)





print("------------------------")
"""
print out the highest score in a given list of scores 
"""

student_scores = input("Enter a list of student scores\n").split(" ")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# if the current score > upcoming score, print

#Highest_score = 0
HighestScore = student_scores[0]    #assign the first element to a variable...starting position
for score in student_scores:        #evaluate each element in the list

    if score > HighestScore:        #if the current evaluated score is greater than the score at the first index position...22 > 11
        HighestScore = score        #...the current evaluated score (22) becomes the higgest score or else it remains the same

print(HighestScore)
#    highest =  max(student_scores)
# print(highest)

#the number of scores being evaluated
numOfScore = 0
for num in student_scores:
    numOfScore += 1
print(numOfScore)



print("------------------------")
"""
calculate the average height from a list of heights
"""

studentHeight = [180,124,165,173,189,169,146]
totalHeight = 0 #define total height, and set it as 0 as it increaments within the for loop
for height in studentHeight:
    totalHeight += height  #totalHeight = totalHeight + height. For every iteration, it adds the previous height to the current iterated height 0 -> 180 -> 180+124 -> ...
    avgHeight = totalHeight/len(studentHeight) #average height = sum of the iterated heights/ length of the list
print(round(avgHeight)) #a single output is needed, so its outside of the loop

#



print("-----------------------------")
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:   #for an element in list, iterate through the list and print each element
    print(fruit)
    print(fruit + " pie") #prints as many times as the iteration runs, 3 times
print(fruits) #outside the for loop so no iteration is done. only prints once

