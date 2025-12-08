# # To run this code you need to install the following dependencies:
# # !pip install google-genai

# import base64
# import os
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv

# load_dotenv()


# def generate(user_input):
#     client = genai.Client(
#         api_key=os.getenv("GEMINI_API_KEY"),
#     )

#     model = "gemini-flash-latest"
#     contents = [
#         types.Content(
#             role="user",
#             parts=[
#                 types.Part.from_text(text=user_input),
#             ],
#         ),
#     ]
#     generate_content_config = types.GenerateContentConfig(
#         system_instruction=[
#             types.Part.from_text(text="""1. You are expected to give simple and relatable responses.
# 2. You are an academic chatbot on healthcare
# 3. You are only expected to generate responses related to healthcare prompts.
# """),
#         ],
#     )

#     for chunk in client.models.generate_content_stream(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     ):
#         print(chunk.text, end="")

# while True:
#     user_input = input("\nUser:")
#     generate(user_input)

# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate(user_input):
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-3-pro-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        system_instruction=[
            types.Part.from_text(text="""1. You are expected to give simple and relatable responses.
2. You are an academic chatbot on healthcare
3. You are only expected to generate responses related to healthcare prompts.
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


while True:
    user_input = input("\nUser:")
    generate(user_input)

