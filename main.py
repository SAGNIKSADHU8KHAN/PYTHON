import random

def number_guessing_game():
    number_to_guess = random.randint(1,100)
    guess_history = []
    attempts = 0

print(" Welcome to number guessing game !")
print(" Guess the number between 1 to 100 ")

while True:
     try:
        guess = int(input('Enter an number'))
        attempts += 1
        guess_history.append(guess)

        if guess < number_to_guess:
            print("Too low ! Try again.")


