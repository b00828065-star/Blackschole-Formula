from math import exp, sqrt
from random import Random

from src._validation import validate_inputs


def _monte_carlo_price(S0, K, r, sigma, T, n_sims, seed, is_call):
    validate_inputs(S0, K, r, sigma, T)
    if not isinstance(n_sims, int) or isinstance(n_sims, bool) or n_sims <= 0:
        raise ValueError("n_sims must be a positive integer.")

    if T == 0 or sigma == 0:
        terminal_price = S0 * exp(r * T)
        payoff = (
            max(terminal_price - K, 0.0)
            if is_call
            else max(K - terminal_price, 0.0)
        )
        return exp(-r * T) * payoff

    rng = Random(seed)
    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * sqrt(T)
    discounted_payoff_sum = 0.0

    for _ in range(n_sims):
        terminal_price = S0 * exp(drift + diffusion * rng.normalvariate(0.0, 1.0))
        payoff = (
            max(terminal_price - K, 0.0)
            if is_call
            else max(K - terminal_price, 0.0)
        )
        discounted_payoff_sum += payoff

    return exp(-r * T) * discounted_payoff_sum / n_sims


def monte_carlo_call(S0, K, r, sigma, T, n_sims=100_000, seed=None):
    """Estimate a European call price using Monte Carlo simulation."""
    return _monte_carlo_price(S0, K, r, sigma, T, n_sims, seed, is_call=True)


def monte_carlo_put(S0, K, r, sigma, T, n_sims=100_000, seed=None):
    """Estimate a European put price using Monte Carlo simulation."""
    return _monte_carlo_price(S0, K, r, sigma, T, n_sims, seed, is_call=False)
