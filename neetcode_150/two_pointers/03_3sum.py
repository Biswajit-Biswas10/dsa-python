"""
Problem Name: Three Sum

Problem Description:
Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: Two unique triplets sum to zero.

Example 2:
Input: nums = [0, 1, 1]
Output: []
Explanation: No triplet sums to zero.

Example 3:
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
Explanation: The only triplet is [0, 0, 0].

Approach:

Algorithm (Sort + Two Pointers):
1. Sort the array so that duplicates are adjacent and two-pointer logic works.
2. Iterate i from 0 to n-2 (the fixed/anchor element):
   - EARLY EXIT:       nums[i] > 0 → all remaining elements are positive,
                       no triplet can sum to zero → break.
   - SKIP DUPLICATE:   i > 0 and nums[i] == nums[i-1] → same anchor as last
                       iteration, skip to avoid duplicate triplets → continue.
3. Set left = i + 1, right = n - 1 and run two-pointer scan:
   - SUM TOO SMALL:   current_sum < 0 → move left pointer right (left += 1)
   - SUM TOO LARGE:   current_sum > 0 → move right pointer left (right -= 1)
   - TRIPLET FOUND:   current_sum == 0 → record triplet, then skip duplicate
                      values on both sides before moving pointers inward.

Why sort first?
- Sorting lets us use two pointers (O(n) per anchor) instead of a nested loop
  (O(n²) per anchor).
- It also groups duplicate values together so we can skip them with a simple
  equality check.

Solution: Sort + Two Pointers
- Time Complexity:  O(n²) — O(n log n) sort + O(n²) two-pointer scan
- Space Complexity: O(1) — only pointer variables (excluding output list)
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Return all unique triplets in nums that sum to zero.

    Sorts the array then uses a fixed anchor pointer (i) with an inward
    two-pointer scan (left, right) to find pairs that complete each triplet.
    Duplicate anchors and duplicate pairs are skipped to ensure uniqueness.

    Args:
        nums: List of integers (may contain duplicates, negatives, zeros)

    Returns:
        List[List[int]]: All unique [a, b, c] triplets where a + b + c == 0
    """
    result = []
    n = len(nums)
    nums.sort()

    for i in range(n - 2):

        # Early exit: smallest remaining value is positive → no zero-sum possible
        # e.g. [1, 2, 3] → 1+2+3 > 0, no point continuing
        if nums[i] > 0:
            break

        # Skip duplicate anchor values to avoid duplicate triplets in result
        # e.g. [-1, -1, 0, 1] → second -1 as anchor gives same triplets as first
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        # Two-pointer inward scan to find pairs that complete the triplet
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Sum too small → need a larger left value
            if current_sum < 0:
                left += 1

            # Sum too large → need a smaller right value
            elif current_sum > 0:
                right -= 1

            # Triplet found → record it, then skip duplicates on both sides
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate left values
                # e.g. [-2, 0, 0, 2, 2] → skip second 0 after recording [-2,0,2]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicate right values
                # e.g. [-2, 0, 0, 2, 2] → skip second 2 after recording [-2,0,2]
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward for next pair
                left += 1
                right -= 1

    return result


## Test Cases
def test_three_sum():
    """Test cases for three_sum function."""

    # Test 1: Main example — two valid triplets
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]]), \
        "Should return two unique triplets"
    print("✓ Test 1 passed: Standard case with two triplets")

    # Test 2: No valid triplet exists
    result = three_sum([0, 1, 1])
    assert result == [], "Should return empty list when no triplet sums to zero"
    print("✓ Test 2 passed: No valid triplet")

    # Test 3: All zeros
    result = three_sum([0, 0, 0])
    assert result == [[0, 0, 0]], "Should return [[0,0,0]] for all-zero input"
    print("✓ Test 3 passed: All zeros")

    # Test 4: All positive — no triplet possible
    result = three_sum([1, 2, 3])
    assert result == [], "Should return empty for all-positive input"
    print("✓ Test 4 passed: All positive numbers")

    # Test 5: All negative — no triplet possible
    result = three_sum([-3, -2, -1])
    assert result == [], "Should return empty for all-negative input"
    print("✓ Test 5 passed: All negative numbers")

    # Test 6: Duplicates in input — no duplicate triplets in output
    result = three_sum([-2, 0, 0, 2, 2])
    assert result == [[-2, 0, 2]], "Should deduplicate triplets"
    print("✓ Test 6 passed: Duplicates handled correctly")

    # Test 7: Multiple triplets
    result = three_sum([-4, -1, -1, 0, 1, 2])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]]), \
        "Should return all unique triplets"
    print("✓ Test 7 passed: Multiple triplets with duplicates")

    # Test 8: Minimum valid input (exactly 3 elements)
    result = three_sum([-1, 0, 1])
    assert result == [[-1, 0, 1]], "Should find the only triplet"
    print("✓ Test 8 passed: Minimum length input")

    # Test 9: Large mix of values
    result = three_sum([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    assert [-5, 1, 4] in result and [-1, 0, 1] in result, \
        "Should find triplets across a large range"
    print("✓ Test 9 passed: Large mixed input")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_three_sum()


print(three_sum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]

print(three_sum([0, 1, 1]))
# Output: []

print(three_sum([0, 0, 0]))
# Output: [[0, 0, 0]]
