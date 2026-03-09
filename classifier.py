import json
import os
CLASSIFIER_PROMPT = """
Your task is to classify the user's intent.

Choose one of these labels:
code
data
writing
career
unclear

Respond ONLY with a JSON object in this format:

{
  "intent": "label",
  "confidence": 0.0
}

Confidence must be a number between 0 and 1.

Do not include explanations or extra text.
"""
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