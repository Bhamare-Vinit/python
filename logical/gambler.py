import random

def gambler_simulation(stake, goal, num_trials):
    wins = 0  # Counter for number of wins
    total_bets = 0  # Counter for total number of bets

    for _ in range(num_trials):
        current_stake = stake
        while current_stake > 0 and current_stake < goal:
            total_bets += 1  # Increment total bets for each bet
            if random.random() < 0.5:
                current_stake += 1  # Win $1
            else:
                current_stake -= 1  # Lose $1

        if current_stake == goal:
            wins += 1  # Increment wins if goal is reached

    win_percentage = (wins / num_trials) * 100  # Calculate win percentage
    loss_percentage = 100 - win_percentage  # Calculate loss percentage

    return wins, total_bets, win_percentage, loss_percentage

# Main code
stake = int(input("Enter the starting stake: "))
goal = int(input("Enter the goal amount: "))
num_trials = int(input("Enter the number of trials: "))

wins, total_bets, win_percentage, loss_percentage = gambler_simulation(stake, goal, num_trials)

print(f"Number of Wins: {wins}")
print(f"Total Bets Made: {total_bets}")
print(f"Percentage of Wins: {win_percentage:.2f}%")
print(f"Percentage of Losses: {loss_percentage:.2f}%")
