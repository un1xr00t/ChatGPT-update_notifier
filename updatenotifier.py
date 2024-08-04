import requests
from bs4 import BeautifulSoup

def check_for_update(app_id, user_key, api_token):
    url = f"https://apps.apple.com/us/app/chatgpt/id{app_id}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        version_element = soup.find('p', class_='whats-new__latest__version')
        if version_element:
            latest_version = version_element.text.strip()
            with open("current_version.txt", "r+") as file:
                current_version = file.read().strip()
                if latest_version != current_version:
                    print(f"New version available: {latest_version}")
                    file.seek(0)
                    file.write(latest_version)
                    file.truncate()
                    send_pushover_notification(latest_version, user_key, api_token)
                else:
                    print("You already have the latest version.")
        else:
            print("Could not find version information.")
    else:
        print("Failed to retrieve app information.")

def send_pushover_notification(version, user_key, api_token):
    message = f"New ChatGPT version available: {version}"
    url = "https://api.pushover.net/1/messages.json"
    payload = {
        "token": api_token,
        "user": user_key,
        "message": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print("Failed to send notification.")

if __name__ == "__main__":
    app_id = "6448311069"  # Replace with the actual ChatGPT app ID
    user_key = "YOUR_PUSHOVER_USER_KEY"  # Replace with your Pushover user key
    api_token = "YOUR_PUSHOVER_API_TOKEN"  # Replace with your Pushover API token
    check_for_update(app_id, user_key, api_token)
