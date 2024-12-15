from os import terminal_size
import random

rangeMin = int(input("\n Enter the lower number for the range: "))
rangeMax = int(input("\n Enter the higher number for the range: "))

number = random.randint(rangeMin - 1, rangeMax + 1)
tries = 5
guesses = []
while tries > 0:
    guess = int(input(f"\n Please Guess a Number between {rangeMin} and {rangeMax} \n"))
    if guess < rangeMin or guess > rangeMax:
        print(
            "\n That number is outside of the range, please re-enter a number between {rangeMin} and {rangeMax} \n"
        )
    elif str(guess) in guesses:
        print("\n That number has already been guessed, please try again! \n")
    elif guess == number:
        print(
            f"\n Correct! Your guess {guess} was the secret number. You guessed it with {tries} tries left!"
        )
        break
    elif guess < number:
        guesses.append(str(guess))
        tries -= 1
        print(
            f"\n Your guess {guess} is below the secret number, you have {tries} tries left!"
        )
    elif guess > number:
        guesses.append(str(guess))
        tries -= 1
        print(
            f"\n Your guess {guess} is above the secret number, you have {tries} tries left!"
        )
print(f"\n Game over! The secret number was {number}")
