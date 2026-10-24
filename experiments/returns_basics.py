"""Practice simple returns with synthetic prices; no market data required."""

from math import isfinite


def simple_returns(prices):
    """Return consecutive fractional changes for positive finite prices."""
    values = [float(price) for price in prices]
    if len(values) < 2:
        raise ValueError("Provide at least two prices.")
    if any(not isfinite(price) or price <= 0 for price in values):
        raise ValueError("Prices must be positive and finite.")
    return [current / previous - 1 for previous, current in zip(values, values[1:])]


if __name__ == "__main__":
    synthetic_prices = [100, 102, 101, 104]
    print("Synthetic prices:", synthetic_prices)
    print("Consecutive returns:", [f"{value:.2%}" for value in simple_returns(synthetic_prices)])
