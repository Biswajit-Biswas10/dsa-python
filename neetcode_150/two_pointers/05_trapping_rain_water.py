"""
Problem Name: Trapping Rain Water

Problem Description:
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation:
    Bar chart with trapped water (~ = water):

            3
            |
    2~~~~ ~~|
    | ~|~~| ||~|
    _|_|__|_||||_|_
    0 1 0 2 1 0 1 3 2 1 2 1

    Water trapped between bars sums to 6 units.

Example 2:
Input: height = [3, 0, 3]
Output: 3
Explanation: The gap between two bars of height 3 holds 3 units of water.

Example 3:
Input: height = [1, 2, 3, 4, 5]
Output: 0
Explanation: Strictly ascending — water flows off to the left, nothing trapped.

Approach:
1. If height is empty or length < 3, return 0

2. Build Prefix Max array (left → right):
   - Set prefix_max[0] = height[0]
   - For i from 1 to n-1:
     - prefix_max[i] = max(prefix_max[i-1], height[i])

3. Build Suffix Max array (right → left):
   - Set suffix_max[n-1] = height[n-1]
   - For i from n-2 down to 0:
     - suffix_max[i] = max(suffix_max[i+1], height[i])

4. Calculate trapped water:
   - Initialize total_water = 0
   - For each index i from 0 to n-1:
     - water_at_i = min(prefix_max[i], suffix_max[i]) - height[i]
     - Add water_at_i to total_water

5. Return total_water

Why prefix + suffix arrays?
- At each position, we need to know the tallest bar on both sides.
- Precomputing these avoids a nested loop (O(n²)) and gives us O(n) lookups.
- Each position's trapped water depends only on its left max, right max,
  and its own height — all available in O(1) after precomputation.

Solution: Prefix Max + Suffix Max
- Time Complexity:  O(n) — three separate passes through the array
- Space Complexity: O(n) — two extra arrays of size n
"""

from typing import List

def trapping_rain_water(height: List[int]) -> int:
    """
    Compute the total units of water trapped between bars after raining.

    Builds prefix_max (tallest bar to the left) and suffix_max (tallest bar
    to the right) arrays, then calculates water at each position as the
    difference between the water level and the ground height, clamped to zero.

    Args:
        height: List of non-negative integers representing bar heights.

    Returns:
        int: Total units of trapped rainwater.
    """
    n = len(height)

    # Step-1: Edge Case — need at least 3 bars to form a container
    # e.g. [3, 1] → water flows off both sides, nothing trapped
    if n < 3:
        return 0

    # Step-2: Build Prefix Max Array (left → right)
    # prefix_max[i] = tallest bar from index 0 to i
    # e.g. height = [1, 0, 3, 2] → prefix_max = [1, 1, 3, 3]
    prefix_max = [0] * n
    prefix_max[0] = height[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], height[i])

    # Step-3: Build Suffix Max Array (right → left)
    # suffix_max[i] = tallest bar from index i to n-1
    # e.g. height = [1, 0, 3, 2] → suffix_max = [3, 3, 3, 2]
    suffix_max = [0] * n
    suffix_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], height[i])

    # Step-4: Calculate Trapped Water
    # Water level at i = min(left wall, right wall)
    # Water at i       = max(water_level - ground_height, 0)
    # Clamp to 0 because water cannot be negative (bar taller than water level)
    total_water = 0
    for i in range(n):
        water_at_i = max(min(prefix_max[i], suffix_max[i]) - height[i], 0)
        total_water += water_at_i

    return total_water


## Test Cases
def test_trapping_rain_water():
    """Test cases for trapping_rain_water function."""

    # Test 1: Classic example — water trapped in multiple valleys
    result = trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert result == 6, "Should trap 6 units in the classic elevation map"
    print("✓ Test 1 passed: Classic elevation map (6 units)")

    # Test 2: V-shaped container — simple valley between two walls
    result = trapping_rain_water([3, 0, 3])
    assert result == 3, "Should trap 3 units in a V-shaped container"
    print("✓ Test 2 passed: V-shaped container (3 units)")

    # Test 3: Strictly ascending — water flows off to the left
    result = trapping_rain_water([1, 2, 3, 4, 5])
    assert result == 0, "Should trap nothing in ascending bars"
    print("✓ Test 3 passed: Ascending bars (0 units)")

    # Test 4: Strictly descending — water flows off to the right
    result = trapping_rain_water([5, 4, 3, 2, 1])
    assert result == 0, "Should trap nothing in descending bars"
    print("✓ Test 4 passed: Descending bars (0 units)")

    # Test 5: Edge case — fewer than 3 bars, impossible to trap
    result = trapping_rain_water([1, 2])
    assert result == 0, "Should return 0 for fewer than 3 bars"
    print("✓ Test 5 passed: Edge case with 2 bars (0 units)")

    # Test 6: Flat surface — no valleys to hold water
    result = trapping_rain_water([3, 3, 3, 3])
    assert result == 0, "Should trap nothing on a flat surface"
    print("✓ Test 6 passed: Flat surface (0 units)")

    # Test 7: Single deep valley
    result = trapping_rain_water([5, 0, 0, 0, 5])
    assert result == 15, "Should trap 15 units in a deep valley"
    print("✓ Test 7 passed: Single deep valley (15 units)")

    # Test 8: Uneven walls — water limited by shorter wall
    result = trapping_rain_water([4, 0, 0, 0, 2])
    assert result == 6, "Should trap based on shorter wall height"
    print("✓ Test 8 passed: Uneven walls (6 units)")

    # Test 9: Empty input
    result = trapping_rain_water([])
    assert result == 0, "Should return 0 for empty input"
    print("✓ Test 9 passed: Empty input (0 units)")

    # Test 10: Multiple valleys
    result = trapping_rain_water([3, 0, 3, 0, 3])
    assert result == 6, "Should trap water in multiple valleys"
    print("✓ Test 10 passed: Multiple valleys (6 units)")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_trapping_rain_water()


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# Output: 6

print(trapping_rain_water([3, 0, 3]))
# Output: 3

print(trapping_rain_water([0, 0, 0]))
# Output: 0
