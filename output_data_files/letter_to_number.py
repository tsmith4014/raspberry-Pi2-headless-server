import re

def convert_answers(match):
    # Extract the matched answers string, excluding "Answer: "
    answers_str = match.group(0)[8:]
    # Split the answers on commas to handle multiple answers
    answers = answers_str.split(',')
    # Convert each answer to its corresponding number, stripping spaces and converting letters
    converted_answers = [str(ord(answer.strip()) - 64) if answer.strip().isalpha() else answer.strip() for answer in answers]
    # Join the converted answers back together
    return 'Answer: ' + ', '.join(converted_answers)

# Open the file and read its content
with open('qa_pairs_output_modified.txt', 'r') as file:
    content = file.read()

# Use regex to find "Answer:" followed by letters or numbers, possibly separated by commas
# This regex accounts for spaces and commas between answers
modified_content = re.sub(r'Answer: ([A-Ea-e\d],?\s?)+', convert_answers, content)

# Write the modified content back to the file
with open('qa_pairs_output_final.txt', 'w') as file:
    file.write(modified_content)