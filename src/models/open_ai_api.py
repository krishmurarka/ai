from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def run_open_ai_api():
  client = OpenAI()

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant which provides information about the temperature."},
      {"role": "user", "content": "Hey there"},
    ],
    max_tokens= 5,
    temperature=0.1
  )
  print(response.choices[0].message.content)
