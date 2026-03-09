import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_intent(message: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": message}
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        result = json.loads(content)

        return {
            "intent": result.get("intent", "unclear"),
            "confidence": float(result.get("confidence", 0.0))
        }

    except Exception:
        return {
            "intent": "unclear",
            "confidence": 0.0
        }
from classifier import classify_intent

msg = "How do I sort a list of objects in Python?"
result = classify_intent(msg)
print(result)