# Python experiments

Small exercises using synthetic data and the Python standard library.

## Simple percentage returns

[returns_basics.py](returns_basics.py) calculates the fractional change between consecutive synthetic prices:

`return = current_price / previous_price - 1`

A move from 100 to 102 is 0.02, or 2%. A move from 200 to 204 is also 2%, although its absolute price change is twice as large.

Run from the repository root:

```sh
python3 experiments/returns_basics.py
python3 -m unittest discover -s experiments/tests -v
```

The function rejects too-short inputs and nonpositive or nonfinite prices. The tests cover known returns, unchanged prices and invalid inputs. These are invented prices, not platform data or a trading strategy. This exercise does not model dividends, corporate actions, transaction costs or portfolio construction.

Next useful exercise: compound these returns and compare the ending value with the original price ratio.
