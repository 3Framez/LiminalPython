# Adding two random numbers
num = input("Enter two digit number: ") #num variable is of type string
# we subscript the num variable by seperating the number by their index position
add = int(num[0]) + int(num[1]) #typecast the num variable to a string datatype
print(add)


# BMI Calculator
height = float(input("Enter a height: ")) #typecast height from string to float
weight = int(input("Enter a weight: ")) #typecast weight from string to int
bmi = round(weight/(height**2)) #rounding to the nearest whole number
print(f"Your BMI is {bmi}")



# Your Life in weeks
age = int(input("What is your current age: "))

ageLimit = 90
months = (ageLimit * 12) - (age * 12)  # convert years left to months
weeks = (ageLimit * 52) - (age * 52)  # convert years left to months
days = (ageLimit * 365) - (age * 365) #convert years left to days

print(f"You have {months} months and {weeks} weeks and {days} days left")


# Tip calculator
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill $:" )) #total bill is float $000.00
tip = int(input("What percentage tip would you like to give? 10,12 or 15"))

percentTip = tip/100 #percentage tip equates to 0.1, 0.12, 0.15

billSplit = int(input("How many people to split the bill?"))
billOfEach = totalBill/billSplit  #each persons pay is the total bill divided by number of persons paying
tipAmount = billOfEach * percentTip #the tip amount is each persons bill * the tip percentage
finalBill = billOfEach + tipAmount #the final bill each person's bill plus the tip amount calculated
print(f"Each person should pay: ${round(finalBill,2)}") #round to 2 decimal places

