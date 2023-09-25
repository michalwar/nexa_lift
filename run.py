import os
import openai

openai.organization = os.getenv("OPENAI_ORG_ID")


input_text = "How well you know workout plans, especially for the Olympic weightlifting?"

llm_model = "gpt-3.5-turbo"
llm_message = [{"role": "user", "content": input_text}]


response = openai.ChatCompletion.create(
    model=llm_model, messages=llm_message
)

print(response["choices"][0]["message"]["content"])