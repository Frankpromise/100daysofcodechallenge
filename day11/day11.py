import random
from art import logo

#define a function to return a random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#deal_card()

# a function that takes a list of cards as input as returns score

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Inside calculate_score() check for an 11 (ace). 
    #If the score is already over 21, remove the 11 and replace it with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
    #Create a function called compare() and pass in the user_score and computer_score. 
    #If the computer and user both have the same score, then it's a draw. 
    # If the computer has a blackjack (0), then the user loses. 
    # If the user has a blackjack (0), then the user wins. 
    # If the user_score is over 21, then the user loses. 
    #If the computer_score is over 21, then the computer loses. 
    #If none of the above, then the player with the highest score wins

def compare(user_score, computer_score):
    if computer_score == user_score:
         return "Draw 🙃"
    elif computer_score == 0:
       return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif  computer_score > 21:
        return "opponent  went over. You win 😎"
    elif user_score > computer_score:
        return "You win 😎"
    else:
        return "you lose😭"
# deal_card()
# calculate_score()
# compare()

#create a function to play the game

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

#the game will need to be rechecked for every new card drawn
#and calculated score needs to be repeated
    while not is_game_over:
        user_score = calculate_score(user_cards)
        
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            
        #now ask the user if they want to play again
        
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                
                user_cards.append(deal_card())
            else:
                is_game_over = True

#if the user is done, it is time to allow the computer play

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
    #ask the user if they want to continue playing
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    
    play_game()