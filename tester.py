#
#
#
#
# # def clear():
# #     os.system('cls' if os.name == 'nt' else 'clear')
# def clear():
#     os.system('cls')
#
# # for x in range(3):
# #     names = input('Enter a name: \n\n')
# #     os.system('cls')
# #     # clear()
#
#
import os

def clear():
    os.system('cls')

nameAndBid = {}
print('Welcome to the secret auction program.')
def request():
    name = input('What is your name?: \n\n')
    bid = int(input('What is your bid?: \n\n$'))
    nameAndBid [name] = bid  #for every name key assign a bid value, and store in the empty defined dictionary above
    os.system('cls')
    return addBids()

nameAndBid
def addBids():
    bid = input ("are there any other bidders? Type 'yes' or 'no'. \n\n").lower()
    if bid == 'yes':
        return request()
    elif bid == 'no':
        #getting the higest bid
        bidValues = nameAndBid.values() #get the values of all the bids, stored in a list
        maxBid = max(bidValues) #get the highest bid value form the list

        # getting the name of the highest bidder
        for name, height in nameAndBid.items():
            if height == maxBid:
                highestBidder = name


                return print(f'The winner is {highestBidder} with a bid of ${maxBid}')



request()
# clear()
# addBids()



# employees = {'mike': 27000, 'john': 65000, 'rebecca': 60000, 'tom': 10000}
#
# #items()/keys()/values() areexclusive to dictionaries
#
# for data in employees.items():  #items returns the key,value pair
#     print(data) #returns the key,value pair together in a tuple
#
# for data in employees.values():  #values returns the values
#     print(data)
#
# for data in employees.keys():  #keys returns the key
#     print(data)
#
# for key, value in employees.items():  #items returns the key,value pair
#     #returns the key,value pair sperately value
#     print(key)
#     print(value)



# emptyDict = {}
# for x in range(2):
#     name = input('Enter name: \n\n')
#     height = float(input('Enter height: \n\n'))
#     # emptyDict = name,height
#     # name.keys()
#     # height.values()
#     emptyDict[name] = height
#     # emptyDict += {name:height}
#     print(emptyDict)
#     # print(type(emptyDict))
#
# heightVal = emptyDict.values()
#
# print(max(heightVal))
# # print(emptyDict.get(sum(height)))
# for name, height in emptyDict.items():
#     if height == max(emptyDict.values()):
#         # print(emptyDict.keys())
#         print(name)


