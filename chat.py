import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nYou:"

#prompt=input("輸入問題=>")

def chat_prompt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" You:", " AI:"]
    )
    print(response.choices[0].text)
chat_prompt("how are you")