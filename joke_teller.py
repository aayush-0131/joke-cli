# joke_teller.py

import requests
import sys


def get_joke():
    """
    Fetches a random dad joke from the icanhazdadjoke API.
    """
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}  # We want the response in JSON format

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)

        data = response.json()
        return data.get("joke")

    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, etc.
        return f"Error: Could not fetch a joke. Reason: {e}"
    except KeyError:
        # Handle cases where the JSON response doesn't have the 'joke' key
        return "Error: Invalid response from the joke API."


def main():
    """
    Main function to print the joke.
    """
    print("\n" + "=" * 50)
    joke = get_joke()
    print(joke)
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
