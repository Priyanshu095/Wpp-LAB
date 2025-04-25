import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'draw'
        if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return 'user'
        else:
            self.computer_wins += 1
            return 'computer'

    def check_winner(self):
        if self.user_wins > self.computer_wins:
            return 'User wins the game!'
        elif self.computer_wins > self.user_wins:
            return 'Computer wins the game!'
        else:
            return 'The game is a draw!'

# User interaction
rounds = int(input("Enter the number of rounds: "))
rps = RockPaperScissors(rounds)
for i in range(rps.rounds):
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = rps.get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    winner = rps.find_winner(user_choice, computer_choice)
    print(f"Round winner: {winner}")
print(rps.check_winner())
