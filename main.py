import openai
import os

# Get the value of an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

with open('data/5_spend_dataset_current.csv', 'r') as file:
    # Read the entire contents of the file
    contents = file.read()

while True:
    question = input("What is your question to OpenAI (type 'EXIT' to quit): ")

    if question.upper() == "EXIT":
        break

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will answer question regarding a CSV file content"},
            {"role": "user", "content": " Here is the CSV data " + contents},
            {"role": "user", "content": question}
        ]
    )
    print(chat_completion.choices[0].message.content)