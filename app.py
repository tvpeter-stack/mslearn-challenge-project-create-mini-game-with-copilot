# write 'hello world' to the console
print('hello world')

import random

def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    while True:
        print("Enter your move: (rock, paper, scissors)")
        player_move = input().lower()
        if player_move not in options:
            print("Invalid move. Please try again.")
            continue
        computer_move = random.choice(options)
        print(f"Computer plays {computer_move}.")
        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "scissors" and computer_move == "paper") or \
             (player_move == "paper" and computer_move == "rock"):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print(f"Score: Player {player_score}, Computer {computer_score}")
        print("Do you want to play again? (yes or no)")
        play_again = input().lower()
        if play_again != "yes":
            break

play_game()
