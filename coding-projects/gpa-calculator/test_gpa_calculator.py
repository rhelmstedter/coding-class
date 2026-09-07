"""Test harness for gpa_calculator.py.

Runs every test case from the specification through the real program and
compares the output lines against what the specification promises.
"""

import subprocess
import sys

PROGRAM = "gpa_calculator.py"

CASES = [
    {
        "name": "Typical case: A, B, A, B, C, A",
        "inputs": ["4", "3", "4", "3", "2", "4"],
        "expected": [
            "You earned 20 grade points in 6 classes.",
            "Your GPA is 3.33.",
        ],
    },
    {
        "name": "Every point value used: 3, 2, 4, 1, 0, 3",
        "inputs": ["3", "2", "4", "1", "0", "3"],
        "expected": [
            "You earned 13 grade points in 6 classes.",
            "Your GPA is 2.17.",
        ],
    },
    {
        "name": "Boundary case: straight A's (highest possible)",
        "inputs": ["4", "4", "4", "4", "4", "4"],
        "expected": [
            "You earned 24 grade points in 6 classes.",
            "Your GPA is 4.0.",
        ],
    },
    {
        "name": "Boundary case: straight F's (lowest possible)",
        "inputs": ["0", "0", "0", "0", "0", "0"],
        "expected": [
            "You earned 0 grade points in 6 classes.",
            "Your GPA is 0.0.",
        ],
    },
]

# Typing a letter grade instead of its point value should stop the program.
ERROR_CASE = {
    "name": "Error case: a letter is not a number",
    "inputs": ["A", "3", "4", "3", "2", "4"],
    "expected_error": "ValueError: invalid literal for int() with base 10: 'A'",
}


def run(inputs):
    """Run the program with the given answers and return (output_lines, stderr)."""
    result = subprocess.run(
        [sys.executable, PROGRAM],
        input="\n".join(inputs) + "\n",
        capture_output=True,
        text=True,
    )
    if "You earned" not in result.stdout:
        return [], result.stderr
    tail = result.stdout.split("You earned")[-1]
    return ("You earned" + tail).strip().split("\n"), result.stderr


failures = 0
for case in CASES:
    actual, _ = run(case["inputs"])
    ok = actual == case["expected"]
    print(f"[{'PASS' if ok else 'FAIL'}] {case['name']}")
    print(f"       input: {', '.join(case['inputs'])}")
    for line in actual:
        print(f"       {line}")
    if not ok:
        failures += 1
        for line in case["expected"]:
            print(f"       expected: {line}")
    print()

_, stderr = run(ERROR_CASE["inputs"])
ok = ERROR_CASE["expected_error"] in stderr
print(f"[{'PASS' if ok else 'FAIL'}] {ERROR_CASE['name']}")
print(f"       input: {', '.join(ERROR_CASE['inputs'])}")
print(f"       {ERROR_CASE['expected_error']}")
if not ok:
    failures += 1
print()

total = len(CASES) + 1
print(f"{total - failures} of {total} test cases passed.")
sys.exit(1 if failures else 0)
