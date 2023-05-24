import openai
import os
import sys
from openai_utils import completions_with_backoff

# Get the value of an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Check if the file location parameter is provided
if len(sys.argv) < 2:
    print("Please provide the exact file location as a parameter.")
    print("Usage: python main.py <file_location> ")
    sys.exit(1)

# Retrieve the file location parameter
fileLocation = sys.argv[1]

try:
    # Open the file in read mode
    with open(fileLocation, 'r') as file:
        # Read the entire contents of the file
        contents = file.read()

except FileNotFoundError:
    print("Error: File not found.")
    print("Please make sure the file exists and provide the correct file location.")
    sys.exit(1)

except IOError:
    print("Error: Unable to read the file.")
    print("Please check if the file is accessible and not corrupted.")
    sys.exit(1)

while True:
    question = input("What is your question to OpenAI (type 'EXIT' to quit): ")

    if question.upper() == "EXIT":
        break

    model = "gpt-3.5-turbo"
    message = [
        {"role": "system", "content": "You will answer question regarding a CSV file content"},
        {"role": "user", "content": " Here is the CSV data " + contents},
        {"role": "user", "content": question}
    ]

    chat_completion = completions_with_backoff(model, message)
    print(chat_completion.choices[0].message.content)