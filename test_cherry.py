import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def open_app(app_name: str) -> str:
    """Opens a software application on the Windows PC."""
    return f"Successfully opened {app_name}."

def close_app(app_name: str) -> str:
    """Closes an active application on the Windows PC."""
    return f"Successfully closed {app_name}."

def open_website(website_name: str) -> str:
    """Opens a website URL in the default browser."""
    return f"Opened {website_name} in the browser."

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[open_app, close_app, open_website]
)
chat = model.start_chat(enable_automatic_function_calling=True)

try:
    response = chat.send_message("open notepad")
    print("Response parts:", response.parts)
    print("Response text:", response.text)
except Exception as e:
    print("EXCEPTION:", type(e).__name__, str(e))
