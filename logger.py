# logger.py

import json
from datetime import datetime
from classifier import classify_intent
from router import route_and_respond

def log_request(user_message: str, intent: dict, final_response: str, log_file="route_log.jsonl"):
    """
    Logs the request to a JSON Lines file.
    Each line contains a JSON object with:
    - user_message
    - intent
    - confidence
    - final_response
    - timestamp
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_message": user_message,
        "intent": intent.get("intent", "unclear"),
        "confidence": intent.get("confidence", 0.0),
        "final_response": final_response
    }

    # Append the entry to the log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


# -----------------------------
# Example usage / test
# -----------------------------
if __name__ == "__main__":
    # Sample user message
    user_message = "How do I sort a list in Python?"

    # Step 1: Classify intent
    intent = classify_intent(user_message)

    # Step 2: Route and generate final response
    final_response = route_and_respond(user_message, intent)

    # Step 3: Log the request
    log_request(user_message, intent, final_response)

    # Step 4: Print final response
    print("Final Response:\n", final_response)
    print("\nLogged to route_log.jsonl")