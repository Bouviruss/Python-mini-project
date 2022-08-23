import random
user_win = 0
computer_win = 0

options = ["paper", "rock", "scissors"]

while True:
    user_input = input("Your Guessing is paper/scissors/rock or Q to quit: ").lower() #input guessing here and quit game
    if user_input == "q":
        break
    if user_input not in ["paper", "rock", "scissors"]:
        continue
    random_number = random.randint(0, 2) # paper: 0 , rock: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won! ")
        user_win += 1

    if user_input == "paper" and computer_pick == "rock":
        print("You won! ")
        user_win += 1

    if user_input == "scissors" and computer_pick == "paper":
        print("You won! ")
        user_win += 1
    else:
        print("You lost! ")
        computer_win += 1
print("you won", user_win, "times.")
print("The computer win", computer_win, "times.")

print("Goodbye!")
