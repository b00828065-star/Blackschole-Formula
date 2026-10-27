# src/black_scholes.py

import math
from math import log, sqrt, exp
from scipy.stats import norm

def black_scholes_call(S0, K, r, sigma, T):
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call = S0 * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    return call

def black_scholes_put(S0, K, r, sigma, T):
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    put = K * exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return put