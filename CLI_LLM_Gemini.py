from google import genai
from google.genai.errors import APIError

print("[From aistudio.google.com]")
api_key = input("Paste your API HERE: ")
client = genai.Client(api_key=api_key)

models = ["gemini-3.5-flash-lite", "gemini-3.5-flash", "gemini-2.5-flash", "gemini-2-flash", "gemini-2-flash-lite", "gemini-2.5-flash-lite", "gemini-2.5-pro", "gemini-3-flash", "gemini-3.1-pro", "gemini-3.1-flash-lite", "gemini-3.6-flash"]
print("SELECT Model Options: ", *models, sep="\n\t")
Choice = input("Enter the Gemini model's name u want to use: ")

chat = client.chats.create(model=Choice)

print("\n--- Chat STARTED TYPE {exit} to well.. exit of course ---")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break

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
        print(f"\nGemini: Unexpected error -> {i} ")
        