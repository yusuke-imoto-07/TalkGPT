import openai
import os

openai.api_key = os.getenv('OPENAI_KEY')
#model_name = "gpt-3.5-turbo"
model_name = "gpt-4"

def get_answer(messages):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    answer = response.choices[0]["message"]["content"].strip()
    return answer
