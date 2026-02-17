def encoder(message):
    pass



def request():
    # have a list of letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']







    message = input("Type your message: ")
    code = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ")
    shiftNum = int(input("Type the shift Number: "))


    if code == 'encrypt':


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

            elif newPosition >= len(letters):
                # newValue = len(letters)[0]
                # the modulo(%) remainder is the position of the new Letter when its new position > length of letters
                #zzz (25) shifted to 4 = d (4)  || 25 + 4 % 26 = 3 (c)


                    newLetterPos = newPosition % len(letters)  #17 + 9 || 19 + 9


                    shiftedLetters += letters[newLetterPos]
                    print(shiftedLetters)



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
        # decryptedMsg
            newPosition = letterPos - shiftNum
            # print("----------------------")
            # print(newPosition)

        # # for y in range(len(message)):
            shiftedLetter = letters[newPosition]
            decodedWord += shiftedLetter
        print(f"Here is the decoded result: {decodedWord}")


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

