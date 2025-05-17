import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")

# Point OpenAI client to Groq endpoint
openai.api_base = "https://api.groq.com/openai/v1"

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",  # or llama3-70b-8192, gemma-7b-it
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

print("Groq Chatbot: Hello! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Groq Chatbot: Goodbye!")
        break
    response = get_ai_response(user_input)
    print("Groq Chatbot:", response)
