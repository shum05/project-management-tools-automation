# Script to collect data from project management tools (Jira, Trello)

import requests
import json
from .config import JIRA_API_KEY, JIRA_API_URL, TRELLO_API_KEY, TRELLO_API_URL

def fetch_jira_data():
    headers = {
        "Authorization": f"Bearer {JIRA_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(JIRA_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from Jira")
        return {}

def fetch_trello_data(board_id):
    url = TRELLO_API_URL.format(board_id=board_id)
    params = {
        'key': TRELLO_API_KEY,
        'token': '****'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from Trello")
        return []

def save_data(data, filename='data/raw_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    jira_data = fetch_jira_data()
    trello_data = fetch_trello_data('your_board_id')
    combined_data = {"jira": jira_data, "trello": trello_data}
    save_data(combined_data)
