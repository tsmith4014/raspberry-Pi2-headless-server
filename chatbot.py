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
    for _ in range(num_questions):
        # Select a random question
        question = random.choice(questions)
        
        # Display the question with the counter instead of the question number
        print(f"Question {question_counter}:", question.split('. ', 1)[1])  # Split the question string and remove the number
        
        # Wait for user's answer (input is not evaluated in this version)
        input("Your answer (press Enter to reveal the correct answer): ")
        
        # Show the correct answer
        print("Correct answer:", lookup_table[question], "\n")
        
        question_counter += 1  # Increment the question counter
# def start_quiz(lookup_table, num_questions):
#     questions = list(lookup_table.keys())
#     for _ in range(num_questions):
#         # Select a random question
#         question = random.choice(questions)
#         print("Question:", question)
        
#         # Wait for user's answer (input is not evaluated in this version)
#         input("Your answer (press Enter to reveal the correct answer): ")
        
#         # Show the correct answer
#         print("Correct answer:", lookup_table[question], "\n")

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
            answer = get_answer(user_input, lookup_table)
            print(answer)

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