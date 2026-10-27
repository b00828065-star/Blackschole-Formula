# Black-Scholes & Monte Carlo Option Pricing

Calculate European call and put prices with the Black-Scholes formula and a
Monte Carlo simulation.

## Overview

This project implements two fundamental option pricing techniques used in quantitative finance:

Black-Scholes analytical model
Monte Carlo simulation under the Black-Scholes framework

The objective is to compare a closed-form pricing solution with a numerical simulation approach and better understand the probabilistic foundations of option pricing.

This project was developed as a personal learning initiative to strengthen my understanding of:

Derivative pricing
Brownian motion
Risk-neutral valuation
Quantitative finance programming in Python


# Financial modelling
## Black-Scholes Model

The Black-Scholes model provides a closed form solution for pricing European options.

The model assumes that the underlying asset follows a Geometric Brownian Motion:

dSt=μStdt+σStdWt

Under the risk-neutral measure:

dSt=rStdt+σStdWt​

The call option price is given by:

C=S0*N(d1)−Ke−rTN(d2)

where:

d1=(ln⁡(S0/K)+((r+σ^2)/2)T)σ*T^0.5 

d2=d1−σ*T^0.5​


## Monte Carlo Simulation

Instead of using a closed-form formula, Monte Carlo simulation generates thousands of possible future asset prices:

ST=S0exp⁡(((r−σ^2)/2)T+σ*(T^0.5)*Z)

with:

Z∼N(0,1)

The option price is estimated as:

Price=(e^−rT)*E[Payof f]

where the expectation is approximated using simulated paths.
