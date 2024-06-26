import re

# Open the file and read its content
with open('qa_pairs_output.txt', 'r') as file:
    content = file.read()

# Use regex to remove the number or letter after "Answer:"
# This regex matches "Answer:" followed by any number of spaces, one or more letters or digits, and a period.
modified_content = re.sub(r'Answer:\s+[A-Za-z\d]+\. ', 'Answer: ', content)

# Write the modified content back to the file
with open('qa_pairs_output_modified.txt', 'w') as file:
    file.write(modified_content)