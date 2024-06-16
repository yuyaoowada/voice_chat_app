import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_chatgpt_response(prompt):
    """Process to receive responses to messages to ChatGPT"""
    max_tokens = 100

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": 'あなたはずんだもんです。ずんだもんのように話してください。'
                        f"話す内容は${max_tokens}文字以内に収めてください。会話の最後は質問してあげるといいと思います。"
                        'ただ、「バイバイ」と言われたら会話を終了するようにしてください。'},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
