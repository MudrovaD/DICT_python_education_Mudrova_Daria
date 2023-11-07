"""hangman:gallows game"""
import random

word_list = ["python", "java", "javascript", "php"]


def choose_word():
    return random.choice(word_list)


def play_hangman():
    while True:
        print("HANGMAN")
        choice = input('Type "play" to play the game, "exit" to quit: > ')

        if choice == "play":
            secret_word = choose_word()
            guessed_word = ["_"] * len(secret_word)
            attempts = 8  # Кількість спроб
            guessed_letters = []  # Список вже вгаданих літер

            print("Welcome to the game!")

            while attempts > 0:
                print("".join(guessed_word))
                guess = input("Input a letter: > ").lower()

                if len(guess) != 1:
                    print("You should input a single letter")
                elif not guess.isalpha() or not guess.islower():
                    print("Please enter a lowercase English letter")
                elif guess in guessed_letters:
                    print("You've already guessed this letter")
                elif guess in secret_word:
                    guessed_letters.append(guess)
                    for i in range(len(secret_word)):
                        if secret_word[i] == guess:
                            guessed_word[i] = guess
                    if "_" not in guessed_word:
                        print(f"Congratulations! You guessed the word: {secret_word}")
                        break
                    else:
                        print("No improvements")
                else:
                    attempts -= 1
                    guessed_letters.append(guess)
                    print(f"That letter doesn't appear in the word. You have {attempts} attempts left.")

            if attempts == 0:
                print(f"Thanks for playing! You lost!")
        elif choice == "exit":
            break
        else:
            print('Invalid choice. Please enter "play" or "exit".')


if __name__ == "__main__":
    play_hangman()



