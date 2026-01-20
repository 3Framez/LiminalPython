print("Hello",1,"World",sep = ' ')  #adding delimiters


#loops

scores = [44,55,66,77,88,99,24,75,63,88,21,66]

#finding the maximum number within the list
maxNum = 0
for score in scores:
    if score > maxNum:  #anytime score is greater than maxNum, the value score becomes the new maxNum
        maxNum = score
print(maxNum)


# sum total of the entire list
sumOfScores = 0
for score in scores:
    sumOfScores += score
print(sumOfScores)

