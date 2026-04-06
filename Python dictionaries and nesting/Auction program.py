def max_bid_amount():
    max_auction_amount = max(Bidders_list.values()) # fetching of maximum values
    winner = max(Bidders_list, key=Bidders_list.get) #fetching key of the maximum value
    print(f"The winner is {winner} with a bid of {max_auction_amount}")

print("Welcome to the auction program")
more_bidders = "yes"
Bidders_list = {}
while more_bidders == "yes":
    bidder_name = input("What is your name? ")
    auction_amount = int(input("What is the bid amount?"))
    Bidders_list[bidder_name] = auction_amount
    print(Bidders_list)
    more_bidders = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        max_bid_amount()
    elif more_bidders == "yes":
        print("\n" * 100)







