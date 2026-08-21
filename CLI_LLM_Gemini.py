import sys
from google import genai
from google.genai.errors import APIError
from google.genai import types

print("[From aistudio.google.com]")
api_key = input("\nPaste your API HERE: ")
client = genai.Client(api_key=api_key)

models = [
    "gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", 
    "gemini-3.1-pro-preview", "gemini-3.1-pro-preview-customtools", 
    "gemini-3.1-flash-lite", "gemini-3.1-flash-lite-preview", 
    "gemini-3-pro-preview", "gemini-3-flash-preview", "gemini-2.5-pro", 
    "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash", 
    "gemini-2.0-flash-001", "gemini-2.0-flash-lite", "gemini-2.0-flash-lite-001", 
    "gemini-flash-latest", "gemini-flash-lite-latest", "gemini-pro-latest", 
    "gemma-4-31b-it", "gemma-4-26b-a4b-it", "gemini-omni-flash-preview"
]
print("SELECT Model Options: ", *models, sep="\n\t")

while True:
    Choice = input("Enter the Gemini model's name u want to use: ")
    prompt = input('\nEnter prompt u wanna give gemini [example it\'s personality, how to act, etc... NO legal stuff though] type "skip" to skip: ')
    
    if prompt.lower() == "skip":
        config = None 
    else:
        config = types.GenerateContentConfig(system_instruction=prompt)
    
    break

try:
    chat = client.chats.create(model=Choice, config=config)
except Exception as e:
    print(f"Failed to create chat session: {e}")
    sys.exit(1)

print("\n--- Chat STARTED TYPE exit to well.. exit of course ---")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        sys.exit(0)

    try:
        response = chat.send_message_stream(user_input)
        print("Gemini: ", end="", flush=True)
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
    except APIError as e:
        print(f"\nGemini: API error -> {e}")
    except Exception as i:
        print(f"\nGemini: Unexpected error -> {i}")
         
