import random

def generate_powerball_numbers():
    # Greeting the user
    print("Welcome to the PowerBall Number Generator!")
    print("This program will help you generate random numbers for your PowerBall ticket.\n")

    # Generating the first five white ball numbers (1-69)
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)

    # Generating the red PowerBall number (1-26)
    red_ball = random.randint(1, 26)

    # Formatting the output with the specified spaces
    ticket = f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}"

    # Printing the generated ticket
    print("Your PowerBall ticket numbers are:")
    print(ticket)

    # Farewell message
    print("\nGood luck, and may your numbers bring you fortune!")

# Run the PowerBall number generator
generate_powerball_numbers()