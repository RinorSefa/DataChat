# Project Description 

The task is to develop a Python-based solution that leverages OpenAI's language model to enable interactive conversations with SQL/tabular data or CSV files without the need to write any SQL queries. The goal is to create a user-friendly and code-free environment where users can ask questions about the data using natural language and receive accurate and explained results. The project requires integrating OpenAI's language model with Python and implementing the necessary logic to handle data retrieval and interpretation.

## Steps
 1. **Locate your API key**: Obtain the API key provided by OpenAI to authenticate your requests. If you don't have an API key, you can sign up for one on the OpenAI website.
 2. **Set the environment variable (OPENAI_API_KEY)**: Before running the main.py script, ensure that you have set the OPENAI_API_KEY environment variable to your API key. 
 3. **Install dependencies**: Install the required dependencies to run the script. Open a terminal or command prompt and navigate to the project directory. Then, run the following command to install the dependencies listed in the requirements.txt file: ``pip install -r requirements.txt``
4. **Locate the data table file** (text format, csv, txt)
4. **Usage**: Run the main.py script from the command line, providing the location of the data table file as an argument. ``python main.py <file_location>``
5. **Follow the prompts**: The main.py script will prompt you to enter your question to OpenAI. Type your question and press Enter to receive the AI-generated response based on the provided CSV data.
6. **If you want to exit the script, type 'EXIT' and press Enter.**