#!/usr/bin/env python3
"""Use the dog api to get images of dogs."""

import difflib
import requests
import random
import os

from rich import print  # poetry add rich

WELCOME = "[red]Welcome to the dog API :dog:. We serve up cute images of dogs.[/red]"


def fetch_random_dog() -> None:
    """Get a random image of a dog."""
    RANDOM_URL = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(RANDOM_URL).json()
    random_link = response["message"]
    print(random_link)


def fetch_all_breeds() -> list:
    """Return a list of all possible breeds and sub breeds."""
    ALL_BREEDS_URL = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(ALL_BREEDS_URL).json()
    breeds = []
    for breed, sub_breeds in response["message"].items():
        breeds.append(breed)
        if sub_breeds:
            for sub_breed in sub_breeds:
                breeds.append(f"{sub_breed} {breed}")
    return breeds


def get_user_choice() -> str:
    """Get the breed from the user."""
    breeds = fetch_all_breeds()
    while True:
        user_choice = input("Enter the breed you would like to see:\n> ").lower()
        if user_choice not in breeds:
            try:
                suggestion = difflib.get_close_matches(user_choice, breeds)[0]
            except IndexError:
                print("Could not find a close match. Please try again.\n")
                continue
            confirm = input(
                f"That breed does not exist, did you mean '{suggestion}'?"
            ).lower()
            if confirm.startswith("y"):
                return suggestion
            else:
                print("Ok, try again.")
                continue
        else:
            return user_choice


def fetch_by_breed() -> None:
    """Get an image of a dog based on user input."""
    user_choice = get_user_choice()
    if " " in user_choice:
        sub_breed, breed = user_choice.split()
        user_choice = f"{breed}/{sub_breed}"
    breed_url = f"https://dog.ceo/api/breed/{user_choice}/images"
    breed_response = requests.get(breed_url).json()["message"]
    print(random.choice(breed_response))


def main() -> None:
    """Run the main menu."""
    print(WELCOME)
    while True:
        main_options = input(
            "Choose from the following options:\n\n[B]y Breed\n[R]andom\n[Q]uit\n> "
        ).lower()
        os.system("clear")
        if main_options.startswith("r"):
            print("Here is a random dog:\n\n")
            fetch_random_dog()
        elif main_options.startswith("b"):
            fetch_by_breed()
        elif main_options.startswith("q"):
            print("OK, see you next time.")
            break
        else:
            print("Sorry, I don't understand. Please choose one of the options.")


if __name__ == "__main__":
    main()
