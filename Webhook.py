import requests
import validators
import time
import sys
import logging

logging.basicConfig(filename="discord.script", filemode="a", level=logging.INFO, encoding="utf-8", format="%(asctime)s - [%(name)s] - %(levelname)s - %(message)s")
logger = logging.getLogger("DISCORD-WEBHOOK")

while True:    
    try:
        webhook_url = input("Enter discord webhook URL: ").strip()
        if validators.url(webhook_url):
            break
        print(f"Invalid URL: ['{webhook_url}']", "\nTry Again")

        logger.error(f"invalid URL: {webhook_url}")
    except KeyboardInterrupt:
        print("\nTyping Interrupted")
        logger.error("Program stopped during URL input via KeyboardInterrupt.")
        sys.exit(1)
        
while True:
    try:
        time.sleep(2)
        message = input("\nEnter Message to send through webhook[type: exit ; to exit]: ").strip()
        if message.lower() == "exit":
            break
        data = {"content": message}
        
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print("\n---Sent---")
                logger.info("message sent")
            else:
                print(f"Not working: {response.status_code}")
                print(response.text)
                logger.error(f"discord rejected the message. Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"Failed to send: {message}", "\nNO INTERNET, or Discord Servers are down (TRY AGAIN LATER)")                       
            logger.critical(f"couldn't send {message} due to unstable connection")

    except KeyboardInterrupt:
        print("\nExiting program...")
        logger.error("typing interrupted")
        sys.exit(1)
        
