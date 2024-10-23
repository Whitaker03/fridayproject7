import random

def number_guessing_game():
    # Greeting the user
    print("Welcome to the Number Guessing Game!")
    play = input("Do you want to play? (yes/no): ").strip().lower()

    if play == 'no':
        print("Maybe next time!")
        return
    elif play != 'yes':
        print("Please answer with 'yes' or 'no'.")
        return

    # Secret number between 1 and 10
    secret_number = random.randint(1, 10)

    # Loop for guessing
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            
            if guess < 1 or guess > 10:
                print("Please guess a number within the range (1-10).")
                continue

            if guess == secret_number:
                print("Congratulations! You've guessed the number!")
                break
            else:
                print("Try again!")
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

    # Farewell message
    print("Thanks for playing! Goodbye!")

# Run the number guessing game
number_guessing_game()