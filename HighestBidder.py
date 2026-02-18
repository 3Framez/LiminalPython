import os

def clear():
    os.system('cls')

nameAndBid = {}
print('Welcome to the secret auction program.')
def request():
    name = input('What is your name?: \n\n')
    bid = int(input('What is your bid?: \n\n$'))
    nameAndBid [name] = bid  #for every name key assign a bid value, and store in the empty defined dictionary above
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
            if height == maxBid: # or max(nameAndBid.values()): if baxBid hadn't been calculated
                highestBidder = name


                return print(f'The winner is {highestBidder} with a bid of ${maxBid}')




request()
clear()
addBids()