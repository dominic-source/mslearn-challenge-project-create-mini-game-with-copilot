import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return get_user_choice()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return None
    elif user_choice == "rock":
        return True if computer_choice == "scissors" else False
    elif user_choice == "paper":
        return True if computer_choice == "rock" else False
    elif user_choice == "scissors":
        return True if computer_choice == "paper" else False

def play_game():
    play = input("Do you want to play a game of rock, paper, scissors? (yes/no): ").lower()
    if play != "yes":
        return
    count = {
        "user": 0,
        "computer": 0,
        "tie": 0
    }
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        who_won = determine_winner(user_choice, computer_choice)
        if who_won == None:
            print("It's a tie!")
            count["tie"] += 1
        elif who_won:
            print("You won!")
            count["user"] += 1
        else:
            print("Computer won!")
            count["computer"] += 1
        play = input("Do you want to play another round of rock, paper, scissors? (yes/no): ").lower()
        if play != "yes":
            break
    print(f"User: {count['user']}, Computer: {count['computer']}, Tie: {count['tie']}")
play_game()
