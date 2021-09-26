#################################################
# Imports
#################################################
import os
import random
from typing import List

attempts = 0
guessedLetters = []
global missingLetters
missingLetters = 0

#################################################
# Define Hangman Diagrams
#################################################
diagrams = ['''





=========''','''
      
      
      |
      |
      |
=========''','''

      |
      |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

############################################################################################################################
# Function - Category & Word Selection:
# User inputs category from displayed list, from which the chosen category file is read to find the random word / secret
############################################################################################################################
def wordSelect():
    categories = ["animals", "movies"]
    category=str(input('\n Please Select The Name of the Chosen Category: \n 1. animals \n 2. movies \n'))
    if category not in categories:
          print("\n Category Not Found - Please Try Again")
          wordSelect()
    filename="%s.txt" % category
    file=open(filename, 'r')
    m=file.readlines()
    lenghth=len(m)
    randomIndex=random.randrange(lenghth)
    word=m[randomIndex].rstrip('\n')
    file.close()
    return(word)

#################################################
# Function -  Writing Out the Guessable String
#################################################

def letterPrint(secret):
      for letter in (secret):
          if letter in guessedLetters:
            print(letter, end=' ')
          elif letter == ' ':
                print(" / ", end= ' ')
          else:
             print("_", end=' ')
             global missingLetters
             missingLetters += 1


def hangman():
      maxAttempts = len(diagrams)
      attempts=0
      secretWord = wordSelect()
      secretLength=len(secretWord)
      global guessedLetters
      guessedLetters = []
      while attempts < maxAttempts:
            global missingLetters
            missingLetters=0
            print(diagrams[attempts])
            letterPrint(secretWord)
            if missingLetters == 0:
                  print("\nyes!, you have guessed", secretWord, "correctly")   
            if attempts == len(diagrams) - 1:
                  print("\nyou lose!, the secret word was", secretWord)
            if missingLetters == 0 or attempts == maxAttempts -1:
                  print('\n Game Complete - You Can Have Anther Go or Quit:')
                  playagain = input("\n Would You Like To Play Again? y or n ") #once the user has won or lost the game, the user is to be asked if they want to play again
                  if playagain == "y":
                        hangman()
                  elif playagain == "n":
                        break #if the user enters "n" to play again, the game will end
                  elif playagain != "y" or "n":
                        print("please enter y or n")
                        continue
            
            print("\n\nguessed letters  ", guessedLetters)
            guess = input("\nguess a letter  ") #while the attempts limit hasn't been met, the user will be asked to guess a letter
            guess = guess.lower()
            if len(guess)!=1:
                  print("please enter 1 letter only")
            elif guess in guessedLetters:
                  print("you have already guessed that letter ")
            elif guess not in (secretWord): #if the user guesses a letter not in the word, the guess will be added to incorrectletters and attemtps will increase by 1
                  attempts+=1
                  print("incorrect, you have", len(diagrams)-1-attempts, "goes remaining")
            guessedLetters.append(guess)
missingLetters = 0
hangman()
