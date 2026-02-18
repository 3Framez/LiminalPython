import os

# def clear():
#     os.system('cls')

nameAndBid = {}
print('Welcome to the secret auction program.')
def request():
    '''
    DOCSTRING: it creates a dictionary with key value pairs of names and their bids
    input: name, bid
    :return: addBids() which asks the user if there are any additional bids
    '''
    name = input('What is your name?: \n')
    bid = int(input('What is your bid?: \n$'))
    nameAndBid [name] = bid  #for every name key assign a bid value, and store in the empty defined dictionary above
    os.system('cls') #clears once the name and bid are given
    return addBids()

nameAndBid
def addBids():
    '''
    DOCSTRING: asks the user if there are any more bids to be added
    input: bid
    :return: request() which asks for the name and bid of any additional bidder
    '''
    bid = input ("are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if bid == 'yes':
        return request()
    elif bid == 'no':
        #getting the higest bid
        bidValues = nameAndBid.values() #get the values of all the bids, stored in a list
        maxBid = max(bidValues) #get the highest bid value form the list

        # getting the name of the highest bidder
        for name, height in nameAndBid.items():
            if height == maxBid: # or max(nameAndBid.values()): if baxBid hadn't been calculated
                highestBidder = name #name of the bidder that has the highest bid


                return print(f'The winner is {highestBidder} with a bid of ${maxBid}')



# function calls
request() #the first function being called
# clear() # better to be defined within the request function
# addBids() #not needed to be called, because its called within the request function