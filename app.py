# app.py
from classifier import classify_intent
from router import route_and_respond
from logger import log_request
def main():
    print("=== AI Prompt Router ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Step 1: Classify intent
        intent = classify_intent(user_message)

        # Step 2: Route and generate final response
        final_response = route_and_respond(user_message, intent)

        # Step 3: Log the request
        log_request(user_message, intent, final_response)

        # Step 4: Print the response
        print("\nAI:", final_response, "\n")
        if __name__ == "__main__":
            main()
        