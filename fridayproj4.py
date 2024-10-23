def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the smallest planet in our solar system?": "Mercury",
        "What year did the Titanic sink?": "1912",
        "What is the largest mammal in the world?": "Blue Whale"
    }

    # Loop through each question in the dictionary
    for question, answer in questions.items():
        # Display the question
        print(question)
        # Prompt the user for an answer
        user_answer = input("Your answer: ").strip()

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect! The correct answer is: {answer}\n")

    # Farewell message
    print("Thanks for playing the trivia quiz!")

# Run the trivia quiz
trivia_quiz()