

bid_list = {}
loop_start = True

while loop_start == True:


    name = input("What is your name?\n").lower()
    price = int(input("What is your bid?\n $"))
    other_bidders = input("Are there any other bidders? Type yes or no \n").lower()
    bid_list[name] = price

    print("\n" * 20)

    print(bid_list)
    if other_bidders == "no":
        final_bid = max(bid_list, key=bid_list.get)
        print(f"The winning bidder is {final_bid} with a bid of ")


#def compare(bidding_dictionary):


        
