"""
Number Guessing

Author: Alan
Date: August 30th 2024

This script performs a basic number guessing game.
The user selects a difficulty, which determines the number of attempts.
"""

import random, art

# Amounts of lives per difficulty
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def select_difficulty():
    """Return the amounts of lives depending on the selected difficulty."""
    if input("Choose a difficulty! (easy/hard)\n") == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_guess(number_guess, number):
    """
    Returns True if the player guessed correctly or False if not.

    Prints a hint if user guesses incorrectly.
    """
    if number_guess > number:
        print("Too high!")
    elif number_guess < number:
        print("Too low!")
    else:
        print(f"You got it! The answer was {number}")
        return True

    return False

def number_guessing():
    """
    This simple number guessing game asks user a number for them to guess

    Prints a hint if user guesses incorrectly.
    """

    # Stores a random number which the user will guess
    number = random.randint(1, 100)

    # Initialize the is_game_over flag
    is_game_over = False

    # Prints a welcoming message to the user
    print(art.logo)
    print("Welcome to the Number Guessing Game!")

    # Gets attempts depending on user's selected difficulty
    attempts = select_difficulty()

    # Loops until the game is over
    while not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number")

        # Asks the user to guess the numer
        number_guess = int(input("Make a guess:\n"))

        # Checks the user's guess
        is_game_over = check_guess(number_guess, number)

        # Player loses an attempt
        attempts -= 1

        # Ends the game if user runs out of attempts, but they haven't guessed the number
        if not is_game_over and attempts == 0:
            print(f"You've ran out of guesses! The number was {number}")
            is_game_over = True

number_guessing()
