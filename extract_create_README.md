# AWS Quiz Lookup Table Project README

This README provides a detailed guide for the AWS Quiz Lookup Table Project. It outlines the file and process flow used to create a lookup table from a raw input document and demonstrates how this table is utilized in different applications.

## Table of Contents

- [Project Overview](#project-overview)
- [File Flow and Processing](#file-flow-and-processing)
- [Application Use Cases](#application-use-cases)
- [Setup and Execution](#setup-and-execution)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project transforms a raw text file (`aws.txt`) containing AWS certification exam questions and answers into a structured JSON lookup table (`lookup_table.json`). The resulting table is then utilized in two distinct applications: a quiz bot deployed on a Raspberry Pi and a GPT-based quiz bot that serves automated quizzes.

## File Flow and Processing

1. **Raw Input Processing**:

   - **Input File**: `aws.txt` - Contains unstructured questions and answers. This is the raw data file that is the single source of info.
   - **Output Files**: `questions.txt` and `answers.txt` - Extracted questions and answers split into two separate files. This was done manually using the aws.txt file and just copied the questions and answers into the respective files on one block each. This is the only manual processing in the project.

2. **QA Pair Extraction**:

   - **Input**: `questions.txt` and `answers.txt`.
   - **Script**: `extract.py` - Parses questions and answers to match and form QA pairs.
   - **Output**: `qa_pairs_output.txt` - Contains matched question and answer pairs.

3. **Lookup Table Creation**:
   - **Input**: `qa_pairs_output.txt`.
   - **Script**: `create_table.py` - Converts QA pairs into a JSON formatted lookup table.
   - **Output**: `lookup_table.json` - Final structured JSON file containing question-answer mappings.

## Application Use Cases

### Raspberry Pi Quiz Bot

- **Description**: A simple quiz application running on Raspberry Pi that utilizes the `lookup_table.json` to quiz users interactively.
- **File**: `chatbot.py` - Contains logic for loading the lookup table, generating quiz questions, and handling user interactions.

### GPT-based Automated Quiz Bot

- **Description**: A GPT model is trained or customized to use the `lookup_table.json` as its sole information source, providing an automated quiz experience.
- **File**: `gpt_builder_prompt.txt` - Script or instructions used to integrate the lookup table with a GPT model.

## Setup and Execution

### Initial Setup

1. Clone the project repository:

   ```bash
   git clone https://github.com/your-github-username/your-project-repository.git
   cd your-project-directory
   ```

2. Install necessary dependencies (if any).

### Running the Applications

**Raspberry Pi Quiz Bot**:

1. Ensure your Raspberry Pi device is set up and connected.
2. Run the `chatbot.py` script to start the quiz bot:
   ```bash
   python chatbot.py
   ```

**GPT-based Automated Quiz Bot**:

1. Follow the instructions in `gpt_builder_prompt.txt` to configure and launch the GPT-based bot.

## Contributing

Contributions to this project are welcome! Please refer to the project's contributing guidelines for more details on how you can contribute.

## License

This project is licensed under the MIT License. See the LICENSE file in the project directory for full details.

This README aims to streamline the understanding and operation of the AWS Quiz Lookup Table Project, ensuring clarity in the process flow from raw data to application deployment.
