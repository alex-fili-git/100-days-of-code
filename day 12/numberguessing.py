import art
import random

def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        return 10
    else:
        return 5

def check_guess(guess, answer, attempts):
    """Check right answer and return attempts."""
    if guess == answer:
        print(f"You got it! The answer was {answer}")
    elif guess > answer:
        print("Too high.")
        return attempts -1 
    elif guess < answer:
        print("Too low.")
        return attempts -1

def game():
    print(art.logo)
    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    attempts = set_difficulty()

    guess = 0
    while guess != number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, number, attempts)
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")

game()