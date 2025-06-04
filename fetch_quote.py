import json
import random
from urllib.request import urlopen, URLError

API_URL = "https://api.quotable.io/random"

# ANSI colours
CYAN  = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Fallback quotes if the API can’t be reached
LOCAL_QUOTES = [
    ("Life is either a daring adventure or nothing at all.", "Helen Keller"),
    ("Be yourself; everyone else is already taken.",            "Oscar Wilde"),
    ("The secret of getting ahead is getting started.",         "Mark Twain"),
]

def fetch_quote():
    try:
        with urlopen(API_URL, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            return data["content"], data["author"]
    except (URLError, TimeoutError, ValueError):
        # Sandbox can’t reach the Internet → choose a local quote instead
        return random.choice(LOCAL_QUOTES)

def main():
    quote, author = fetch_quote()
    print(f"{CYAN}{quote}{RESET}\n – {GREEN}{author}{RESET}")

if __name__ == "__main__":
    main()
