import art
print(art.logo2)

print("Welcome to the auction!")

More_people = True

auction_dictionary = {}
 
while More_people:
   
    
    name = input("What is your name?:\n").lower()
    bid = int(input("What is your bid price?:\n$"))
    
    auction_dictionary[name] = bid
    
    still_continue = input("Are there more people? Yes or no?\n").lower()
    

    if still_continue == "no":
        More_people = False
    else:
        print("\n"*100)
   
winner = max(auction_dictionary, key=auction_dictionary.get)
print(f"The winner is {winner} with a bid of ${auction_dictionary[winner]}")