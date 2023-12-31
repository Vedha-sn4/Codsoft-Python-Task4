import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins. Better luck next time!"

def print_choices(user_choice, computer_choice):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\n===== Rock-Paper-Scissors Game =====")
        user_choice = input("Choose rock, paper, or scissors: ").lower()


        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
            print("Congratulations! You win!")
        elif "Computer wins" in result:
            computer_score += 1
            print("Computer wins. Better luck next time!")

        print(f"Scores - You: {user_score} | Computer: {computer_score}")

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        if play_again != 'yes':
            print("\nGame ended. Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print(f"Congratulations! You win!")
            elif user_score < computer_score:
                print("Computer wins. Better luck next time!")
            else:
                print("It's a tie!")
            break

# Run the rock-paper-scissors game
rock_paper_scissors()


