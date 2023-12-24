import json
import random

# Function to load the lookup table from a JSON file
def load_lookup_table(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to get answer from the lookup table based on the question
def get_answer(question, lookup_table):
    normalized_question = question.strip().lower()
    return lookup_table.get(normalized_question, "Sorry, I don't have an answer for that.")

# Function to start a quiz
def start_quiz(lookup_table, num_questions):
    questions = list(lookup_table.keys())
    for _ in range(num_questions):
        # Select a random question
        question = random.choice(questions)
        print("Question:", question)
        
        # Wait for user's answer (input is not evaluated in this version)
        input("Your answer (press Enter to reveal the correct answer): ")
        
        # Show the correct answer
        print("Correct answer:", lookup_table[question], "\n")

# Main chatbot logic
def chatbot():
    lookup_table = load_lookup_table('lookup_table.json')  # Update with the correct file path

    while True:
        user_input = input("Enter 'quiz' to start a quiz, ask a question about AWS, or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'quiz':
            try:
                num_questions = int(input("How many questions do you want in the quiz? "))
                start_quiz(lookup_table, num_questions)
            except ValueError:
                print("Please enter a valid number.")
        else:
            answer = get_answer(user_input, lookup_table)
            print(answer)

# Run the chatbot
chatbot()
