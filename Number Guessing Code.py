# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:32:34 2026

@author: obong
"""
import random

# Generate a random number
number_to_guess = random.randint(1, 100)

# Loop
while True:
     
# Ask the user to make a guess
 try:
  guess = int( input('Guess the number between 1 and 100: '))

# If number < guess
  if guess < number_to_guess:

     #    Print too low 
     print('Too low')
     
# If number > guess
  elif guess > number_to_guess:

#    Print too high
     print('Too high')

# Else
  else:
     
#   Print well done
     print('Congratulations! You guessed the number')
     break
 
#    Print an error
 except ValueError: 
    
# If not a valid number
  print('Please enter a valid number')







