# Black-Scholes Formula

Calculate European call and put prices with the Black-Scholes formula and a
Monte Carlo simulation.

## Run

From the project directory, run:

```sh
python3 main.py
```

The project uses only the Python standard library. Monte Carlo prices are
estimates and can differ slightly from the Black-Scholes prices; the fixed
seed in `main.py` makes the displayed estimates reproducible.