"""Pencils"""
import random
import sys

def get_number_of_pencils():
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n> "))
            if num_pencils > 0:
                return num_pencils
            else:
                print("The number of pencils should be positive.")
        except ValueError:
            print("The number of pencils should be numeric.")

def get_first_player_name():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        first_player = input("Who will be the first (John, Jack):\n> ").strip()
        if first_player.lower() in ['john', 'jack']:
            return first_player.capitalize()
        else:
            print("Choose between 'John' and 'Jack'.")
            attempts += 1
    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")
    sys.exit()

def print_pencils_and_turn(num_pencils, player):
    print("|" * num_pencils)
    print(f"{player}'s turn:")

def take_pencils(num_pencils, player):
    if player == 'Jack':
        if num_pencils % 4 == 1 or num_pencils % 4 == 2:
            return random.choice([1, 2, 3])
        elif num_pencils % 4 == 0:
            return min(3, num_pencils)  # New strategy to leave 4, 8, 12... pencils
        else:
            return num_pencils % 4
    else:
        while True:
            try:
                pencils_to_take = int(input(f"{player}, how many pencils would you like to take? (1-3)\n> "))
                if 1 <= pencils_to_take <= min(3, num_pencils):
                    return pencils_to_take
                else:
                    print("Invalid input. Choose '1', '2' or '3'.")
            except ValueError:
                print("Invalid input. Choose '1', '2' or '3'.")

def determine_winner(current_player, pencils_taken):
    if pencils_taken == 0:
        return f"{current_player} won by taking the last pencil!"
    else:
        return f"{current_player} won! (Strategy: {pencils_taken} pencil(s) taken)"

def main():
    num_pencils = get_number_of_pencils()
    current_player = get_first_player_name()

    while num_pencils > 0:
        print_pencils_and_turn(num_pencils, current_player)

        pencils_to_take = take_pencils(num_pencils, current_player)
        num_pencils -= pencils_to_take

        if num_pencils == 0:
            print(determine_winner(current_player, pencils_to_take))
            break
        elif num_pencils < 0:
            print("Invalid game state. Exiting.")
            sys.exit()
        else:
            print(f"Pencils remaining: {num_pencils}")
            user_input = input("Do you want to continue? (yes/no)\n> ").lower()
            if user_input != 'yes':
                print(f"{current_player} exited the game.")
                sys.exit()
            current_player = 'Jack' if current_player == 'John' else 'John'

    print("Game over!")

if __name__ == "__main__":
    main()

