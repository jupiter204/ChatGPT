#1.4
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("openai")

start_sequence = "\nAI:"
restart_sequence = "\nYou:"

def chat_prompt(level,prompt,token):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=level,
        max_tokens=token,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " AI:"]
    )
    return response['choices'][0]['text'] # type: ignore

def image_prompt(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
    )
    return response['data'][0]['url'] # type: ignore