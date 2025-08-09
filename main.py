import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess_history = []  
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            guess_history.append(guess)

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nYour Guess History:", guess_history)

# Run the game
number_guessing_game()
