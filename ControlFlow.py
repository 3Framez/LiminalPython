# Conditional statements


#Love language calculator
print("Welcome to the love language calculator")
name1 = input("What is your name?\n ").lower()  #lowers the caps on the name given AnGelA -> angela
name2 = input("What is their name?\n ").lower()
# word1 = ['t','r','u','e']
# word2 = ['l','o','v','e']


word1 = 'true'
word2 = 'love'

# count function use case
#name1.count(word1[0]) #counting the number of occurences the letter in the 0th position (t) in word1 occurs in name1

#letters T R U E. num of times the letters TRUE appears in the first name + num of times the letters TRUE appears in the second name
firstLetter = name1.count(word1[0]) + name2.count(word1[0])
secondLetter = name1.count(word1[1]) + name2.count(word1[1])
thirdLetter = name1.count(word1[2]) + name2.count(word1[2])
fourthLetter = name1.count(word1[3]) + name2.count(word1[3])

#letters L O V E. num of times the letters LOVE appears in the first name + num of times the letters LOVE appears in the second name
fifthLetter = name1.count(word2[0]) + name2.count(word2[0])
sixthLetter = name1.count(word2[1]) + name2.count(word2[1])
seventhLetter = name1.count(word2[2]) + name2.count(word2[2])
eigthLetter = name1.count(word2[3]) + name2.count(word2[3])

#lists the letter and the number of occurences in both the first and second name
print(f"T ocuurs in {firstLetter} times")
print(f"R ocuurs in {secondLetter} times")
print(f"U ocuurs in {thirdLetter} times")
print(f"E ocuurs in {fourthLetter} times")
totalName1 = firstLetter+secondLetter+thirdLetter+fourthLetter #adding the number of TRUE shows up together
print(f"Total = {totalName1}")

print(f"L ocuurs in {fifthLetter} times")
print(f"O ocuurs in {sixthLetter} times")
print(f"V ocuurs in {seventhLetter} times")
print(f"E ocuurs in {eigthLetter} times")
totalName2 = fifthLetter+sixthLetter+seventhLetter+eigthLetter #adding the number of times LOVE shows up
print(f"Total = {totalName2}")

print(f"Love Score = {totalName1}{totalName2}") #the total count of TRUE beside the total count of LOVE

loveScore = str(totalName1)+str(totalName2) #typecasting to string to be used as a variable in the if/else statement

if int(loveScore) > 90 or int(loveScore) < 10:
    print("Your score is "+loveScore+" and you go together like coke and mentos")
elif int(loveScore) > 40 and int(loveScore) < 50:
    print("Your score is "+loveScore+" and you are alright together")
else:
    print("Your score is "+loveScore)
# print("first name")
# trueInName1 = name1.count(word1[0])+name1.count(word1[1])+name1.count(word1[2])+name1.count(word1[3])
# print(f"letters t r u e occur in the first name {trueInName1} times")
# loveinName1 = name2.count(word2[0])+name1.count(word2[1])+name1.count(word2[2])+name1.count(word2[3])
# print(f"letters l o v e occur in the first name {loveinName1} times")
#
# print("second name")
# trueInName2 = name2.count(word1[0])+name2.count(word1[1])+name2.count(word1[2])+name2.count(word1[3])
# print(f"letters t r u e occur in the second name {trueInName2} times")
# loveInName2 = name2.count(word2[0])+name2.count(word2[1])+name2.count(word2[2])+name2.count(word2[3])
# print(f"letters l o v e occur in the second name {loveInName2} times")


#count
# word1 = 'truelove'
#
# # name1.count(word1[0]) #counting the number of occurences the letter in the 0th position (t) in word1 occurs in name1
#
# print("first name")
# wordInName1 = name1.count(word1[0])+name1.count(word1[1])+name1.count(word1[2])+name1.count(word1[3])+name1.count(word1[4])+name1.count(word1[5])+name1.count(word1[6])+name1.count(word1[7])
# print(f"letters t r u e l o v e occur in the first name {wordInName1} times")
#
# print("second name")
# wordInName2 = name2.count(word1[0])+name2.count(word1[1])+name2.count(word1[2])+name2.count(word1[3])+name2.count(word1[4])+name2.count(word1[5])+name2.count(word1[6])+name2.count(word1[7])
# print(f"letters t r u e l o v eoccur in the second name {wordInName2} times")
#
#


