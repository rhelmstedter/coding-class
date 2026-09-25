"""Chatbot 2.0 by Mr. Helmstedter: the Shelter Matchmaker."""

import random


def ask(question):
    """Print a question and hand back the answer with the mess cleaned off."""
    answer = input(question)
    return answer.strip().lower()


THINKING = [
    "Let me write that down.",
    "Noted.",
    "Okay, that helps.",
]

ENCOURAGEMENT = [
    "You are going to be a great match for somebody.",
    "Every animal in here is hoping you walk in.",
    "No wrong answers on this one.",
]

HOMES = ["house", "apartment", "dorm"]
ENERGIES = ["calm", "playful", "somewhere in between"]

name = ask("Welcome to the shelter! What is your name? ").title()
print(f"Good to meet you, {name}. Let me find you a friend.")
print()

print("Where do you live?")
for option in HOMES:
    print(f"  - {option}")
home = ask("> ")
while home not in HOMES:
    print(f'I do not have "{home}" on the list. Pick one of the three.')
    home = ask("> ")

if home == "house":
    print("A house gives us plenty to work with.")
elif home == "apartment":
    print("An apartment narrows things down, but it does not rule much out.")
else:
    print("A dorm is tight, but people make it work.")
print()

space = ask("How much room do you have for a pet? ")
print(random.choice(THINKING))
print()

schedule = ask("Are you home most of the day, or out most of the day? ")
if "home" in schedule:
    print("Being around a lot is the single best thing you can offer.")
elif "out" in schedule:
    print("Then we want somebody who is comfortable on their own.")
else:
    print("I will assume your days are a mix.")
print()

print("What kind of energy are you hoping for?")
for option in ENERGIES:
    print(f"  - {option}")
energy = ask("> ")
while energy not in ENERGIES:
    print(f'I do not have "{energy}" on the list. Pick one of the three.')
    energy = ask("> ")

if energy == "calm":
    print("Calm it is. I have three in mind already.")
elif energy == "playful":
    print("Playful is easy to find here. Loud, but easy.")
else:
    print("Somewhere in the middle. That is most of them, honestly.")
print()

mornings = ask("How do you feel about early mornings? ")
print(random.choice(THINKING))
print()

experience = ask("Have you had a pet before? ")
if experience in ["yes", "y", "yeah", "yep"]:
    print("Experience helps. You know what you are signing up for.")
elif experience in ["no", "n", "nope"]:
    print("First time is exciting. We will start you somewhere gentle.")
else:
    print("Either way, we will figure it out together.")
print(random.choice(ENCOURAGEMENT))
print()

hoping_for = ask("What is one thing you are looking forward to? ")
nervous = ask("Anything you are nervous about? ")
print(random.choice(THINKING))
print()

print(f"Here is what I have, {name}.")
print(f"{home.title()}, {space} to work with, and you are {schedule}.")
print(f"You want {energy}. On early mornings you said: {mornings}.")
print(f"Looking forward to {hoping_for}. Nervous about {nervous}.")
print()
print("Give me a minute. I think I know who to bring out.")
