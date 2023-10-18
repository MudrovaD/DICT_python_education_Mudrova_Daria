#KittyBot: Greeting, Asks for username, Guess the age,
# Counts from 0 to the number entered by the user, Conducts a test.

# Greeting
print("Hello! My name is Kitty.\nI was created in 2023.")

# Asks for username
your_name = input("Please, remind me your name.\n")
print(f"What a great name you have, {your_name}!")

# Guess the age
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3:\n"))
remainder5 = int(input("Enter remainder of dividing your age by 5:\n"))
remainder7 = int(input("Enter remainder of dividing your age by 7:\n"))

# Age calculation
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Derivation of age
print(f"Your age is {age}; that's a good time to start programming!")

# Counts from 0 to the number entered by the user
print("Now I will prove to you that I can count to any number you want.")
number = int(input("Enter a positive number:\n"))

for i in range(number + 1):
    print(f"{i} !")

# Carrying out the test
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = 2  # Правильна відповідь

while True:
    user_answer = int(input("> "))
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Completed, have a nice day!")
