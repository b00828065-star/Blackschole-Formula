from math import isfinite


def validate_inputs(S0, K, r, sigma, T):
    values = (S0, K, r, sigma, T)
    if not all(isfinite(value) for value in values):
        raise ValueError("All option parameters must be finite.")
    if S0 <= 0 or K <= 0:
        raise ValueError("S0 and K must be positive.")
    if sigma < 0:
        raise ValueError("sigma must be non-negative.")
    if T < 0:
        raise ValueError("T must be non-negative.")
