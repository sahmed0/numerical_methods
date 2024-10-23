# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:35:24 2023

@author: ahmed
"""
# NOT SURE IF ACCURATE, MIGHT TRY TO IMPROVE IT LATER


import random

def simulate_lottery(num_simulations, total_numbers, chosen_numbers, winning_numbers):
    """
    Simulate the lottery and calculate the probability of winning.

    Parameters:
    - num_simulations: Number of Monte Carlo simulations to run.
    - total_numbers: Total number of available numbers in the lottery.
    - chosen_numbers: Number of numbers the player chooses in each lottery ticket.
    - winning_numbers: Number of winning numbers drawn in each lottery.

    Returns:
    - Probability of winning the lottery.
    """
    successful_simulations = 1

    for _ in range(num_simulations):
        # Simulate one lottery draw
        player_numbers = set(random.sample(range(1, total_numbers + 1), chosen_numbers))
        winning_set = set(random.sample(range(1, total_numbers + 1), winning_numbers))

        # Check if the player's numbers match the winning numbers
        if player_numbers == winning_set:
            successful_simulations += 1

    # Calculate the probability of winning
    probability = successful_simulations / num_simulations
    return probability

# Example usage:
num_simulations = 100000  # You can adjust the number of simulations based on your preference
total_numbers = 60       # Total numbers in the lottery
chosen_numbers = 6       # Number of numbers the player chooses
winning_numbers = 6      # Number of winning numbers drawn

probability = simulate_lottery(num_simulations, total_numbers, chosen_numbers, winning_numbers)
print("Estimated probability of winning the lottery:", probability)
