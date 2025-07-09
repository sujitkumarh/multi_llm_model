from PIL import Image
import pytesseract
from autogen import AssistantAgent, UserProxyAgent
import json
import os

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\shujare\tesseract.exe"

def run():
    # Load LLM config
    config = json.load(open("config/ollama_config.json"))

    # Create assistant
    assistant = AssistantAgent(
        name="assistant",
        llm_config=config,
        system_message=(
            "You're an assistant analyzing screen content from a screenshot. "
            "Only respond to what's in the image. If the user asks anything else, politely decline. "
            "At the end of each reply, ask if they'd like to continue or end the conversation."
        ),
    )

    # Create user agent
    user = UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={"use_docker": False},
    )

    # Load and OCR the screenshot
    if not os.path.exists("assets/screenshot.png"):
        print("❌ Screenshot not found at assets/screenshot.png")
        return

    image = Image.open("assets/screenshot.png")
    text = pytesseract.image_to_string(image)

    message = f"""Here's the screen content:\n{text}\n\nWhat should I do next?"""
    user.initiate_chat(assistant, message=message)

    # Ask the user if they want to continue
    while True:
        choice = input("\n🤖 Would you like to continue chat or end this conversation? (continue/end): ").strip().lower()
        if choice == "end":
            print("👋 Ending the conversation. Have a great day!")
            break
        elif choice == "continue":
            next_prompt = input("\n💬 Enter your next message related to the screen: ").strip()
            if next_prompt:
                user.initiate_chat(assistant, message=next_prompt)
        else:
            print("⚠️ Please type 'continue' or 'end'.")
