from groq import Groq
import json
from pdf_extractor import extract
import os



def parse(path:str) -> dict:
    string =extract(path)
    client = Groq(api_key = os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
    model = os.getenv("GROQ_MODEL"),
    messages = [
        {"role": "user", "content": f"parse this timetable into a JSON dict keyed by day, return only JSON nothing else:\n{string}"}
    ]
)
    text = response.choices[0].message.content
    return json.loads(text)
