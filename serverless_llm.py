from openai import OpenAI
import json

with open('key_ai.json') as f:
    data = json.load(f)
with open('structured_output.json') as f:
    structured_output = json.load(f)
openai_api_key = data["openai_api_key"]
tools = [structured_output]
# tools = [{
#     "type": "function",
#     "name": "get_weather",
#     "description": "Get current temperature for a given location.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "location": {
#                 "type": "string",
#                 "description": "City and country e.g. Bogotá, Colombia"
#             }
#         },
#         "required": [
#             "location"
#         ],
#         "additionalProperties": False
#     }
# }]


client = OpenAI(
    api_key=openai_api_key
)
response = client.responses.create(
    model="gpt-4.1-2025-04-14",
    # input=[{"role": "user", "content": "Пожалуйста используй команду которую выберишь"}],
    input=[{"role": "user", "content": "Call ls for me"}],
    tools=tools
)
# response = dict(response)
# pretty = json.dumps(response, indent = 4)
response_dict = response.model_dump()
print(json.dumps(response_dict, indent=4, ensure_ascii=False))
# print (type(response))

# client = OpenAI(
#     api_key=openai_api_key
# )

# chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "system",
#         "content": "You are an expert who responds to the best of your ability. Limit you responses to 1000 tokens."
#     }, {
#         "role": "user",
#         "content": "Tell me up-to-date information about income tax in Finland."
#     }],
#     model=model,
# )

# print(chat_completion)
