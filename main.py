import openai
import os

# Get the value of an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)