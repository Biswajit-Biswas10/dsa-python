"""
Problem Name: Best Time to Buy and Sell Stock

Problem Description:
You are given an integer array "prices" where "prices[i]" is the price of
NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day
in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any
transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10, 1, 5, 6, 7, 1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10, 8, 7, 5, 2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
- 1 <= prices.length <= 100
- 0 <= prices[i] <= 100

Approach:

Algorithm (Greedy — One Pass):
1. Initialise two variables:
   - min_price  = prices[0]   (cheapest buy price seen so far)
   - max_profit = 0           (best profit we can make)
2. Loop from index 1 to n-1, handling two cases:
   - GREEDY BUY:  prices[i] < min_price  → update min_price (found cheaper buy)
   - GREEDY SELL: otherwise              → calculate profit and update max_profit
       - profit = prices[i] - min_price
       - max_profit = max(max_profit, profit)
3. Return max_profit. If no profitable trade exists, it naturally stays 0.

Why Greedy works here:
- A lower buy price is ALWAYS better for any future sell.
- By greedily tracking the minimum price so far, we guarantee the best
  possible buy point for every potential sell day.
- We never need to look back — local optimal leads to global optimal.

Solution: Greedy (One Pass with Running Minimum)
- Time Complexity:  O(n) - single pass through the array
- Space Complexity: O(1) - only two variables, no extra data structures
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Return the maximum profit from buying and selling a stock once.

    Uses a greedy approach: track the minimum price seen so far and
    calculate the best possible profit at each step.

    Args:
        prices: List of stock prices where prices[i] is the price on day i.

    Returns:
        int: Maximum profit achievable. Returns 0 if no profitable trade exists.
    """
    # Track the lowest price seen so far (start with first day as our best buy)
    min_price = prices[0]

    # Track the best profit we can make (0 means no profit yet)
    max_profit = 0

    # Total number of days
    n = len(prices)

    # Loop through every price starting from day 2 (index 1)
    for i in range(1, n):

        # GREEDY BUY: Found a cheaper price? This is our new best buy day
        # e.g. prices = [10, 1, ...] → min_price updates from 10 to 1
        if prices[i] < min_price:
            min_price = prices[i]

        # GREEDY SELL: Today's price is higher, let's check profit
        else:
            # Calculate: "What if I sell today?"
            profit = prices[i] - min_price

            # Keep the better profit: previous best OR today's profit
            max_profit = max(max_profit, profit)

    # Return the best profit found (stays 0 if no profitable trade exists)
    return max_profit


## Test Cases
def test_max_profit():
    """Test cases for max_profit function."""

    # Test 1: Main example — buy at 1, sell at 7
    result = max_profit([10, 1, 5, 6, 7, 1])
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Test 1 passed: Buy low, sell high — profit = 6")

    # Test 2: Decreasing prices — no profitable trade
    result = max_profit([10, 8, 7, 5, 2])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 2 passed: Decreasing prices — no profit")

    # Test 3: Single element — no trade possible
    result = max_profit([5])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 3 passed: Single price — no profit")

    # Test 4: Two elements — profitable
    result = max_profit([1, 5])
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 4 passed: Two prices — profit = 4")

    # Test 5: Two elements — not profitable
    result = max_profit([5, 1])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 5 passed: Two prices descending — no profit")

    # Test 6: All same prices
    result = max_profit([3, 3, 3, 3])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 6 passed: All same prices — no profit")

    # Test 7: Best buy is not the first element
    result = max_profit([7, 2, 5, 1, 3])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 7 passed: Best buy in the middle — profit = 3")

    # Test 8: Increasing prices — buy first, sell last
    result = max_profit([1, 2, 3, 4, 5])
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 8 passed: Increasing prices — profit = 4")

    # Test 9: Profit at the end
    result = max_profit([9, 1, 3, 2, 8])
    assert result == 7, f"Expected 7, got {result}"
    print("✓ Test 9 passed: Late sell — profit = 7")

    # Test 10: Multiple dips with best profit in between
    result = max_profit([3, 1, 4, 8, 2, 7])
    assert result == 7, f"Expected 7, got {result}"
    print("✓ Test 10 passed: Multiple dips — profit = 7")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_max_profit()


print(max_profit([10, 1, 5, 6, 7, 1]))
# Output: 6

print(max_profit([10, 8, 7, 5, 2]))
# Output: 0
