import random
lst=["s", "w", "g"]

chance=10
no_of_chances=0
computer_point=0
human_point=0

print("\t\t\t\t\t\t Snake Water Gun Game\n\n")
print("Press\ns for snake\nw for water\ng for gun\n")

while no_of_chances < chance:
    _input=input("Snake Water Gun")
    _random=random.choice(lst)

    if _input == _random:
        print("Tie 0 point to both\n")

    #if user enter s
    elif _input =="s" and _random =="g":
        computer_point = computer_point + 1
        print(f" your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point\n")
        print(f"you has {human_point} and computer has {computer_point} \n")

    elif _input=="s" and _random =="w":
        human_point = human_point + 1
        print(f" your guess is {_input} and computer guess is {_random}")
        print("You wins 1 point")
        print(f" you has {human_point} and computer has {computer_point}")

    # if user enter w
    elif _input =="w" and _random =="g":
        human_point = human_point + 1
        print(f" your guess {_input} and computer guess {_random}\n")
        print("human wins 1 point\n")
        print(f"you has {human_point} and computer has {computer_point} \n")

    elif _input=="w" and _random =="s":
        computer_point = computer_point + 1
        print(f" your guess is {_input} and computer guess is {_random}")
        print("Computer wins 1 point")
        print(f" you has {human_point} and computer has {computer_point}")

    # if user enter g
    elif _input =="g" and _random =="s":
        human_point = human_point + 1
        print(f" your guess {_input} and computer guess {_random}\n")
        print("human wins 1 point\n")
        print(f"you has {human_point} and computer has {computer_point} \n")

    elif _input =="g" and _random =="w":
        computer_point = computer_point + 1
        print(f" your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point\n")
        print(f"you has {human_point} and computer has {computer_point} \n")

    else:
        print("Invalid Input Read instructions again\n")

    no_of_chances = no_of_chances + 1
    print(f" {no_of_chances} is left out of {chance}")

print("Game Over")

if computer_point > human_point:
    print("Computer wins")
elif human_point > computer_point:
    print("You won")
else:
    print("Its a Tie")

print(f"You have {human_point} and computer has {computer_point}")