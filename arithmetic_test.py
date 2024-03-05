import random


def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
    elif level == 2:

        num = random.randint(11, 29)
        question = f"{num}^2"
        answer = num ** 2
    else:
        return None, None

    return question, answer


def main():
    correct_answers = 0
    total_questions = 5

    while True:
        try:
            level = int(input(
                "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    for _ in range(total_questions):
        question, correct_answer = generate_question(level)
        print(question)

        while True:
            user_answer = input("> ")
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/{total_questions}.")

    save_result = input("Would you like to save the result? Enter yes or no.\n> ")
    if save_result.lower() in ['yes', 'y']:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(
                f"{name}: {correct_answers}/{total_questions} in level {level} ({'simple operations with numbers 2-9' if level == 1 else 'integral squares of 11-29'}).\n")
        print("The results are saved in 'results.txt'.")


if __name__ == "__main__":
    main()
