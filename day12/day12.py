#Day 12 Project - Guess The Number

from art import logo
import random

HARD_LEVEL_LIFE = 5
EASY_LEVEL_LIFE = 10

print(logo)

def check_answer(guess, answer, life) :
  if answer == guess :
    print(f"You got it! The answer was {answer}")
  else :
    if answer > guess :
      print("Too low")
    else :
      print("Too high")
    print("Guess again")
    return life - 1

def set_level() :
  level = input("Choose a difiiculty. Type 'easy' or 'hard': ")
  if level == 'hard' :
    return HARD_LEVEL_LIFE
  else :
    return EASY_LEVEL_LIFE

  
def game():
  answer = random.randint(1, 100)
  guess = 0
  life = set_level()
  
  while guess != answer and life > 0:
    print(f"You have {life} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    life = check_answer(guess, answer, life)
  
    if life == 0:
      print("You've run out of guesses. You lose")
    if guess == answer :
      print("You win")


game()

