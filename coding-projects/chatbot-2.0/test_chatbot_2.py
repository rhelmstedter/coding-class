"""Test harness for chatbot_2.py.

Runs each specification test case through the real program and checks the
output against what the specification promises. random.seed is fixed so the
lines pulled from THINKING and ENCOURAGEMENT are reproducible in the writeup.
"""

import subprocess
import sys

PROGRAM = "chatbot_2.py"
SEED = 7

CASES = [
    {
        "name": "Typical case",
        "note": "Valid menu answers on the first try, ordinary text everywhere else. "
                "Every decision block should land on a branch that fits the answer.",
        "inputs": [
            "Russell", "apartment", "not much", "out most of the day", "calm",
            "I hate them", "yes", "coming home to somebody",
            "the vet bills honestly",
        ],
        "expect": [
            "An apartment narrows things down, but it does not rule much out.",
            "Then we want somebody who is comfortable on their own.",
            "Calm it is. I have three in mind already.",
            "Experience helps. You know what you are signing up for.",
            "Apartment, not much to work with, and you are out most of the day.",
            "You want calm. On early mornings you said: i hate them.",
        ],
    },
    {
        "name": "Special case: messy typing",
        "note": "Capitals and stray spaces on every answer. The cleaning inside ask() "
                "has to absorb them, or the menu answers get refused and every "
                "decision block falls through to its else.",
        "inputs": [
            "russell", "  APARTMENT  ", "Some", "  Home  ", "  CALM ",
            "fine", "  YES  ", "walks", "nothing",
        ],
        "expect": [
            "Good to meet you, Russell. Let me find you a friend.",
            "An apartment narrows things down, but it does not rule much out.",
            "Being around a lot is the single best thing you can offer.",
            "Calm it is. I have three in mind already.",
            "Experience helps. You know what you are signing up for.",
        ],
        "reject": [
            'I do not have "  apartment  " on the list. Pick one of the three.',
        ],
    },
    {
        "name": "Boundary case: answer not on the menu",
        "note": "Two wrong answers on the first menu and one on the second. The while "
                "loop has to refuse each one and ask again without moving on.",
        "inputs": [
            "Ana", "condo", "tent", "apartment", "not much", "home",
            "chill", "playful", "no opinion", "no", "a nap on the couch",
            "chewed shoes",
        ],
        "expect": [
            'I do not have "condo" on the list. Pick one of the three.',
            'I do not have "tent" on the list. Pick one of the three.',
            'I do not have "chill" on the list. Pick one of the three.',
            "An apartment narrows things down, but it does not rule much out.",
            "Being around a lot is the single best thing you can offer.",
            "Playful is easy to find here. Loud, but easy.",
            "First time is exciting. We will start you somewhere gentle.",
        ],
    },
    {
        "name": "Error case: user answers nothing",
        "note": "Enter pressed on every free-text question, and once on each menu "
                "before a real answer. The program does not crash, but the closing "
                "summary prints gaps where the answers should be.",
        "inputs": ["Ana", "", "house", "", "", "", "calm", "", "", "", ""],
        "expect": [
            'I do not have "" on the list. Pick one of the three.',
            "A house gives us plenty to work with.",
            "I will assume your days are a mix.",
            "Either way, we will figure it out together.",
            "House,  to work with, and you are .",
        ],
    },
]


def run(inputs):
    """Run the program with a fixed random seed and return its output."""
    wrapper = (
        f"import random; random.seed({SEED})\n"
        f"exec(open({PROGRAM!r}).read())\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", wrapper],
        input="\n".join(inputs) + "\n",
        capture_output=True,
        text=True,
    )
    return result.stdout, result.stderr


failures = 0
for case in CASES:
    out, err = run(case["inputs"])
    missing = [line for line in case["expect"] if line not in out]
    unwanted = [line for line in case.get("reject", []) if line in out]
    ok = not missing and not unwanted and not err
    print(f"[{'PASS' if ok else 'FAIL'}] {case['name']}")
    print(f"       {case['note']}")
    if missing or unwanted or err:
        failures += 1
        for line in missing:
            print(f"       MISSING: {line}")
        for line in unwanted:
            print(f"       SHOULD NOT APPEAR: {line}")
        if err:
            print(f"       STDERR: {err.strip().splitlines()[-1]}")
    print()

total = len(CASES)
print(f"{total - failures} of {total} test cases passed.")
sys.exit(1 if failures else 0)
