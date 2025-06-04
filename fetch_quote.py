import json
from urllib.request import urlopen

API_URL = "https://api.quotable.io/random"

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"


def fetch_quote():
    with urlopen(API_URL) as resp:
        data = json.loads(resp.read().decode())
        return data.get('content'), data.get('author')


def main():
    quote, author = fetch_quote()
    print(f"{CYAN}{quote}{RESET}\n- {GREEN}{author}{RESET}")


if __name__ == "__main__":
    main()
