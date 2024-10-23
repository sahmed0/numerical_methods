# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:01:46 2023

@author: ahmed
"""

import random

def monte_carlo_bayes_simulation(num_simulations, prior_prob_A, prob_B_given_A, prob_B_given_not_A):
    """
    Simulate a scenario to estimate the probability of event A happening given that event B has happened using Bayes' theorem.

    Parameters:
    - num_simulations: Number of Monte Carlo simulations to run.
    - prior_prob_A: Prior probability of event A happening.
    - prob_B_given_A: Probability of event B happening given that event A has happened.
    - prob_B_given_not_A: Probability of event B happening given that event A has not happened.

    Returns:
    - Estimated probability of event A happening given that event B has happened.
    """
    num_A_and_B = 0
    num_B = 0

    for _ in range(num_simulations):
        # Simulate whether event A happens based on prior probability
        event_A = random.uniform(0, 1) < prior_prob_A

        # Simulate whether event B happens given the outcome of event A
        if event_A:
            event_B = random.uniform(0, 1) < prob_B_given_A
        else:
            event_B = random.uniform(0, 1) < prob_B_given_not_A

        # Count occurrences of B and A∩B
        if event_B:
            num_B += 1
            if event_A:
                num_A_and_B += 1

    # Calculate the estimated probability of A|B using Bayes' theorem
    if num_B == 0:
        return 0

    probability_A_given_B = (num_A_and_B / num_B) * prior_prob_A / (prob_B_given_A * prior_prob_A + prob_B_given_not_A * (1 - prior_prob_A))

    return probability_A_given_B

# Example usage:
num_simulations = 100000  # You can adjust the number of simulations based on your preference
prior_prob_A = 0.3       # Prior probability of event A happening
prob_B_given_A = 0.8     # Probability of event B happening given that event A has happened
prob_B_given_not_A = 0.2 # Probability of event B happening given that event A has not happened

probability_A_given_B = monte_carlo_bayes_simulation(num_simulations, prior_prob_A, prob_B_given_A, prob_B_given_not_A)
print(f"Estimated probability of event A happening given that event B has happened: {probability_A_given_B:.4f}")
