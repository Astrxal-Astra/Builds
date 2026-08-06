import time
import requests
from bs4 import BeautifulSoup
import validators

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def check_slots(url, keywords):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text()
            
            found_keywords = [kw for kw in keywords if kw.lower() in page_text.lower()]
            
            if found_keywords:
                print(f"ALERT: Found keyword(s) {found_keywords}! Alert")
                return True 
            else:
                print("Checked PAGE... Still searching.")
                
        elif response.status_code == 403 or response.status_code == 429:
            print(f"Access denied. Status {response.status_code}, maybe you've been blocked.")
           
            
        else:
            print(f"Server returned status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Connection failed. Maybe your wifi is off.")
    except requests.exceptions.Timeout:
        print("Connection timed out. The server is taking too long.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    
    return False 

if __name__ == "__main__":
    while True:
        target_url = input("Paste target URL here: ").strip()
        if validators.url(target_url):
            break
        print(f"Invalid URL: '{target_url}'. Try again.")
    
    raw_keywords = input("Enter keywords separated by commas: ").strip()
    keywords = [kw.strip() for kw in raw_keywords.split(",")]
    
    while True:
        try:
            check_interval = int(input("ENTER INTERVAL's IN SECONDS(S): ").strip())
            if check_interval > 0:
                break
            print("Please enter a number greater than 0 Or it literally just breaks.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"\nMonitoring: {target_url}")
    print(f"Tracking keywords: {keywords}")
    print(f"Checking every {check_interval} seconds...\n")
    
    while True:
        should_stop = check_slots(target_url, keywords)
        if should_stop:
            break
        time.sleep(check_interval)
                        