# AUCTION APPLICATION

import sys, subprocess

# GAVEL ASCI ART

gavel = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /         \\
                        /___________\\
                       .-------------.
                      /_______________\\
'''


print(gavel)
print("Welcome to the Blind Auction Program.")

# the dictionary to store the names and bids
bids_dic = {}

# to declare the winner
def blind_auction():
  highest_bid = 0
  winner = ""
  for bidder in bids_dic:
    current_bid = bids_dic[bidder]
    if current_bid > highest_bid:
      highest_bid = current_bid
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}! Congatulations {winner}!!")


# to create true state so that the bidding won't stop until someone enters "no"
should_continue = True

# the actual bidding process
while should_continue:
  bidder = input("Please enter your name: ")
  amount = int(input("Please enter your bid: "))
  bids_dic[bidder] = amount
  go_again = input("Is there another bidder? ")
  subprocess.run('clear')
  if go_again == "no":
    should_continue = False
    subprocess.run('clear')
    blind_auction()
    
