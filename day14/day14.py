#import all modules
import random
from game_data import data

#print(data)
from art import logo,vs
#print(logo,vs)

#look for a way to print random game data
# def random_key():
    
#     list_data = []
#     for dict_item in data:
#         for key in dict_item:
#             list_data.append(dict_item)
#     random_list = random.choice(list_data)
#     print(random_list)
# random_key()
def random_choice():
    return random.choice(data)
    

###define a function to descibe how the data will be returned

def describe_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

#check followers against users guess to see if they got it right

def answer_checker(guess, follower1, follower2):
    if follower1 > follower2:
        return guess == 'a'
    else:
        return guess == 'b'
    
#define a function to play the game
def play_game():
    print(logo)
    score = 0
    
    continue_game = True
    choice_a = random_choice()
    choice_b = random_choice()
    
    while continue_game:
        choice_a = choice_b
        choice_b = random_choice()
        
        
        while choice_a == choice_b:
            choice_b = random_choice()
            
        print(f'compare A: {describe_data(choice_a)}.')
        print(vs)
        print(f'Against B: {describe_data(choice_b)}')
        guess = input('Who has the most followers? "A" or "B" ').lower()
        follower1 = choice_a['follower_count']
        follower2 = choice_b['follower_count']
        correct_ans = answer_checker(guess, follower1, follower2)
        
        print(logo)
        if correct_ans:
            score+=1
            print(f'You are correct! your current score is {score}.')
        else:
            continue_game = False
            print(f'Sorry. That was wrong. Your final score is {score}')
            
play_game()
        

    