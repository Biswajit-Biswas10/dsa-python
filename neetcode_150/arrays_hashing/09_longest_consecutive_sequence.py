"""
Problem Name: Longest Consecutive Sequence

Problem Description:
Given an array of integers nums, return the length of the longest consecutive sequence of elements that 
can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the 
previous element. The elements do not have to be consecutive in the original array.

Example 1:
Input: [2, 20, 4, 10, 3, 4, 5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

Example 3:
Input: [0, 0]
Output: 1
Explanation: After handling duplicates, only one 0 remains.

Approach:

Algorithm (Sort + Linear Scan):
1. Edge case: if array is empty, return 0.
2. Sort the input array.
3. Initialise two variables:
   - count = 1   (current streak length, a single number is already length 1)
   - longest = 1 (best streak found so far)
4. Iterate from the 2nd element, comparing each number with the previous:
   - DUPLICATE:    current == previous     → skip it (continue)
   - CONSECUTIVE:  current == previous + 1 → grow streak (count += 1),
                                              update longest if count is bigger
   - GAP:          current > previous + 1  → reset streak (count = 1)
5. Return longest.

Why handle duplicates?
- After sorting [2, 20, 4, 10, 3, 4, 5] becomes [2, 3, 4, 4, 5, 10, 20]
- The two 4s are neither consecutive nor a gap.
- Without skipping duplicates, we'd wrongly reset the streak at the second 4.

Solution: Sort + Linear Scan
- Time Complexity:  O(n log n) - dominated by the sorting step
- Space Complexity: O(1) - only two extra variables (excluding sort space)
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Return the length of the longest consecutive elements sequence
    in an unsorted array.

    Uses sorting followed by a single linear scan, handling three
    cases at each step: duplicate (skip), consecutive (grow), gap (reset).
    e.g. [2, 20, 4, 10, 3, 4, 5] → sorted [2, 3, 4, 4, 5, 10, 20] → 4

    Args:
        nums: List of integers (may contain duplicates)

    Returns:
        int: Length of the longest consecutive sequence
    """
    # Edge case: empty array has no consecutive sequence
    if len(nums) < 1:
        return 0

    sorted_nums = sorted(nums)

    # A single number is already a sequence of length 1
    count = 1
    longest = 1

    # Scan sorted array starting from the 2nd element
    for i in range(1, len(sorted_nums)):
        curr_num = sorted_nums[i]
        prev_num = sorted_nums[i - 1]

        # Case 1: DUPLICATE → skip, don't affect the streak
        # e.g. [... 4, 4 ...] → same number, just move on
        if curr_num == prev_num:
            continue

        # Case 2: CONSECUTIVE → grow the current streak
        # e.g. [... 3, 4 ...] → extends the sequence
        elif curr_num == prev_num + 1:
            count += 1
            longest = max(longest, count)

        # Case 3: GAP → streak is broken, start fresh
        # e.g. [... 5, 10 ...] → gap of 5, reset to 1
        else:
            count = 1

    return longest


## Test Cases
def test_longest_consecutive():
    """Test cases for longest_consecutive function."""

    # Test 1: Main example with duplicates
    result = longest_consecutive([2, 20, 4, 10, 3, 4, 5])
    assert result == 4, "Should return 4 for sequence [2, 3, 4, 5]"
    print("✓ Test 1 passed: Array with duplicates")

    # Test 2: Classic example
    result = longest_consecutive([100, 4, 200, 1, 3, 2])
    assert result == 4, "Should return 4 for sequence [1, 2, 3, 4]"
    print("✓ Test 2 passed: Classic example")

    # Test 3: Empty array
    result = longest_consecutive([])
    assert result == 0, "Should return 0 for empty array"
    print("✓ Test 3 passed: Empty array")

    # Test 4: Single element
    result = longest_consecutive([7])
    assert result == 1, "Should return 1 for single element"
    print("✓ Test 4 passed: Single element")

    # Test 5: All duplicates
    result = longest_consecutive([0, 0])
    assert result == 1, "Should return 1 for all duplicates"
    print("✓ Test 5 passed: All duplicates")

    # Test 6: All consecutive
    result = longest_consecutive([5, 4, 3, 2, 1])
    assert result == 5, "Should return 5 for fully consecutive array"
    print("✓ Test 6 passed: All consecutive")

    # Test 7: No consecutive pairs
    result = longest_consecutive([10, 30, 50])
    assert result == 1, "Should return 1 when no consecutive pairs exist"
    print("✓ Test 7 passed: No consecutive pairs")

    # Test 8: Negative numbers
    result = longest_consecutive([-3, -2, -1, 0, 1])
    assert result == 5, "Should return 5 for negative to positive sequence"
    print("✓ Test 8 passed: Negative numbers")

    # Test 9: Multiple streaks, longest at the end
    result = longest_consecutive([1, 2, 10, 11, 12, 13])
    assert result == 4, "Should return 4 for sequence [10, 11, 12, 13]"
    print("✓ Test 9 passed: Multiple streaks")

    # Test 10: Duplicates within a streak
    result = longest_consecutive([1, 2, 2, 3, 3, 3, 4])
    assert result == 4, "Should return 4 despite heavy duplicates"
    print("✓ Test 10 passed: Duplicates within a streak")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_longest_consecutive()


print(longest_consecutive([2, 20, 4, 10, 3, 4, 5]))
# Output: 4

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# Output: 4

print(longest_consecutive([0, 0]))
# Output: 1
