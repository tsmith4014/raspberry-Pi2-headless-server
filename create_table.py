import json
from pathlib import Path

# Function to extract QA pairs and convert them into a lookup table
def create_lookup_table(file_path):
    qa_text = Path(file_path).read_text()
    qa_pairs = qa_text.split('\n\n')  # Each QA pair is separated by two newlines
    lookup_table = {}

    for pair in qa_pairs: #This logic works like this: for each pair in qa_pairs, if the pair contains "Question:" and "Answer:", then split the pair into question and answer. Then, remove the "Question:" and "Answer:" strings and strip any extra whitespace. Finally, add the question as the key and the answer as the value to the lookup_table dictionary.  This deconstructs the QA pairs and creates a lookup table where the question is the key and the answer is the value.
        if "Question:" in pair and "Answer:" in pair:
            question, answer = pair.split('\nAnswer:')
            question_key = question.replace("Question: ", "").strip()
            lookup_table[question_key] = answer.strip()

    return lookup_table

# Path to the file containing QA pairs
qa_file_path = './output_data_files/qa_pairs_output.txt'  # Update with the correct file path

# Create the lookup table
lookup_table = create_lookup_table(qa_file_path)

# Save the lookup table as a JSON file
output_json_path = './output_data_files/lookup_table.json'  # Update with desired output file path
with open(output_json_path, 'w') as json_file:
    json.dump(lookup_table, json_file, indent=4)

print(f"Lookup table has been saved to {output_json_path}")