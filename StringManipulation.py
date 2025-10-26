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




