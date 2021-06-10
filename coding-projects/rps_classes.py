from collections import defaultdict
import csv
import random
import os
import time


class Action:
    def __init__(self, action, value):
        self.action = action
        self.value = value


class Player:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins


# parses the csv for possible actions and possible victories
victories = defaultdict(list)
with open("data/battle-table.csv", "r") as csvfile:
    headers = csv.DictReader(csvfile).fieldnames
    actions = [
        Action(action, value) for value, action in enumerate(headers) if value > 0
    ]

    for line in csv.DictReader(csvfile, fieldnames=headers):
        action = line["Attacker"]
        for fieldname in headers:
            if line[fieldname] == "win":
                victories[action].append(fieldname)


def main():
    print_header()
    name = input("Enter your name: ")
    player1 = Player(name)
    player2 = Player("Computer")
    BEST_OF_NUM = 3
    print(f"Welcome {player1.name}. Let's play best of {BEST_OF_NUM} rounds.")
    game_loop(player1, player2, BEST_OF_NUM)
    get_final_score(player1, player2, BEST_OF_NUM)


def print_header():
    print("=" * 30)
    print("  15-way Rock Paper Scissors")
    print("=" * 30)


def game_loop(player1, player2, BEST_OF_NUM):
    while max([player1.wins, player2.wins]) < BEST_OF_NUM - 1:
        try:
            p1_turn = get_user_selection()
        except ValueError:
            range_str = f"[1, {len(actions)}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        print(f"You choose {p1_turn.action}")
        print("The computer is thinking.")
        time.sleep(0.5)
        print("1...")
        time.sleep(0.25)
        print("2...")
        time.sleep(0.25)
        print("3...")
        time.sleep(0.25)
        p2_turn = get_computers_selection()
        print(f"The Computer choose {p2_turn.action}")
        determine_winner(p1_turn, p2_turn, player1, player2, victories)
        get_score(player1, player2)
        input("Press ENTER to move to the next round.")
        os.system("cls" if os.name == "nt" else "clear")
        print_header()


def get_user_selection():
    choices = [f"[{action.value}] {action.action}" for action in actions]
    choices_str = "\n".join(choices)
    selection = int(input(f"\nChoose your move:\n\n{choices_str}\n"))
    action = actions[selection - 1]
    return action


def get_computers_selection():
    return random.choice([action for action in actions])


def determine_winner(p1_turn, p2_turn, player1, player2, victories):
    defeats = victories[p1_turn.action]
    if p1_turn.action == p2_turn.action:
        print(f"\nBoth players selected {p1_turn.action}. It's a tie!")
    elif p2_turn.action in defeats:
        print(f"\n{p1_turn.action} beats {p2_turn.action}! You win!")
        player1.wins += 1
    else:
        print(f"\n{p2_turn.action} beats {p1_turn.action}! You lose.")
        player2.wins += 1


def get_score(player1, player2):
    print(f"\n{player1.name} has won {player1.wins} times.")
    print(f"{player2.name} has won {player2.wins} times.", end="\n\n")


def get_final_score(player1, player2, BEST_OF_NUM):
    print(f"\n{player1.name} won {player1.wins} times.")
    print(f"{player2.name} won {player2.wins} times.", end="\n\n")
    if player1.wins == BEST_OF_NUM - 1:
        print("You won the match! Thanks for playing!")
    if player2.wins == BEST_OF_NUM - 1:
        print("The Computer won the math! Better luck next time.")


if __name__ == "__main__":
    main()
