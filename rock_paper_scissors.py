"""Game "Rock, scissors, paper"""
import random


def get_computer_choice(options):
    return random.choice(options)


def get_winner(user_choice, computer_choice, options):
    winning_options = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})"
    elif winning_options[user_choice] == computer_choice:
        return f"Well done. The computer chose {computer_choice} and failed"
    else:
        return f"Sorry, but the computer chose {computer_choice}"


def update_rating(username, points):
    ratings = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                name, rating = line.strip().split()
                ratings[name] = int(rating)
    except FileNotFoundError:
        print("Rating file not found. Creating new rating file.")
        open("rating.txt", "w").close()  # Create an empty rating file
        ratings[username] = 0
    else:
        ratings[username] = ratings.get(username, 0) + points

    with open("rating.txt", "w") as file:
        for name, rating in ratings.items():
            file.write(f"{name} {rating}\n")


def get_user_options():
    options_input = input("Enter your options (separated by commas) or press Enter for default (rock,paper,scissors): ")
    options = options_input.split(",") if options_input else ["rock", "paper", "scissors"]
    return options


def main():
    username = input("Enter your name: ").strip()
    print(f"Hello, {username}")

    ratings = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                name, rating = line.strip().split()
                ratings[name] = int(rating)
    except FileNotFoundError:
        print("Rating file not found. Creating new rating file.")
        open("rating.txt", "w").close()  # Create an empty rating file
        ratings[username] = 0
    else:
        ratings[username] = ratings.get(username, 0)

    user_rating = ratings.get(username, 0)
    print(f"Your rating: {user_rating}")

    options = get_user_options()
    print("Okay, let's start")

    while True:
        user_input = input("Enter your choice or type '!exit' to quit: ").lower()

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {user_rating}")
        elif user_input in options:
            computer_choice = get_computer_choice(options)
            result = get_winner(user_input, computer_choice, options)
            print(result)

            if "Win" in result:
                update_rating(username, 100)
            elif "Draw" in result:
                update_rating(username, 50)
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
