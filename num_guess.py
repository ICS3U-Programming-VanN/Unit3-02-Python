#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 5, 2022
# This program asks the user to try and guess the correct number between 1-9 and
# displays a message depending on if they get it right or not


import constants


def main():
    # Asks user to guess the number
    user_guess = float(input("Guess the correct number (1-9): "))

    # IF the user guesses the number correctly
    if user_guess == constants.CORRECT_NUMBER:
        print("You guessed correctly!")

    # IF the user does not guess correctly
    else:
        print("You guessed wrong!")

    # Displays the correct number
    print(f"\nThe correct answer was {constants.CORRECT_NUMBER}")


if __name__ == "__main__":
    main()
