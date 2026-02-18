"""
Project: Rock Paper Scissors
Course Section: 9 - Rock, Paper, Scissors
Revision: 1.3 - Final Version
Date: 2026-02-18
License: CC BY-NC-SA 4.0
"""

from random import choice

# valid_choices is a list, so it's compatible with random.choice()
valid_choices = ["rock", "paper", "scissors"]

try:
    print("--- ROCK PAPER SCISSORS: HUMAN VS CPU ---")
    
    p1 = input("Enter your move: ").lower().strip()
    
    # Works perfectly with a list too!
    if p1 not in valid_choices:
        raise ValueError(f"Invalid input: '{p1}'")

    # Now we can pass the variable directly
    computer_choice = choice(valid_choices)
    print(f"Computer chooses: {computer_choice}")

    if p1 == computer_choice:
        print("Result: It's a tie!")
    elif (p1 == "rock" and computer_choice == "scissors") or \
         (p1 == "paper" and computer_choice == "rock") or \
         (p1 == "scissors" and computer_choice == "paper"):
        print(f"Result: You win! {p1.capitalize()} beats {computer_choice}.")
    else:
        print(f"Result: Computer wins! {computer_choice.capitalize()} beats {p1}.")

except ValueError as err:
    print(f"Game Error: {err}")
except Exception:
    print("An unexpected error occurred.")

print("End of Game.")