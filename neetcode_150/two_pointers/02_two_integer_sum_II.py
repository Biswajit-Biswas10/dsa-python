"""
Problem Name: Two Integer Sum II

Problem Description:
Given an array of integers numbers that is sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array [index1, index2]
of length 2, where 1 <= index1 < index2 <= numbers.length.

There is guaranteed to be exactly one solution. You may not use the same element twice.

Example 1:
Input: numbers = [1, 2, 3, 4], target = 3
Output: [1, 2]
Explanation: The sum of 1 and 2 is 3. Since we are using 1-indexed,
index1 = 1 and index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Example 3:
Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.

Example 4:
Input: numbers = [-1, 0], target = -1
Output: [1, 2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2.

Approach:

Algorithm (Two Pointers — Inward Scan on Sorted Array):
1. Initialise two pointers:
   - left  = 0                  (start of the array)
   - right = len(numbers) - 1   (end of the array)
2. Loop while left < right, handling three cases:
   - TOO SMALL: current_sum < target → move left forward  (left += 1)
   - TOO LARGE: current_sum > target → move right backward (right -= 1)
   - EXACT MATCH: current_sum == target → return [left + 1, right + 1]
3. The problem guarantees exactly one solution, so the loop always finds it.


Solution: Two Pointers (Inward Scan)
- Time Complexity:  O(n) - each pointer moves at most n times total
- Space Complexity: O(1) - only two pointer variables, no extra data structures
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Return 1-indexed positions of two numbers that add up to target
    in a sorted array.

    Uses two pointers moving inward from both ends, leveraging the
    sorted order to decide which pointer to move.

    Args:
        numbers: Sorted (non-decreasing) list of integers
        target:  The target sum to find

    Returns:
        List[int]: 1-indexed [index1, index2] where
                   numbers[index1-1] + numbers[index2-1] == target
    """
    left = 0
    right = len(numbers) - 1

    while left < right:

        # Calculate the sum of elements at both pointers
        # e.g. numbers = [1, 2, 3, 4], left=0, right=3 → sum = 1 + 4 = 5
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Found the pair — return 1-indexed positions
            # e.g. left=0, right=1 → return [1, 2]
            return [left + 1, right + 1]

        elif current_sum < target:
            # Sum is too small — move left pointer forward to increase sum
            # e.g. numbers[0]=1 is too small, try numbers[1]=2 next
            left += 1

        else:
            # Sum is too large — move right pointer backward to decrease sum
            # e.g. numbers[3]=4 is too large, try numbers[2]=3 next
            right -= 1


## Test Cases
def test_two_sum():
    """Test cases for two_sum function."""

    # Test 1: Basic example
    result = two_sum([1, 2, 3, 4], 3)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Test 1 passed: Basic pair [1, 2] summing to 3")

    # Test 2: Classic two-sum example
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Test 2 passed: First two elements sum to target")

    # Test 3: Non-adjacent elements
    result = two_sum([2, 3, 4], 6)
    assert result == [1, 3], f"Expected [1, 3], got {result}"
    print("✓ Test 3 passed: Non-adjacent pair [1, 3] summing to 6")

    # Test 4: Negative numbers
    result = two_sum([-1, 0], -1)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Test 4 passed: Negative number pair")

    # Test 5: Larger array — pair in the middle
    result = two_sum([1, 3, 4, 5, 7, 10, 11], 9)
    assert result == [3, 4], f"Expected [3, 4], got {result}"
    print("✓ Test 5 passed: Pair in the middle of a larger array")

    # Test 6: Duplicate values
    result = two_sum([1, 2, 2, 3], 4)
    assert result == [1, 4], f"Expected [1, 4], got {result}"
    print("✓ Test 6 passed: Duplicate values in array")

    # Test 7: Two elements only
    result = two_sum([5, 10], 15)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Test 7 passed: Minimum length array (two elements)")

    # Test 8: Large target with negative numbers
    result = two_sum([-10, -3, 0, 5, 9], -13)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Test 8 passed: Negative numbers summing to negative target")

    # Test 9: Target zero with positive and negative
    result = two_sum([-5, -3, 0, 3, 7], 0)
    assert result == [2, 4], f"Expected [2, 4], got {result}"
    print("✓ Test 9 passed: Positive and negative summing to zero")

    # Test 10: Last two elements
    result = two_sum([1, 2, 3, 4, 5], 9)
    assert result == [4, 5], f"Expected [4, 5], got {result}"
    print("✓ Test 10 passed: Last two elements form the pair")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_two_sum()


print(two_sum([1, 2, 3, 4], 3))
# Output: [1, 2]

print(two_sum([2, 7, 11, 15], 9))
# Output: [1, 2]

print(two_sum([2, 3, 4], 6))
# Output: [1, 3]
