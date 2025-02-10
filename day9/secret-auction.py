from os import system

system('cls')

auction_bids = {}

is_other_bidders = True

while is_other_bidders:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    auction_bids[name] = price

    match input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower():
        case 'no':
            is_other_bidders = False
    system('cls')


higher_bid = ['', 0]
print(auction_bids)
for bidder in auction_bids:
    if auction_bids[bidder] > higher_bid[1]:
        higher_bid[0] = bidder
        higher_bid[1] = auction_bids[bidder]
        
print(f"The winner is {higher_bid[0]} with a bid of ${higher_bid[1]}!")