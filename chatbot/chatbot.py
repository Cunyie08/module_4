from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("test_api"))

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "developer", "content": "You are an assistive chatbot"},
        {"role": "user", "content": "How to make fluffy pancakes"}
        ]
)

print(response.choices[0].message.content)
