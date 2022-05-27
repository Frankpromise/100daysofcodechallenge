import random
from game_data import data
from art import logo,vs

def random_choice():
    return random.choice(data)
    
    
def describe_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

def answer_checker(guess, follower1, follower2):
    if follower1 > follower2:
        return guess == 'a'
    else:
        return guess == 'b'
    
    
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
