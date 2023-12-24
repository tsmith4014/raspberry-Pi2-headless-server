import re
from pathlib import Path

# Function to extract question and answer pairs from a chapter
def extract_qa_pairs(chapter_questions, chapter_answers):
    qa_pairs = {}
    question_pattern = re.compile(r'\d+\..+?(?=\n\d+\.|\Z)', re.DOTALL)
    answer_pattern = re.compile(r'\d+\..+?(?=\n\d+\.|\Z)', re.DOTALL)

    questions = question_pattern.findall(chapter_questions)
    answers = answer_pattern.findall(chapter_answers)

    for question in questions:
        question_number = question.split('.')[0].strip()
        for answer in answers:
            if answer.startswith(question_number + '.'):
                qa_pairs[question.strip()] = answer.strip()
                break
    return qa_pairs

# Read the text file content for questions and answers
questions_path = 'questions.txt'  # Update with the correct file path for questions
answers_path = 'answers.txt'  # Update with the correct file path for answers

questions_text = Path(questions_path).read_text()
answers_text = Path(answers_path).read_text()

# Split the text by chapters
chapter_questions_split = re.split(r'Chapter \d+ Review Questions', questions_text)[1:]
chapter_answers_split = re.split(r'Chapter \d+: Review Answers', answers_text)[1:]

# Debugging: Print the number of chapters found
print(f"\nNumber of question chapters: {len(chapter_questions_split)}")
print(f"Number of answer chapters: {len(chapter_answers_split)}")

# Match questions with answers for each chapter
all_qa_pairs = {}
for i, (chapter_questions, chapter_answers) in enumerate(zip(chapter_questions_split, chapter_answers_split)):
    print(f"Processing Chapter {i+1}")  # Debugging: Print current chapter being processed
    chapter_qa_pairs = extract_qa_pairs(chapter_questions, chapter_answers)
    all_qa_pairs.update(chapter_qa_pairs)

# Print first few QA pairs for review
for i, (q, a) in enumerate(all_qa_pairs.items()):
    if i < 10:  # Limit to first 10 pairs
        print(f"Question: {q}\nAnswer: {a}\n")
    else:
        break

# Write the QA pairs to a file
output_file_path = 'qa_pairs_output.txt'  # Update with desired output file path
with open(output_file_path, 'w') as file:
    for question, answer in all_qa_pairs.items():
        file.write(f"Question: {question}\nAnswer: {answer}\n\n")

print(f"Question-answer pairs have been saved to {output_file_path}")



# import re
# from pathlib import Path

# # Read the text file content for questions and answers
# questions_path = 'questions.txt'  # Update with the correct file path for questions
# answers_path = 'answers.txt'  # Update with the correct file path for answers

# questions_text = Path(questions_path).read_text()
# answers_text = Path(answers_path).read_text()

# # Define patterns to extract questions and answers
# question_pattern = re.compile(r'(\d+\..+?)(?=\n\d+\.|\nChapter|\Z)', re.DOTALL)
# answer_pattern = re.compile(r'(\d+\..+?)(?=\n\d+\.|\nChapter|\Z)', re.DOTALL)

# # Extract questions and answers
# questions = question_pattern.findall(questions_text)
# answers = answer_pattern.findall(answers_text)

# # Match questions with answers
# qa_pairs = {}
# for question in questions:
#     question_number = question.split('.')[0].strip()
#     for answer in answers:
#         if answer.startswith(question_number + '.'):
#             qa_pairs[question.strip()] = answer.strip()
#             break

# # Print first few QA pairs for review
# for i, (q, a) in enumerate(qa_pairs.items()):
#     if i < 10:  # Limit to first 10 pairs
#         print(f"Question: {q}\nAnswer: {a}\n")
#     else:
#         break

# # Write the QA pairs to a file
# output_file_path = 'qa_pairs_output.txt'  # Update with desired output file path
# with open(output_file_path, 'w') as file:
#     for question, answer in qa_pairs.items():
#         file.write(f"Question: {question}\nAnswer: {answer}\n\n")

# print(f"Question-answer pairs have been saved to {output_file_path}")




# import re
# from pathlib import Path

# # Read the text file content
# file_path = 'aws.txt'  # Update with the correct file path
# text = Path(file_path).read_text()

# # Check if the text can be split into questions and answers
# separator = "Answer Key"  # Replace this with the actual separator used in your document
# if separator in text:
#     parts = text.split(separator)
#     questions_part = parts[0]
#     answers_part = parts[1]
# else:
#     print("The separator was not found in the document.")
#     exit()

# # Define patterns for questions and answers
# question_pattern = re.compile(r'\d+\.\s[A-Z].+?\n(?:\s+\d\..+?\n)*', re.DOTALL)
# # Modified pattern to capture the full explanatory text of each answer
# answer_pattern = re.compile(r'\d+\.\s[A-Z]\..+?(?=\n\d+\.|$)', re.DOTALL)

# # Extract questions and answers
# questions = question_pattern.findall(questions_part)
# answers = answer_pattern.findall(answers_part)

# # Match questions with their answers
# qa_pairs = {}
# for question in questions:
#     question_number = question.split('.')[0].strip()
#     for answer in answers:
#         if answer.startswith(question_number + '.'):
#             qa_pairs[question.strip()] = answer.strip()
#             break

# # Write the QA pairs to a file
# output_file_path = 'output_file.txt'  # Update with desired output file path
# with open(output_file_path, 'w') as file:
#     for question, answer in qa_pairs.items():
#         file.write(f"Question: {question}\nAnswer: {answer}\n\n")

# print(f"Question-answer pairs have been saved to {output_file_path}")





# import re
# from pathlib import Path

# # Read the text file content
# file_path = 'aws.txt'  # Update with the correct file path
# text = Path(file_path).read_text()

# # Check if the text can be split into questions and answers
# separator = "Answer Key"  # Replace this with the actual separator used in your document
# if separator in text:
#     parts = text.split(separator)
#     questions_part = parts[0]
#     answers_part = parts[1]
# else:
#     print("The separator was not found in the document.")
#     exit()

# # Define patterns for questions and answers
# question_pattern = re.compile(r'\d+\.\s[A-Z].+?\n(?:\s+\d\..+?\n)+', re.DOTALL)
# answer_pattern = re.compile(r'\d+\.\s[A-Z]\..+?', re.DOTALL)

# # Extract questions and answers
# questions = question_pattern.findall(questions_part)
# answers = answer_pattern.findall(answers_part)

# # Match questions with their answers
# qa_pairs = {}
# for question in questions:
#     question_number = question.split('.')[0].strip()
#     for answer in answers:
#         if answer.startswith(question_number + '.'):
#             qa_pairs[question.strip()] = answer.strip()
#             break

# # Write the QA pairs to a file
# output_file_path = 'output_file.txt'  # Update with desired output file path
# with open(output_file_path, 'w') as file:
#     for question, answer in qa_pairs.items():
#         file.write(f"Question: {question}\nAnswer: {answer}\n\n")

# print(f"Question-answer pairs have been saved to {output_file_path}")
