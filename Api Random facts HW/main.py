import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    try:
        response = requests.get(url, timeout=5)  # 5 seconds max wait
        response.raise_for_status()  # Raise error if status not 200
        fact_data = response.json()
        print(f".....\nDid you know? {fact_data['text']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching fact: {e}")

while True:
    user_input = input("Press Enter to get a random fact or type q to quit... ")
    if user_input.lower() == 'q':
        break
    get_random_fact()