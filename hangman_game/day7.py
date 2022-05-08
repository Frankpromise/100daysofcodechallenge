
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(f'chosen word is {chosen_word}')

from hangman_art import logo
print(logo)

lives = 6
game_end = False

display = []
length_of_word = len(chosen_word)

for _ in range(length_of_word):
  display+= "_"

while not game_end:
    user_guess = input('Guess a letter. \n').lower()
    if user_guess in display:
        print(f'Your guess is {user_guess}. You already guessed this letter')
        
    for position in range(length_of_word):
      letter = chosen_word[position]

      if letter == user_guess:
        display[position] = letter

      

    if user_guess not in chosen_word:

        print(f'you guessed {user_guess}. This word is no in the chosen word. You lose a live')
        lives-=1
        if lives == 0:
          game_end = True
          print('No more lives.You lose')

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print('You have won')
      
    
     
    
    from hangman_art import stages
    print(stages[lives])










