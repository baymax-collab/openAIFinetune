import os
import openai
openai.api_key = ""
import json
completion = openai.ChatCompletion.create(
  model="",
  messages=[
    {"role": "system", "content": "小明"},
    {"role": "user", "content": "你是谁"}
  ]
)
# print(completion.choices[0].message)
json_str = json.dumps(completion.choices[0].message)
print(json.loads(json_str))