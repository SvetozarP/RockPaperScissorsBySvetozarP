from colorama import Fore
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

win: int = 0
draw: int = 0
lose: int = 0

player_move = input("Choose [r]ock, [p]aper or [s]cissors or [q]uit: ")

while player_move != "q":

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    elif player_move == "q":
        break
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 3:
        computer_move = scissors
    else:
        computer_move = paper

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.LIGHTGREEN_EX + "You win!" + Fore.RESET)
        win += 1
        print("Scores so far: " + Fore.LIGHTGREEN_EX + f"Win: {win} " + Fore.YELLOW + f"Draw: {draw} " + Fore.RED
              + f"Lose {lose} " + Fore.RESET)
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!" + Fore.RESET)
        draw += 1
        print("Scores so far: " + Fore.LIGHTGREEN_EX + f"Win: {win} " + Fore.YELLOW + f"Draw: {draw} " + Fore.RED
              + f"Lose {lose} " + Fore.RESET)
    else:
        print(Fore.RED + "You lose!" + Fore.RESET)
        lose += 1
        print("Scores so far: " + Fore.LIGHTGREEN_EX + f"Win: {win} " + Fore.YELLOW + f"Draw: {draw} " + Fore.RED
              + f"Lose {lose} " + Fore.RESET)

    player_move = input(Fore.RESET + "Choose [r]ock, [p]aper or [s]cissors or [q]uit: ")