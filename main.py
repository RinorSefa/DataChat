import openai
import os
import sys
from openai_utils import completions_with_backoff
from openai_utils import num_tokens_from_messages


# Get the value of an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')
NUM_MAX_TOKENS_PER_REQUEST = 4096

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

        num_tokens_in_contents = num_tokens_from_messages([{"role": "user",
                                                            "content": " Here is the CSV data " + contents}])
        if num_tokens_in_contents > NUM_MAX_TOKENS_PER_REQUEST:
            print('This file contains', num_tokens_in_contents, ",Max token size allowed is", NUM_MAX_TOKENS_PER_REQUEST)
            print("Please choose a file which contains less tokes(words), or truncate the file")
            print("We are working to fix this in the next version!")
            # TODO perform different optimization techniques to lower the number of tokens
            exit(1)

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

    total_num_tokens = num_tokens_from_messages(message)
    print('Number of tokens', total_num_tokens)
    print('Request will cost ', total_num_tokens * (0.0002/1000), "$")

    if total_num_tokens > NUM_MAX_TOKENS_PER_REQUEST:
        print('This request contains', total_num_tokens, ",Max token size allowed is", NUM_MAX_TOKENS_PER_REQUEST)
        print("Please choose a file/query which contains less tokes(words), or truncate the file/query")
        print("We are working to fix this in the next version!")
        # TODO perform different optimization techniques to lower the number of tokens
        exit(1)

    chat_completion = completions_with_backoff(model, message)
    print(chat_completion.choices[0].message.content)