import os
import random

playing = True

def guess(x):
  os.system("cls") # Windows
  print('\n**************************************************************')      
  print("\t\tWelcome to the number guessing game!")
  print(f'\t\tGuess a number between 1 and {x} ')  
  print('**************************************************************\n')      
  random_number = random.randint(1, x)
  guess = 0
  guess_count = 0
  
  while guess != random_number:
    guess_count += 1
    guess = int(input('Your Guess? '))
    if guess < random_number:
      print('\nSorry, guess again. Too low.')
    elif guess > random_number:
      print('\nSorry, guess again. Too high.')
  print('\n**************************************************************')      
  print(f'\tYay, congrats. You have guessed the number {random_number} correctly!!')
  print(f'\tIt took you {guess_count} attempts to guess the number correctly.')
  print('**************************************************************')      

while playing == True:
  guess(10)
  continue_playing = int(input('\nWant to continue playing? \n1. Yes \n2. No '))
  if continue_playing == 1:
    playing = True  
  else:
    playing = False

  