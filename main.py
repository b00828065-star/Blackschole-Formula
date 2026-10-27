#main.py

from src.black_scholes import black_scholes_call, black_scholes_put
from src.monte_carlo import monte_carlo_call, monte_carlo_put

def main():
    
    S0 = float(input("Enter the value of S0 (current stock price)"))
    print("S0=",S0)
    K = float(input("Enter the value of K (stike price/ future purchase price)"))
    print("K=",K)
    r = float(input("Enter the value of r (risk-free interest rate)"))
    print("r=",r)
    sigma = float(input("Enter the value of sigma (volatility)"))
    print("sigma=",sigma)
    T = float(input("Enter the value of T (time to expiry, in years)"))
    print("T=",T)
    
    bs_call = black_scholes_call(S0, K, r, sigma, T)
    mc_call = monte_carlo_call(S0, K, r, sigma, T, n_sims=100_000, seed=42)

    bs_put = black_scholes_put(S0, K, r, sigma, T)
    mc_put = monte_carlo_put(S0, K, r, sigma, T, n_sims=100_000, seed=42)

    print(f"Black-Scholes Call : {bs_call:.4f}")
    print(f"Monte Carlo Call    : {mc_call:.4f}")
    print(f"Black-Scholes Put  : {bs_put:.4f}")
    print(f"Monte Carlo Put    : {mc_put:.4f}")

if __name__ == "__main__":
    main()