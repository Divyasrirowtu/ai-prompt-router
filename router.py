# router.py

import os
import openai
from prompts import SYSTEM_PROMPTS, CLARIFY_PROMPT
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def route_and_respond(message: str, intent: dict) -> str:
    """
    Routes the message to the correct expert system prompt.
    Returns the LLM-generated response.
    """
    label = intent.get("intent", "unclear")

    if label == "unclear":
        return CLARIFY_PROMPT

    system_prompt = SYSTEM_PROMPTS.get(label)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7
        )

        final_response = response.choices[0].message.content.strip()
        return final_response

    except Exception as e:
        return f"Error generating response: {str(e)}"