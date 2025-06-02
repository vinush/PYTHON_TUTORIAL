import random


def getChoice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissor"
    else:
        return "Not a valid choice"


def game_version():
    print("game version: 1.2.3")


def main():
    print("welcome to rock, paper,scissor Game")
    print("[R] = Rock, [P] = Paper, [S]=Scissor and [Q]=Quit")

    choices = ["R", "P", "S"]
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f"Game #{counter}. please enter your choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print("Thank for joining! Have nice a day :D")
            game_version()
            game_on = False
        else:
            random_index = random.randint(0, 2)
            computer_choices = choices[random_index]

            print(
                f"you selected {getChoice(user_choice)} vs computer choice is {getChoice(computer_choices)}"
            )

            # winning Rules:
            if user_choice == "R" and computer_choices == "S":
                print("Congrats, you win. Rock beats Scissor")
            elif user_choice == "P" and computer_choices == "R":
                print("Congrats you win. Papper covers Rock")
            elif user_choice == "S" and computer_choices == "P":
                print("Congrats, you win. Scissor cuts Paper")
            elif user_choice == "R" and computer_choices == "P":
                print("So sorry, computer win. Paper covers Rock")
            elif user_choice == "P" and computer_choices == "S":
                print("So sorry, you lost. Scissor cuts Paper")
            elif user_choice == "S" and computer_choices == "R":
                print("So sorry, you lost. Rock beats Scissor")
            elif user_choice == computer_choices:
                print(
                    f"Wow its Draw. Both you and computer is selected {getChoice(user_choice)}"
                )
            else:
                print("Invalid option: Please enter[R,P,S,Q] option")

            counter += 1
        print("-" * 40)


if __name__ == "__main__":
    main()
