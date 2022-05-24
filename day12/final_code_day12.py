import random
from art import logo
print(logo)

attempts_easy = 10
attempts_hard = 5

def answer_checker(guess, answer, turns):
    
    """lets measure our guess against the number generated based on the level we choose"""
    if guess < answer:
        print('Too low')
        return turns - 1
    
    elif guess > answer:
        print('Guess too high')
        return turns - 1
    else:
        
        print(f'you got it! The answer is {answer}')

def difficulty_level():
    guess_level = input("choose a dificulty. Type 'easy' or 'hard' : ").lower()
    
    if guess_level == "easy":
        return attempts_easy
    else:
        return attempts_hard


def play_game():
    print('Welcome to the Number Guessing Game')
    print('\n')
    print('I am thinking of a number beween 1 and 100')
    answer =  random.randint(1,100)
    print(f'Psst, the correct answer is {answer} ')
    
    turns = difficulty_level()
    
    guess = 0
    
    while guess!=answer:
        print(f"You have {turns} remaining to complete this game")
        guess = int(input('Make a guess: '))
        turns = answer_checker(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of guesses, you lose. The answer is {answer}")
            return
        elif guess!= answer:
            print('Guess again!')
            
play_game()
        