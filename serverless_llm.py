from openai import OpenAI
import json
import os

with open('key_ai.json') as f:
    data = json.load(f)

# with open('structured_output.json') as f:
#     structured_output = json.load(f)

openai_api_key = data["openai_api_key"]
tools = [{
    "type": "function",
    "name": "get_ls_results",
    "description": "Get result of ls -las function",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False
    }
}]

client = OpenAI(
    api_key=openai_api_key
)
input_messages=[{"role": "user", "content": "Try to call ls please!"}]
response = client.responses.create(
    model="gpt-4.1-2025-04-14",
    input = input_messages,
    tools=tools
)
response_dict = response.model_dump()
print(json.dumps(response_dict, indent=4, ensure_ascii=False))
tool_call = response.output[0]
print(tool_call)

def get_ls_results():
    print("get_ls_results was called!")
    return os.listdir('.')

if tool_call.name == "get_ls_results":
    print("get_ls_results will be called") 
    ls_results = get_ls_results()
    input_messages.append(tool_call)  # append model's function call message

    input_messages.append({                               # append result message
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": str(ls_results)
    })
    
    response_2 = client.responses.create(
        model="gpt-4.1",
        input=input_messages,
        tools=tools,
    )
    print(response_2.output_text)
