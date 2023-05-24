import openai
import os

# Get the value of an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

while True:
    question = input("What is your question to OpenAI (type 'EXIT' to quit): ")

    if question.upper() == "EXIT":
        break

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    print(chat_completion.choices[0].message.content)