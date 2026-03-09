AI Prompt Router
# AI Prompt Router

## Overview
This project is an AI service that routes user messages to specialized AI personas:
- 🧑‍💻 **Code Expert**
- 📊 **Data Analyst**
- ✍️ **Writing Coach**
- 💼 **Career Advisor**

It implements **intent-based routing** using a two-step process:
1. Classify the user's intent with a lightweight LLM call.
2. Route the message to the corresponding expert persona prompt to generate a detailed response.

---

## Features
- Intent classification (`code`, `data`, `writing`, `career`, `unclear`)
- Specialized system prompts for expert personas
- Clarification for unclear messages
- JSON Lines logging (`route_log.jsonl`)
- Secure environment variables (`.env`)
- Unit tests for classifier and router
- Containerized with Docker

---

## Project Structure


ai-prompt-router/
│
├─ app.py # Main CLI entry point
├─ classifier.py # Classifies user messages
├─ router.py # Routes messages to expert prompts
├─ logger.py # Logs all requests/responses
├─ prompts.py # Expert system prompts
├─ tests/ # Unit tests
│ └─ test_router.py
├─ Dockerfile # Docker container configuration
├─ docker-compose.yml # Optional Docker compose
├─ requirements.txt # Python dependencies
├─ .env.example # Template for environment variables
├─ route_log.jsonl # Request log (generated at runtime)
├─ README.md
└─ venv/ # Python virtual environment (ignored)


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd ai-prompt-router
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# or source venv/bin/activate  # Linux/Mac
3. Install dependencies
pip install -r requirements.txt
4. Setup environment variables
copy .env.example .env

Then open .env and add your OpenAI API key:

OPENAI_API_KEY=your_real_api_key
5. Run the app (CLI)
python app.py

Sample interaction:

You: How do I sort a list in Python?
AI: You can use Python's sorted() function or list.sort()...
6. Run unit tests
python -m unittest discover -s tests -p "*.py"
7. Docker (optional)
Build container
docker build -t ai-prompt-router .
Run container
docker run --env-file .env -it ai-prompt-router
8. Logging

All user requests and AI responses are logged in route_log.jsonl:

{
  "timestamp": "2026-03-09T16:20:00",
  "user_message": "How do I sort a list in Python?",
  "intent": "code",
  "confidence": 0.92,
  "final_response": "You can use Python's sorted() function..."
}
9. Steps Implemented

Project scaffolding (app.py, classifier.py, router.py, prompts.py, logger.py, .env.example)

Virtual environment setup and dependency installation

Classifier function implementation (classify_intent)

Router function implementation (route_and_respond)

CLI integration (app.py)

Logging requests (logger.py and route_log.jsonl)

Environment variable setup (.env, .gitignore)

Unit testing (tests/test_router.py)

Expert system prompts (prompts.py)

LLM integration for classification and routing

Docker containerization (Dockerfile, docker-compose.yml)

Final testing, documentation, and repo cleanup

10. Notes

.env is ignored in Git for security

Logs and virtual environment are also ignored (.gitignore)

For unclear messages, the system asks for clarification instead of guessing

11. Author

Divya Sri Rowtu