print("----------------------------")
#Pizza delivery price checker
"""
small pizza: $15  ; peperroni: +2
medium pizza: $20 ; peperroni: +3
large pizza: 25   ; peperroni: +3
size: L,M,S
addPepperoni: Y/N
extraCheese: +1
"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? (L,M,S): ")
price = 0
# if size == 'S' or size == 'M' or size == 'L' : if we want a catch for inputs orther than S,M,L. But further indentations on the conditional statements below is required
if size == 'S':
    price = 15
elif size == 'M':
    price = 20
elif size == 'L':
    price = 25
addPepperoni = input("Do you want pepperoni? (Y/N): ")
#pepperoni has a differnt price depending on the pizza size, so we need two seperate conditional statements
if (addPepperoni == 'Y') and (size == 'M' or size == 'L'):
    price += 3
elif (addPepperoni == 'Y') and (size == 'S'):
    price += 2
#unlike pepperoni extra cheese is the same price across all pizza slices
extraCheese = input("Do you want extra cheese? (Y/N): ")
if extraCheese == 'Y':
    price += 1

    #print(f"Your total bill is ${price}.00")  #indentation here is wrong as it makes the price exclusive to the extraCheese condition
print(f"Your total bill is ${price}.00")  #indentation here because of price increaments

# else:
#     print("Wrong input. Try again!")




print("-----------------------")
#Leap year calculator
"""
leap year is...
1..year evenly divisible by 4
2..except year evenly divisible by 100
3..unless year is also divisible by 400

TRANSLATION:
if divisible by 4 its a leap year (TRUE)
but ('but' as in an AND) if divisible by 100, its not a leap year (FALSE)
unless ('unless' as in OR) its also divisible by 400, then its a leap year (TRUE)
"""
year = int(input("Which year do you want to check?\n"))
if (year % 4  == 0 and year % 100 != 0) or (year % 400 == 0):
# if (year % 4 == 0) and (year % 100 == 0 or year % 400 == 0 ):

    print(f"{year} is a leap year ")
else:
    print(f"{year} is not a leap year")



print("------------------------")
#BMI Calculator that determines if youre overweight, underweight or the right weight. BMI = weight/height ^ 2
height = float(input("Enter height: "))
weight = int(input("Enter weight: "))
bmi = round((weight/height ** 2),1)
print(bmi)

if bmi > 35:
    print(f"Your BMI is {bmi} and you are clinically obese!")
elif (bmi > 30) and (bmi < 35):
    print(f"Your BMI is {bmi} and you are are obese!")
elif (bmi > 25) and (bmi < 30):
    print(f"Your BMI is {bmi} and you are are overweight!")
elif (bmi > 18.5) and (bmi < 25):
    print(f"Your BMI is {bmi} and you are are of normal weight!")
else:
    print(f"Your BMI is {bmi} and you are are underweight!")


#roller coaster height checker
height = int(input("What is your height?\n"))
if height >= 120:  #comparison operator {==, !=, <, >, <=, >=}
    print("...You can ride!") #indented within the conditional statement
    price = 0 #price starts at 0 and can be incremented later on
    age = int(input("How old are you?\n"))
    # further indentation meaning it only executes when height > 120
    if age > 18:
        price = 12
        print(f"Your price is ${price}")
    elif age < 12: #elif condition is used when you have multiple conditions evaluating the same variable (age)
        price = 5
        print(f"Your price is ${price}")
    else:
        price = 7
        print(f"Your price is ${price}")
    picture = input("Do you want a picture with at the end of your ride? Y/N ")
    #indentation on the same line (as the if/else condition above) because once the conditions above have finished computing, the one below comes next
    if picture == 'Y':
        #indentation (of price) on the same line as other prices because we're adding them up.
        price += 3  #price = price + 3. gives an increment of 3 on the given price
        print(f"Your total is ${price}") #indentation here as its exclusive to the picture condition due to the increament happening here
    else:
        print(f"Your total price is ${price}")
else: #if and else should be indented on the same line
    print("Sorry, you can't ride!")


print("---------------")
#ODD or EVEN number checker
num = int(input("Enter a number: "))
if num % 2 == 0: #even numbers leave no remainders
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")



