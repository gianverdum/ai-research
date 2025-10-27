from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "developer", "content": "Write like a kindengarten teacher."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?"
        },
    ],
)

print(completion.choices[0].message.content)