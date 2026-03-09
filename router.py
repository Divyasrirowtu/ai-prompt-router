import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent", "unclear")

    # If intent is unclear → ask clarification question
    if intent == "unclear":
        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"

    # Get correct system prompt
    system_prompt = SYSTEM_PROMPTS.get(intent)

    if not system_prompt:
        return "Sorry, I cannot handle this request right now."

    # Second LLM call to generate response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()