"""
Problem Name: Container With Most Water

Problem Description:
You are given an integer array heights where heights[i] represents the height
of the ith bar. You may choose any two bars to form a container. Return the
maximum amount of water a container can store.

Note: The water area is calculated as min(height[left], height[right]) × (right - left).
The shorter bar limits the water level (water spills over it), and the distance
between the bars determines the width.

Example 1:
Input: heights = [1, 7, 2, 5, 4, 7, 3, 6]
Output: 36
Explanation: Choosing bars at index 1 (height 7) and index 7 (height 6)
gives water = min(7, 6) × (7 - 1) = 6 × 6 = 36.

Example 2:
Input: heights = [2, 2, 2]
Output: 4
Explanation: Choosing bars at index 0 (height 2) and index 2 (height 2)
gives water = min(2, 2) × (2 - 0) = 2 × 2 = 4.

Approach:

Algorithm (Two Pointers):
1. Initialise two pointers:
   - left  = 0                    (start of the array)
   - right = len(heights) - 1     (end of the array)
   - max_water = 0                (tracks the best result)
2. Loop while left < right:
   - CALCULATE: width = right - left, height = min(heights[left], heights[right])
   - UPDATE:    max_water = max(max_water, width × height)
   - MOVE:      move the pointer pointing to the shorter bar inward
       - heights[left] < heights[right]  → left += 1
       - otherwise                       → right -= 1
3. Return max_water.

Why move the shorter bar?
- Water level is capped by the shorter bar.
- Moving the taller bar: width shrinks, height stays capped → area can only decrease.
- Moving the shorter bar: width shrinks, but height might increase → area could increase.
- Without this greedy choice, we'd need O(n²) brute force checking every pair.

Solution: Two Pointers (Inward Scan)
- Time Complexity:  O(n) - each pointer moves at most n times
- Space Complexity: O(1) - only a few variables, no extra data structures
"""

from typing import List


def container_with_most_water(heights: List[int]) -> int:
    """
    Return the maximum water area formed by choosing any two bars.

    Uses two pointers starting from both ends, greedily moving the
    shorter bar inward to find the optimal pair.

    Args:
        heights: List of integers representing bar heights

    Returns:
        int: Maximum water a container can store
    """
    # ========== INITIALIZATION ==========
    left = 0
    right = len(heights) - 1
    max_water = 0

    # ========== MAIN ALGORITHM ==========
    # Move pointers inward until they meet
    while left < right:

        # Calculate width (distance between bars)
        # e.g. right=7, left=1 → width = 6
        width = right - left

        # Calculate height (limited by the shorter bar)
        # e.g. heights[1]=7, heights[7]=6 → height = min(7, 6) = 6
        height = min(heights[left], heights[right])

        # Update max_water if current area is larger
        # e.g. max(0, 6 × 6) = 36
        max_water = max(max_water, width * height)

        # Move the shorter bar inward (greedy choice)
        # e.g. heights[1]=7 > heights[7]=6 → move right inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    # ========== RETURN RESULT ==========
    # All pairs considered — return the best
    return max_water


## Test Cases
def test_container_with_most_water():
    """Test cases for container_with_most_water function."""

    # Test 1: General case with varying heights
    result = container_with_most_water([1, 7, 2, 5, 4, 7, 3, 6])
    assert result == 36, "Should return 36 for bars at index 1 and 7"
    print("✓ Test 1 passed: General case with varying heights")

    # Test 2: All bars have equal height
    result = container_with_most_water([2, 2, 2])
    assert result == 4, "Should return 4 for equal height bars"
    print("✓ Test 2 passed: All bars have equal height")

    # Test 3: Minimum valid input — two bars
    result = container_with_most_water([1, 1])
    assert result == 1, "Should return 1 for two bars of height 1"
    print("✓ Test 3 passed: Minimum valid input")

    # Test 4: Classic LeetCode example
    result = container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert result == 49, "Should return 49 for classic example"
    print("✓ Test 4 passed: Classic LeetCode example")

    # Test 5: Strictly increasing heights
    result = container_with_most_water([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result == 25, "Should return 25 for increasing heights"
    print("✓ Test 5 passed: Strictly increasing heights")

    # Test 6: Strictly decreasing heights
    result = container_with_most_water([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert result == 25, "Should return 25 for decreasing heights"
    print("✓ Test 6 passed: Strictly decreasing heights")

    # Test 7: One very tall bar in the middle
    result = container_with_most_water([1, 1, 1, 100, 1, 1, 1])
    assert result == 6, "Should return 6 — tall bar doesn't help when others are short"
    print("✓ Test 7 passed: One very tall bar in the middle")

    # Test 8: Two tall bars at the ends
    result = container_with_most_water([100, 1, 1, 1, 1, 1, 100])
    assert result == 600, "Should return 600 for tall bars at both ends"
    print("✓ Test 8 passed: Two tall bars at the ends")

    # Test 9: Large and small alternating
    result = container_with_most_water([1, 100, 1, 100])
    assert result == 200, "Should return 200 for alternating heights"
    print("✓ Test 9 passed: Large and small alternating")

    # Test 10: Two bars with different heights
    result = container_with_most_water([5, 10])
    assert result == 5, "Should return 5 — limited by shorter bar"
    print("✓ Test 10 passed: Two bars with different heights")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_container_with_most_water()


print(container_with_most_water([1, 7, 2, 5, 4, 7, 3, 6]))
# Output: 36

print(container_with_most_water([2, 2, 2]))
# Output: 4

print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Output: 49
