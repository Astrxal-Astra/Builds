import requests
import validators
import time
import sys

while True:    
    try:
        webhook_url = input("Enter discord webhook URL: ").strip()
        if validators.url(webhook_url):
            break
        print(f"Invalid URL {webhook_url}")
        print("Try again")
    except KeyboardInterrupt:
        print("\nTyping Interrupted")
        sys.exit()
        
while True:
    try:
        time.sleep(3)
        message = input("\nEnter Message to send through webhook[type: exit ; to exit]: ").strip()
        if message.lower() == "exit":
            break
        data = {"content": message}
        
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print("\nSent")
            else:
                print(f"Not working: {response.status_code}")
                print(response.text)
        except requests.exceptions.RequestException:
            print(f"Failed to send: {message}")
            print("NO INTERNET, or Discord Servers are down (TRY AGAIN LATER)")

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
