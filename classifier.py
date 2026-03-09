# classifier.py

import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def classify_intent(message: str) -> dict:
    """
    Calls LLM to classify user intent.
    Returns a JSON with 'intent' and 'confidence'.
    Defaults to 'unclear' if parsing fails.
    """
    prompt = f"""
Your task is to classify the user's intent. 
Choose one of: code, data, writing, career, unclear.
Return a single JSON object: {{ "intent": "label", "confidence": float }}.
Do not include any other text.

User message: {message}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Classify the intent."},
                      {"role": "user", "content": prompt}],
            temperature=0
        )

        # Extract text
        text = response.choices[0].message.content.strip()

        # Parse JSON
        intent_json = json.loads(text)
        return {
            "intent": intent_json.get("intent", "unclear"),
            "confidence": float(intent_json.get("confidence", 0.0))
        }

    except Exception as e:
        # In case of any error, return unclear
        return {"intent": "unclear", "confidence": 0.0}