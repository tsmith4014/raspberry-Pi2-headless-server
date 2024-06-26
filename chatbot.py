import json
import random

# Function to load the lookup table from a JSON file
def load_lookup_table(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to start a quiz
def start_quiz(lookup_table, num_questions):
    questions = list(lookup_table.keys())
    question_counter = 1  # Initialize the question counter
    score = 0  # Initialize the score

    for _ in range(num_questions):
        # Select a random question
        question = random.choice(questions)
        
        # Display the question with the counter instead of the question number
        print(f"Question {question_counter}:", question.split('. ', 1)[1])  # Split the question string and remove the number
        
        # Capture user's answer
        user_answer = input("Your answer (use commas to separate multiple answers, then press Enter): ").strip()
        
        # Extract the correct answer(s) from the lookup table
        correct_answer = lookup_table[question].split('. ')[0]  # Assuming the correct answer is always before the first period
        
        # Split and trim both user's and correct answers
        user_answers_set = set([answer.strip() for answer in user_answer.split(',')])
        correct_answers_set = set([answer.strip() for answer in correct_answer.split(',')])
        
        # Compare user's answers to the correct answers
        if user_answers_set == correct_answers_set:
            print("That's correct!\n")
            score += 1  # Increment score for correct answer
        else:
            print("That's incorrect.")
        
        # Show the correct answer
        print("Correct answer:", lookup_table[question].split('. ', 1)[1], "\n")  # Adjusted to show the answer text without the question number
        
        question_counter += 1  # Increment the question counter

    # Display the user's score at the end of the quiz
    print(f"Quiz completed! Your score is {score}/{num_questions}.")

# Main chatbot logic
def chatbot():
    lookup_table = load_lookup_table('./output_data_files/lookup_table.json')  # Update with the correct file path

    while True:
        user_input = input("Enter 'quiz' to start a quiz or type 'exit' to quit: ")
        
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
            print("Unrecognized command. Please enter 'quiz' to start a quiz or 'exit' to quit.")

# Run the chatbot
chatbot()


# working on this logic, currently its non-sensical to use as is and needs to be reworked
# import fuzzywuzzy
# # Function to get answer from the lookup table based on the question
# def get_answer(question, lookup_table):
#     normalized_question = question.strip().lower()
#     return lookup_table.get(normalized_question, "Sorry, I don't have an answer for that.")

# from fuzzywuzzy import process

# # Function to get answer from the lookup table based on the question
# def get_answer(question, lookup_table):
#     normalized_question = question.strip().lower()
#     best_match = process.extractOne(normalized_question, lookup_table.keys())
#     if best_match[1] < 80:  # if match quality is less than 80 out of 100
#         return "Sorry, I don't have an answer for that."
#     return lookup_table.get(best_match[0], "Sorry, I don't have an answer for that.")