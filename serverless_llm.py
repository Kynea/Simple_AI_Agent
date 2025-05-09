from openai import OpenAI
import json
with open('key_ai.json') as f:
    data = json.load(f)
openai_api_key = data["openai_api_key"]
model = "gpt-4.1-2025-04-14"

client = OpenAI(
    api_key=openai_api_key
)

chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": "You are an expert who responds to the best of your ability. Limit you responses to 1000 tokens."
    }, {
        "role": "user",
        "content": "Tell me up-to-date information about income tax in Finland."
    }],
    model=model,
)

print(chat_completion)
