####-------------------------####
# this program runs a slilent auction#
# Creator: Charlotte Cordwell
# Created 4/02/19
#

def get_float(prompt): #gets a float for anything
    choice = -1
    while choice ==-1:
        try:
            choice = float(input("What is your bid?"))
        except ValueError:
            print("Please put in a real number greater than -1.")
    return choice

#initalize variables/lists

highestBid = 0
bidCount = 0
name = ""

bids= []
names= []

#main routine

reservePrice = get_float("What is the reserve price?",)

while name.upper()!= 'F': #.upper changes everything uppercase, so 'f' works.
    print("To finish the acution input an 'F' into name")
    if highestBid== 0:
        print("There are no bids so far.")
    else:
        print('Highest bid so far is',highestBid)

    name = input('What is your name?')
    names.append(name)

    if name.upper()!= 'F':
        bid = get_float("What is your bid?")

        if bid > highestBid:
            highestBid = bid;
            bids.append(bid)
            bidCount += 1
        else:
            print('Sorry',name,'You will need to make another, higher bid')

if highestBid >= reservePrice:
    print('Auction won.', names[bidCount-1],'at', bids[bidCount- 1])
else:
    print('Auction did not meet reserve price')

for i in range (bidCount):
    print('Bidder:',names[i],'Bid:', bids[i])


        
