# #the argument is added to the inputed number
# def add2(num1):
#     num2 = int(input("Enter second number: "))
#     result = num1 + num2
#     return result
#
# print(add2(3))
#
# # the argument is the one being inputed
# def power2(num):
#     num = int(input("Enter number: "))
#     result = num**2
#     return result
#
# print(power2(3))
#

def encoder(message):
    pass



def request():
    # have a list of letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # print(len(letters))


    # message = input("Type your message: ")
    #
    # shiftNum = input(int("Type the shift number"))

#identify the position of each letter within the message




# message = 'hello'

# message = 'xy'

    message = input("Type your message: ")
    code = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ")
    shiftNum = int(input("Type the shift Number: "))

# request()

    if code == 'encrypt':


    # for x in range(len(letters)):
    #     print(letters[x] + "------")  #the position of each letter within the list


    # def encrypt():
    #identify the position of the recurring letters within message
        shiftedLetters = ''
        # counter = 0
        for i in range(len(message)):
            letterPos = letters.index(message[i])  #gets the position of each of the message's character within the list of letters
            print(letterPos)


            newPosition = letterPos + shiftNum

            # shiftNum = 4
            if newPosition < len(letters):
                print(f"letter position shifted: {newPosition}")
                print(letters[newPosition]) #shifted result
                shiftedLetters += letters[newPosition]
                print(shiftedLetters)
                #whenever the new position exceeds the length of letters, the new position goes back to the start of the list

            # newPosition2 = i + shiftNum
            elif newPosition >= len(letters):
                # newValue = len(letters)[0]
                # the modulo(%) remainder is the position of the new Letter when its new position > length of letters
                #zzz (25) shifted to 4 = d (4)  || 25 + 4 % 26 = 3 (c)


                    newLetterPos = newPosition % len(letters)  #17 % 9 || 19 % 9
                # if newLetterPos == 0:
                # # if newLetterPos == 0:
                #     letters[newLetterPos] = 'a'
                # if letters[i] == 'r':
                #     newLetterPos == 0
                #     newLetterPos = newPosition % len(letters)  # 17 + 9 || 19 + 9

                # print(letters[newLetterPos])
                    shiftedLetters += letters[newLetterPos]
                    print(shiftedLetters)

                # elif newPosition == len(letters)


                    # newPosition =  letterPos - shiftNum #+ counter #-> examine
                    # print(f" negative letter position shifted: {newPosition}")
                    # print(letters[newPosition])
                    # shiftedLetters += letters[newPosition]
                    # print(f"Here is the decoded result: {shiftedLetters}")

                # counter = 0
            #if newPosition (shifted number + letter position within the list) is > len
            #then the the original letter's position becomes the sarting position of the letter's list
            # then that newPosition (26+) takes on the value of the beginning of the list of letters
            # y (23 + 3) shifted to 3 should be b || z shifted to 3 should be c || x shifted to 3 should be a
            # letterpos remains the same shiftNum remains the same but newPosition changes
            # 26 (y)

            # how to go back to the first position within a list if the length of list is exceeded

                    # [24, 25, 26, 27, 28]
            #                  [0,  1,  2]
                    #if it is 26 the value would be 0, if its 27 the value would be 1
                    #oldLetterIdx and newLetterIdx
                    #oldLetterIdx takes on the value of newLetterIdx
                    #newPosition = letters[0]
                    # print(f"newPos: {newPosition - 1}")
                    # print(f"sNum: {shiftNum}")
                    # print(f"nL: {letters[counter]}")
                    # # newPosition = letters[counter]
                    # counter += 1

                    #
                    # letterRange = range(len(letters))
                    # if x in letters > 25:
                    #     x = 0
                    # # for x in range(len(letters)):
                    # #           26      -   23
                    # newPos = newPosition - letterPos
                    # #           3
                    # print(f"----{newPos}")
                    # #       letters[2]-> c || what we want
                    # print(letters[newPos - 1])
                    # newLetters = letters[counter + shiftNum ]
                    # print(newLetters)
                    # counter += 1
                # print(letterPos)
            #         # message[newPosition] = letters[x]
            #         # newPosition = x
            #     letterPos = x
            #     print(letterPos)
                # print(f" negative letter position shifted: {newPosition}")
                # shiftedLetters += letters[counter]
                # print(shiftedLetters)
                #     counter += 1

                    #go back to the first position in letters
                    # print(newPosition)
                    # newValue = letters[x + shiftNum]
                #     newPosition = letters[x + shiftNum]
                #     print(f" negative letter position shifted: {newPosition}")
                #     print(letters[newPosition])
                # shiftedLetters += letters[newPosition]
                # print(shiftedLetters)
                # counter += 1

            # if newPosition > len(letters):
            #     newPosition = letters[x]
            #     continue
            #     newPosition = letters[countOfNew]
            #      # letters[countOfNew]
            #     print(f"{newPosition} newPosition")
            #     countOfNew += 1

        #     else:
        #     # for i in range(len(message)):
        #             print(f"letter position shifted: {newPosition}")
        #             print(letters[newPosition])
        #             shiftedLetters += letters[newPosition]
        # print(shiftedLetters)

                # continue
            # print('Here is the encoded result: '+shiftedLetters)






        # letterPos + shiftNum

    elif code == 'decrypt':

        # encrypt()
        # print(encrypt.shiftedLetters)
        #find the position of each letter in message and letters
        #find the

        #identify the position of the recurring message's letters within the list of letters
        decodedWord = ''
        for x in range(len(message)):
            letterPos = letters.index(message[x])
            print(letterPos)
            # pass


        #get the decoded result -> the new position within the letters
        # shifNum = 3
        # decryptedMsg
            newPosition = letterPos - shiftNum
            # print("----------------------")
            # print(newPosition)

        # # for y in range(len(message)):
            shiftedLetter = letters[newPosition]
            decodedWord += shiftedLetter
        print(f"Here is the decoded result: {decodedWord}")
        #
        #
        # counter = 0
        # for y in range(len(letters)):
        #
        #     # print(letters[y])
        #     letterPos = message.index(letters[counter])
        #     counter += 1
        # print(letterPos)
            # print(letterPos)
            # pass

    #depending on the shift number (1), start from each message's (a) letter...




# ...and select the letter from the list 1 shift from the message's letter ab -> bc
#let the positions reloop the list of letter z with shift of 2 -> b
#if it reaches the end of the list of letters, start from the beginning






def goAgain():
    goAgain = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")

    if goAgain == 'yes':
        return request()
        # return print("go again")
    elif goAgain == 'no':
        return print(shiftedLetters)



request()
goAgain()

