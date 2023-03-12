#1.2.5
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("openai")

start_sequence = "\nAI:"
restart_sequence = "\nYou:"

def chat_prompt(level,prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=level,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " AI:"]
    )
    return response.choices[0].text  # type: ignore