import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_chatgpt_response(prompt):
    response = client.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt
    )

    return response
