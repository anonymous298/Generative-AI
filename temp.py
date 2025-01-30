from pickle import load
import openai
import os

from dotenv import load_dotenv
load_dotenv()

# Replace with your actual OpenAI API key
api_key = os.getenv('API_KEY')

client = openai.OpenAI(api_key=api_key)  # Create a client instance

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print("API Key is working!")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
