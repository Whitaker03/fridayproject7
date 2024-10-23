def red_text(text):
    return f"\033[91m{text}\033[0m"

def blue_text(text):
    return f"\033[94m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def brown_text(text):
    return f"\033[38;5;94m{text}\033[0m"  # Brown is approximated

def main():
    # Call each function and print out the text in the corresponding color
    print(red_text("This text is red!"))
    print(blue_text("This text is blue!"))
    print(green_text("This text is green!"))
    print(yellow_text("This text is yellow!"))
    print(brown_text("This text is brown!"))

    # User input prompt
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Display the text in the chosen color
    if color_choice == 'red':
        print(red_text(user_text))
    elif color_choice == 'blue':
        print(blue_text(user_text))
    elif color_choice == 'green':
        print(green_text(user_text))
    elif color_choice == 'yellow':
        print(yellow_text(user_text))
    elif color_choice == 'brown':
        print(brown_text(user_text))
    else:
        print("Sorry, that's not a valid color choice.")

# Run the main function
main()