import openai
from gptkey import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
output = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user",
    "content":
                "Write prompt here!"}]
)
print(output)