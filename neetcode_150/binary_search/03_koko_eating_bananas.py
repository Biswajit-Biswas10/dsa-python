"""
Problem Name: Koko Eating Bananas

Problem Description:
Koko loves to eat bananas. There are n piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed k. Each hour, she chooses a pile and eats
k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during that hour.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: At speed 4, hours needed = ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4)
                                       = 1 + 2 + 2 + 3 = 8 hours ✓

Example 2:
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
Explanation: At speed 30, each pile takes exactly 1 hour = 5 hours total ✓

Example 3:
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

Approach:

Algorithm (Binary Search on Answer):
1. If piles is empty, return 0 (nothing to eat).
2. Set low = 1 (minimum valid speed) and high = max(piles) (no need to go faster
   than the largest pile — it would always finish in 1 hour).
3. Binary search while low < high:
   - Calculate mid = low + (high - low) // 2 as the candidate speed.
   - Compute total hours needed at speed mid:
       hours = sum(ceil(p / mid) for p in piles)
   - If hours <= h: speed is fast enough → try slower → high = mid
   - If hours >  h: speed is too slow  → go faster  → low = mid + 1
4. When low == high, we have converged on the minimum valid speed.
   Return low.

Why Binary Search works here:
- The search space for speed k is [1, max(piles)] — a sorted, bounded range.
- The feasibility function is monotonic: if speed k works, any speed > k also works.
  This means we can binary search on the speed itself, not the array.
- Each iteration halves the search space → O(log(max(piles))) iterations.
- Each iteration costs O(n) to compute total hours → overall O(n log m).

Key difference vs standard Binary Search:
- Standard binary search: searching for a value IN an array.
- This pattern:         searching for the MINIMUM valid value in a range.
  → Use while low < high with high = mid (not mid - 1) to avoid overshooting.

Visualisation:
    piles = [3, 6, 7, 11],  h = 8

    low=1  high=11
    Step 1:  mid=6  → hours = ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6 ≤ 8 → high=6
    Step 2:  mid=3  → hours = ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) = 1+2+3+4 = 10 > 8 → low=4
    Step 3:  mid=5  → hours = ceil(3/5)+ceil(6/5)+ceil(7/5)+ceil(11/5) = 1+2+2+3 = 8 ≤ 8 → high=5
    Step 4:  mid=4  → hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 ≤ 8 → high=4

    low=4 == high=4 → Return 4

Solution: Binary Search on Answer
- Time Complexity:  O(n log m) — log m iterations (m = max pile), O(n) per iteration
- Space Complexity: O(1)       — only low, high, mid, hours variables used
"""

from math import ceil
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    # edge case: empty piles list, no eating needed
    if not piles:
        return 0

    low = 1              # minimum possible speed (at least 1 banana/hour)
    high = max(piles)    # maximum useful speed (finish largest pile in 1 hour)

    # binary search: narrow down the minimum valid speed
    while low < high:
        # candidate speed; integer division avoids float precision issues
        mid = low + (high - low) // 2

        # total hours needed at speed mid across all piles
        # ceil ensures a partial pile still costs a full hour (e.g. 7 bananas at speed 3 = 3 hrs)
        # hours = sum(ceil(p / mid) for p in piles)
        hours = sum((p + mid - 1) // mid for p in piles)

        if hours <= h:
            # speed mid is fast enough — try slower (search left for minimum)
            high = mid
        else:
            # speed mid is too slow — must go faster (search right)
            low = mid + 1

    # low == high: converged on the minimum speed that finishes within h hours
    return low


## Test Cases
def test_min_eating_speed():
    """Test cases for min_eating_speed function."""

    # Test 1: Standard case — answer requires ceiling math
    result = min_eating_speed([3, 6, 7, 11], 8)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 1 passed: Standard case — piles=[3,6,7,11], h=8 → speed 4")

    # Test 2: h equals number of piles — must finish each pile in 1 hour
    result = min_eating_speed([30, 11, 23, 4, 20], 5)
    assert result == 30, f"Expected 30, got {result}"
    print("✓ Test 2 passed: h == len(piles) — must eat at max pile speed → 30")

    # Test 3: Extra hours available — slower speed is sufficient
    result = min_eating_speed([30, 11, 23, 4, 20], 6)
    assert result == 23, f"Expected 23, got {result}"
    print("✓ Test 3 passed: Extra hour available — slower speed sufficient → 23")

    # Test 4: Single pile — only one pile to eat
    result = min_eating_speed([10], 3)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 4 passed: Single pile — piles=[10], h=3 → speed 4")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_min_eating_speed()


print(min_eating_speed([3, 6, 7, 11], 8))
# Output: 4

print(min_eating_speed([30, 11, 23, 4, 20], 5))
# Output: 30
