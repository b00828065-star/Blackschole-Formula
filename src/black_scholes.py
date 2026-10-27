from math import exp, log, sqrt
from statistics import NormalDist

from src._validation import validate_inputs

_NORMAL = NormalDist()


def black_scholes_call(S0, K, r, sigma, T):
    """Return the Black-Scholes price of a European call option."""
    validate_inputs(S0, K, r, sigma, T)
    if T == 0 or sigma == 0:
        return exp(-r * T) * max(S0 * exp(r * T) - K, 0.0)

    sigma_sqrt_T = sigma * sqrt(T)
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / sigma_sqrt_T
    d2 = d1 - sigma_sqrt_T
    return S0 * _NORMAL.cdf(d1) - K * exp(-r * T) * _NORMAL.cdf(d2)


def black_scholes_put(S0, K, r, sigma, T):
    """Return the Black-Scholes price of a European put option."""
    validate_inputs(S0, K, r, sigma, T)
    if T == 0 or sigma == 0:
        return exp(-r * T) * max(K - S0 * exp(r * T), 0.0)

    sigma_sqrt_T = sigma * sqrt(T)
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / sigma_sqrt_T
    d2 = d1 - sigma_sqrt_T
    return K * exp(-r * T) * _NORMAL.cdf(-d2) - S0 * _NORMAL.cdf(-d1)
