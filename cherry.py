import os
import time
import uuid
import subprocess
import webbrowser
import psutil
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
import pygame

# Initialize pygame mixer for playing high-quality audio
pygame.mixer.init()

# Load environment variables
load_dotenv()

# Configure Google Gemini API
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print("Error: Valid GEMINI_API_KEY not found in .env file.")
    exit(1)

genai.configure(api_key=gemini_api_key)

# ==========================================
# JARVIS / PC CONTROL TOOLS FOR GEMINI
# ==========================================

def open_app(app_name: str) -> str:
    """Opens a software application on the Windows PC."""
    app_name = app_name.lower()

    # Common Windows shortcuts
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "command prompt": "cmd.exe",
        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
        "settings": "ms-settings:",
        "file explorer": "explorer.exe",
        "spotify": "spotify.exe"
    }

    try:
        if app_name in apps:
            os.system(f"start {apps[app_name]}")
            return f"Successfully opened {app_name}."
        else:
            # Try to start it generically if not in the dictionary
            os.system(f"start {app_name}")
            return f"Attempted to open {app_name}."
    except Exception as e:
        return f"Failed to open {app_name}: {str(e)}"

def close_app(app_name: str) -> str:
    """Closes an active application on the Windows PC."""
    closed = False
    for proc in psutil.process_iter(['name']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                proc.kill()
                closed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if closed:
        return f"Successfully closed {app_name}."
    return f"Could not find {app_name} to close."

def open_website(website_name: str) -> str:
    """Opens a website URL in the default browser."""
    website_name = website_name.strip().lower()
    if website_name.startswith('http'):
        url = website_name
    elif '.' in website_name:
        url = f"https://{website_name}"
    else:
        url = f"https://www.{website_name}.com"

    webbrowser.open(url)
    return f"Opened {url} in the browser."

def connect_phone() -> str:
    """Checks if a phone is connected via ADB."""
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device\n" in result.stdout or "device\r\n" in result.stdout:
            # Note: adb devices lists 'List of devices attached' and then '<serial> device'
            lines = result.stdout.strip().split('\n')
            devices = [line.split('\t')[0] for line in lines[1:] if 'device' in line]
            if devices:
                return f"Successfully connected to phone (Device: {devices[0]})."
        return "No phone connected. Please ensure ADB is enabled and the device is plugged in."
    except Exception as e:
        return f"Failed to connect to phone: {str(e)}"

def open_phone_app(app_name: str) -> str:
    """Opens an application on the connected Android phone."""
    app_name = app_name.lower()

    # Common Android app packages
    apps = {
        "settings": "com.android.settings",
        "chrome": "com.android.chrome",
        "youtube": "com.google.android.youtube",
        "camera": "com.android.camera2", # Stock Android, might differ on Samsung/others
        "maps": "com.google.android.apps.maps",
        "play store": "com.android.vending",
        "gmail": "com.google.android.gm",
        "spotify": "com.spotify.music"
    }

    package_name = apps.get(app_name)
    if not package_name:
        return f"App {app_name} is not in my list of known phone apps."

    try:
        result = subprocess.run(
            ["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"Successfully opened {app_name} on the phone."
        else:
            return f"Failed to open {app_name} on the phone. Ensure the phone is unlocked and connected."
    except Exception as e:
        return f"Error while trying to open phone app: {str(e)}"

# ==========================================
# CHERRY'S VOICE & LISTENING LOGIC
# ==========================================

def speak(text):
    # Display Kreed's message in a cute panel
    print(f"Cherry: {text}")

    try:
        # We use gTTS with 'en' (English) language.
        tts = gTTS(text=text, lang='en', tld='com', slow=False)
        filename = f"temp_voice_{uuid.uuid4().hex}.mp3"
        tts.save(filename)

        # Play the audio file
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until the audio is finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Clean up the audio file
        pygame.mixer.music.unload()
        time.sleep(0.1)
        try:
            os.remove(filename)
        except Exception:
            pass

    except Exception as e:
        print(f"Audio error: {e}")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Network error: {e}")
        return None

def main():
    # Clear the terminal for a clean UI
    os.system('cls' if os.name == 'nt' else 'clear')

    print("CHERRY AI\nYour Personal Assistant\n")

    # Set up Gemini with our custom personality and connect the PC control tools
    system_prompt = (
        "You are Cherry, a highly intelligent AI assistant for my PC (like Jarvis). "
        "You MUST speak in clear English. "
        "For example: 'Certainly! I am opening notepad for you right now!' or 'I'm processing your complex request, please wait a moment!' "
        "You can control the PC, open apps, close apps, open websites, and connect to my phone using the provided tools. "
        "Be extremely helpful and act like a loyal digital companion capable of handling complex orders. Do NOT use emojis, as they will be spoken out loud."
    )

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_prompt,
        tools=[open_app, close_app, open_website, connect_phone, open_phone_app] # Give Gemini access to these functions
    )

    # enable_automatic_function_calling=True makes Gemini handle tool execution behind the scenes!
    chat = model.start_chat(enable_automatic_function_calling=True)

    # Initial greeting in English
    speak("Hello! I am Cherry, your helpful assistant. What tasks can I do for you today?")

    while True:
        user_input = listen()

        if user_input:
            # Exit commands
            if any(word in user_input for word in ['exit', 'quit', 'stop', 'goodbye', 'bye', 'shutdown']):
                speak("Understood, I am shutting down. See you next time! Goodbye!")
                break

            try:
                # Send text to Gemini. If it needs to open an app, it will do it automatically!
                response = chat.send_message(user_input)

                # Check if text is present to avoid ValueErrors
                try:
                    text_to_speak = response.text
                except ValueError:
                    # In case the model only returns a function call and no text
                    if response.parts:
                        text_to_speak = "Done!"
                    else:
                        text_to_speak = "An error occurred."

                if text_to_speak:
                    speak(text_to_speak)
            except Exception as e:
                error_name = type(e).__name__
                error_msg = str(e)
                print(f"Error communicating with AI: {error_name} - {error_msg}")

                if "ResourceExhausted" in error_name or "429" in error_msg:
                    speak("Oh no! I'm getting too many requests and my brain is overloaded! Please give me about a minute to cool down!")
                else:
                    speak("Sorry, I am encountering an issue understanding that. Please try again.")

if __name__ == "__main__":
    main()
