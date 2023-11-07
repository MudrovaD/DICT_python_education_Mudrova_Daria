"""joint cost sharing programs"""
import random

num_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num_of_friends):
        friend_name = input()
        friends[friend_name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    if num_of_friends > 0:
        amount_per_friend = round(total_amount / num_of_friends, 2)
    else:
        amount_per_friend = 0

    for friend in friends:
        friends[friend] = amount_per_friend

    lucky_choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if lucky_choice.lower() == "yes":
        lucky_friend = random.choice(list(friends.keys()))

        for friend in friends:
            if friend != lucky_friend:
                friends[friend] = round(friends[friend] + amount_per_friend, 2)

        friends[lucky_friend] = 0

        print(f"{lucky_friend} is the lucky one!")
    else:
        print("No one is going to be lucky")

    print(friends)

