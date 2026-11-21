
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found.")

client = genai.Client(api_key=api_key)


def summarize_logs(log_data):

    prompt = f"""
    You are an expert DevOps engineer.

    Analyze the following software build logs:

    {log_data}

    Provide a structured report containing:

    1. Build Status
    2. Error Summary
    3. Possible Root Causes
    4. Warning Analysis
    5. Recommended Solutions
    6. Overall Conclusion

    Use simple and understandable language.
    Do not invent errors or facts.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text