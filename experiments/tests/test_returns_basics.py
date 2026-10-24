"""Behavioral tests for the introductory synthetic-price exercise."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from returns_basics import simple_returns


class SimpleReturnsTests(unittest.TestCase):
    def test_known_consecutive_returns(self):
        actual = simple_returns([100, 110, 99])
        self.assertAlmostEqual(actual[0], 0.10)
        self.assertAlmostEqual(actual[1], -0.10)

    def test_equal_percentage_changes_at_different_price_levels(self):
        self.assertAlmostEqual(simple_returns([100, 102])[0], simple_returns([200, 204])[0])

    def test_unchanged_prices(self):
        self.assertEqual(simple_returns([100, 100, 100]), [0.0, 0.0])

    def test_at_least_two_prices_required(self):
        for prices in ([], [100]):
            with self.subTest(prices=prices), self.assertRaises(ValueError):
                simple_returns(prices)

    def test_invalid_prices_rejected(self):
        for invalid in (0, -1, float("nan"), float("inf")):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                simple_returns([100, invalid])


if __name__ == "__main__":
    unittest.main()
