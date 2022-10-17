#First-price sealed-bid auction
import art
import os
print(art.logo)
biddings = {}
more_biddings = "yes"
while more_biddings == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    biddings[name] = bid
    more_biddings = input("Are there any more bidders? Type 'yes' to add a bidding and 'no' otherwise: ").lower()
    if more_biddings == "yes":
        os.system('clear')
print(f"The winner is {max(biddings.items(), key = lambda k : k[1])[0]} with ${max(biddings.items(), key = lambda k : k[1])[1]}.")