from art import logo
print(logo)

print("Welcome to the secret auction game")

bids= {}


def highest_bidder(bid_track):
  highest_bid = 0
  winner = ""
  for bidder in bid_track:
    bid_amount = bid_track[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, and they won with ${highest_bid}")
  


finished_bidding = False

while not finished_bidding:
  name = input("What is your name?\n").lower()
  bid = int(input("What is your bid?\n"))
  bids[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if other_bidders == "no":
    finished_bidding = True
    highest_bidder(bids)
  elif other_bidders == "yes":
    continue

