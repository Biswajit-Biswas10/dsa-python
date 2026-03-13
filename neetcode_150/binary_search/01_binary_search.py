"""
Problem Name: Binary Search

Problem Description:

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, 
otherwise, return -1.

Your solution must run in O(log n) time.

Example 1:
Input: nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3
Explanation: 4 is found at index 3.

Example 2:
Input: nums = [-1, 0, 2, 4, 6, 8], target = 5
Output: -1
Explanation: 5 does not exist in the array.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are distinct
- nums is sorted in ascending order

Approach:

Algorithm (Two Pointer — Iterative Binary Search):
1. If the array is empty, return -1 (nothing to search).
2. Initialise two pointers: low = 0, high = len(nums) - 1.
3. Loop while low <= high, handling three cases:
   - Calculate mid = low + (high - low) // 2 to avoid overflow.
   - MATCH    (nums[mid] == target): Return mid — target found.
   - TOO HIGH (nums[mid] > target):  Set high = mid - 1
       → discard right half, target must be in left half.
   - TOO LOW  (nums[mid] < target):  Set low = mid + 1
       → discard left half, target must be in right half.
4. If the loop ends without returning, the target does not exist.
   Return -1.

Why Binary Search works here:
- The array is sorted, so comparing the middle element with the
  target tells us which half to discard.
- Each iteration eliminates half the search space — this gives
  O(log n) time instead of O(n) with linear search.
- Three termination cases are exhaustive: found at mid, target
  is smaller (go left), target is larger (go right).

Visualisation:
    nums = [-1, 0, 2, 4, 6, 8],  target = 4

    Step 1:  low=0  high=5 → mid=2 → nums[2]=2  < 4 → low=3
    Step 2:  low=3  high=5 → mid=4 → nums[4]=6  > 4 → high=3
    Step 3:  low=3  high=3 → mid=3 → nums[3]=4 == 4 → Return 3 ✓

Solution: Two Pointer (Iterative Binary Search)
- Time Complexity:  O(log n) - search space halves each iteration
- Space Complexity: O(1)     - only three extra variables (low, mid, high)
"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    # base case: empty array has nothing to search
    if not nums:
        return -1

    # define the search space with two pointers
    low = 0
    high = len(nums) - 1

    # keep searching while the window is valid
    while low <= high:
        # calculate mid safely to avoid integer overflow
        mid = low + (high - low) // 2

        if nums[mid] == target:
            # target found → return its index
            return mid
        elif nums[mid] > target:
            # mid value too high → discard right half
            high = mid - 1
        else:
            # mid value too low → discard left half
            low = mid + 1

    # search space exhausted → target does not exist
    return -1


## Test Cases
def test_binary_search():
    """Test cases for binary_search function."""

    # Test 1: Target exists in the middle
    result = binary_search([-1, 0, 2, 4, 6, 8], 4)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 1 passed: Target in middle — found 4 at index 3")

    # Test 2: Target is the first element
    result = binary_search([-1, 0, 2, 4, 6, 8], -1)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 2 passed: Target at start — found -1 at index 0")

    # Test 3: Target is the last element
    result = binary_search([-1, 0, 2, 4, 6, 8], 8)
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 3 passed: Target at end — found 8 at index 5")

    # Test 4: Target does not exist (falls between elements)
    result = binary_search([-1, 0, 2, 4, 6, 8], 5)
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 4 passed: Target missing — 5 not in array")

    # Test 5: Target smaller than all elements
    result = binary_search([-1, 0, 2, 4, 6, 8], -5)
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 5 passed: Target below range — -5 not in array")

    # Test 6: Target larger than all elements
    result = binary_search([-1, 0, 2, 4, 6, 8], 10)
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 6 passed: Target above range — 10 not in array")

    # Test 7: Empty array
    result = binary_search([], 4)
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 7 passed: Empty array — returns -1")

    # Test 8: Single element — found
    result = binary_search([4], 4)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 8 passed: Single element found — [4], target 4")

    # Test 9: Single element — not found
    result = binary_search([4], 2)
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 9 passed: Single element missing — [4], target 2")

    # Test 10: Two elements — target is first
    result = binary_search([1, 3], 1)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 10 passed: Two elements, target first — [1, 3], target 1")

    # Test 11: Two elements — target is second
    result = binary_search([1, 3], 3)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 11 passed: Two elements, target second — [1, 3], target 3")

    # Test 12: Large sorted array — target near the end
    result = binary_search(list(range(0, 1000)), 997)
    assert result == 997, f"Expected 997, got {result}"
    print("✓ Test 12 passed: Large array — found 997 at index 997")

    # Test 13: Negative numbers only
    result = binary_search([-10, -7, -3, -1], -3)
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Test 13 passed: Negative array — found -3 at index 2")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_binary_search()


print(binary_search([-1, 0, 2, 4, 6, 8], 4))
# Output: 3

print(binary_search([-1, 0, 2, 4, 6, 8], 5))
# Output: -1
