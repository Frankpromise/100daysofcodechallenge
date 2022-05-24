#define a function to return a random number
import random
from art import logo
print(logo)

#print(logo)

# guess_level = input("choose a dificulty. Type 'easy' or 'hard' : ")

# # def random_number(level):
# #     number = random.randint(1,100)
# #     print(f'Psst, the correct answer is {number} ')
# #     return number
    
# #random_number(level=guess)

# #defining the easy level
# def lives():
    
#     if guess_level == "easy":
#         print('You have 10 attempts remaining to guess the number')
#     elif guess_level == "hard" :
#         print('you have 5 attempts to complete this game')
    
        
# #lives()


# #define the guess function
# attempts_easy = 10
# attempts_hard = 5

# def guess(guess_number):
#     number = random.randint(1,100)
#     print(f'Psst, the correct answer is {number} ')
#     lives()
#     guessed_number = input('Make a guess: ')
#     if guess_number < number:
#         return "guess to low. Guess again"
    
    
    
    
# guess(guess_number=guess)
    

# number = random.randint(1,100)

attempts_easy = 10
attempts_hard = 5


# print(f'Psst, the correct answer is {number} ')
# guess_level = input("choose a dificulty. Type 'easy' or 'hard' : ").lower()
# guess = int(input('Make a guess: '))


# number = random.randint(1,100)
# print(f'Psst, the correct answer is {number} ')
    
    
def answer_checker(guess, answer, turns):
    """lets measure our guess against the number generated based on the level we choose"""
    
    
    if guess < answer:
        print('Too low')
        # print('Guess again')
        return turns - 1
    
    elif guess > answer:
        print('Guess too high')
        # print('Guess again')
        return turns - 1
    else:
        
        print(f'you got it! The answer is {answer}')
    
##Next is set our difficulty level
def difficulty_level():
    guess_level = input("choose a dificulty. Type 'easy' or 'hard' : ").lower()

# attempts_easy = 10
# attempts_hard = 5
# guess_level = input("choose a dificulty. Type 'easy' or 'hard' : ").lower()

    if guess_level == "easy":
        return attempts_easy
    else:
        return attempts_hard
    
#Next we set up the function to play the game

def play_game():
    print('Welcome to the Number Guessing Game')
    print('\n')
    print('I am thinking of a number beween 1 and 100')
    answer =  random.randint(1,100)
    print(f'Psst, the correct answer is {answer} ')
    
    #set turns = to difficulty
    
    turns = difficulty_level()
    
    guess = 0
    #use a while loop to allow he player guess multiple times
    
    while guess!=answer:
        print(f"You have {turns} remaining to complete this game")
        
        #now let the user guess a number
        
        guess = int(input('Make a guess: '))
        turns = answer_checker(guess, answer, turns)
        #next is to track the numbers of lives remaining
        if turns == 0:
            print(f"You have run out of guesses, you lose. The answer is {answer}")
            return
        elif guess!= answer:
            print('Guess again!')
                
play_game()
    # should_continue = False

    # while not should_continue:
    
    
    # # if guess_level == "easy":
    # #     print('You have 10 attempts to complete this game')
    # #attempts_easy -=1
    #     guess = int(input('Make a guess: '))
    #     easy(guess_number=guess)
        
            
    #     if guess < number:
            
    #         print('Too low')
    #         print(f'You have {attempts_easy} left')
    #         print('Guess again')
        
    #     elif guess > number:
    #         print('Guess too high')
    #         print(f'You have {attempts_easy} left')
    #         print('Guess again')
    #     elif guess == number:
    #         print(f'you got it! The answer is {number}')
            

    #     if attempts_easy == 0:
    #         should_continue = True
    #         print(f'You have run out of guesses, you lose. The answer is {number}')
                
    #     # if guess < number:
    #     #     print('Too low')
    #     #     print('Guess again')
    #     # elif guess > number:
    #     #     print('Guess too high')
    #     #     print('Guess again')
    #     # elif guess == number:
    #     #     print(f'you got it! The answer is {number}')
        
        
            
        
    
    
    # # if guess == "easy":
    # #     print('You have 10 attempts to complete this game')
        
    # # elif guess_level == 'hard':
    # #     print('You have 5 attempts to complete his game')



