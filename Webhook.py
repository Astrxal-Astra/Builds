import requests

webhook_url = input("Enter Discord webhookURL: ")
message = input("Enter Message to send through webhook: ")
data = {"content": message}

try:
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("~SENT...~")
    else:
        print(f"Not working: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException:
    print(f"Failed to send: {message}")
    print(f"Due to invalid or Not a WebhookURL: :{webhook_url};")
             