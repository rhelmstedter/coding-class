#!/usr/bin/env python3
"""Dog api."""
import difflib
import os
import random

from rich import print
import requests

WELCOME = "[blue]Welcome to the Dog API :dog:. We serve up images of cute dogs.[/blue]"


def fetch_random_dog() -> str:
    """Return a random image of a dog across all breeds."""
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url).json()
    return response["message"]


def get_all_breeds() -> list:
    """Return a list of all breeds and sub breeds."""
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
    """Get the user choice of dog breed."""
    breeds = get_all_breeds()
    while True:
        user_choice = input("Enter the dog breed you want to see:\n>")
        if user_choice not in breeds:
            try:
                suggestion = difflib.get_close_matches(user_choice, breeds)[0]
            except IndexError:
                print("Sorry, I could not find a close match. Please try again.")
                continue
            confirm = input(
                f"{user_choice} does not exist. Did you mean '{suggestion}'?\n"
            )
            if confirm.lower().startswith("y"):
                return suggestion
            else:
                print("Ok, try again.")
                continue
        else:
            return user_choice


def fetch_dog_by_breed() -> str:
    """Return an image of a dog breed choosen by the user."""
    user_choice = get_user_choice()
    if " " in user_choice:
        sub_breed, breed = user_choice.split()
        user_choice = f"{breed}/{sub_breed}"
    breed_url = f"https://dog.ceo/api/breed/{user_choice}/images"
    breed_response = requests.get(breed_url).json()["message"]
    return random.choice(breed_response)


def main() -> None:
    """Run the main logic of the program."""
    print(WELCOME)
    while True:
        main_option = input(
            "Choose from the following:\n[B]y breed\n[R]andom\n[Q]uit\n>"
        ).lower()
        os.system("clear")
        if main_option.startswith("r"):
            print("Here is a random dog:\n")
            print(fetch_random_dog())
        elif main_option.startswith("b"):
            print(fetch_dog_by_breed())
        elif main_option.startswith("q"):
            print("Ok, see you next time.")
            break
        else:
            print("I didn't understand. Please choose one of the options.")


if __name__ == "__main__":
    main()
