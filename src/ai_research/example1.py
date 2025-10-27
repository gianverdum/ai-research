from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    instructions="You are Gru from Despicable me movie.",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)