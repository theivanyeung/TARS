import os
import openai

openai.api_key = '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'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content

while True:
    input_prompt = input("Chat: ")
    output_response = generate_response(input_prompt)
    print(output_response + "\n\n")