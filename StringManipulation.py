num = input("Enter two digit number: ") #num variable is of type string

# we subscript the num variable by seperating the number by their index position
add = int(num[0]) + int(num[1]) #typecast the num variable to a string datatype
print(add)


# BMI Calculator
height = float(input("Enter a height: ")) #typecast height from string to float
weight = int(input("Enter a weight: ")) #typecast weight from string to int
bmi = round(weight/(height**2)) #rounding to the nearest whole number
print(f"Your BMI is {bmi}")