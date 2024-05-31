import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(rounds):
    player_score = 0
    computer_score = 0
    round_number = 1

    while round_number <= rounds:
        print(f"Round {round_number} of {rounds}")
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}\n")

        if player_score >= (rounds // 2) + 1 or computer_score >= (rounds // 2) + 1:
            break
        
        round_number += 1

    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > player_score:
        print("Sorry, the computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    num_rounds = int(input("How many rounds do you want to play? (3 or 5): "))
    play_game(num_rounds)
