# src/monte_carlo.py
import math
import numpy  as np

def monte_carlo_call(S0, K, r, sigma, T, n_sims=100_000, seed=None):
    
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.normal(0.0, 1.0, n_sims)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z)

    payoffs = np.maximum(ST - K, 0.0)
    discounted_payoff_mean = math.exp(-r * T) * np.mean(payoffs)
    return discounted_payoff_mean


def monte_carlo_put(S0, K, r, sigma, T, n_sims=100_000, seed=None):
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.normal(0.0, 1.0, n_sims)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z)

    payoffs = np.maximum(K - ST, 0.0)
    discounted_payoff_mean = math.exp(-r * T) * np.mean(payoffs)
    return discounted_payoff_mean


