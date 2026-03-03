"""
Problem Name: Sliding Window Maximum

Problem Description:
You are given an array of integers "nums" and an integer "k". There is a
sliding window of size k that starts at the left edge of the array. The
window slides one position to the right until it reaches the right edge.

Return a list that contains the maximum element in the window at each step.
The output always contains exactly (n - k + 1) elements.

Example 1:
Input: nums = [1, 2, 1, 0, 4, 2, 6], k = 3
Output: [2, 2, 4, 4, 6]
Explanation:
  Window [1,2,1] → max = 2
  Window [2,1,0] → max = 2
  Window [1,0,4] → max = 4
  Window [0,4,2] → max = 4
  Window [4,2,6] → max = 6

Example 2:
Input: nums = [2, 6, 8, 3, 5, 4], k = 3
Output: [8, 8, 8, 5]
Explanation:
  Window [2,6,8] → max = 8
  Window [6,8,3] → max = 8
  Window [8,3,5] → max = 8
  Window [3,5,4] → max = 5

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

Approach:

Algorithm (Monotonic Deque — Decreasing Order):
1. Use a deque that stores INDICES (not values) in decreasing order
   of their corresponding values.
2. The front of the deque always holds the index of the maximum
   element in the current window.
3. For each new element, apply three rules:
   - EXPIRE:  Remove front index if it's outside the window boundary.
   - CLEAN:   Remove all back indices whose values are smaller than
              the new element (they can NEVER be the max while this
              bigger element exists in the window).
   - ADD:     Append the current index to the back.
4. Once the window is full (i >= k - 1), the front of the deque
   gives the index of the current window's maximum.

Why Monotonic Deque works here:
- A smaller element is USELESS if a larger element exists after it
  within the same window — the smaller one can never be the max.
- By greedily removing useless elements from the back, I maintain
  a decreasing sequence where the front is always the window max.
- Each element is pushed and popped AT MOST once, giving O(n) time.

Solution: Monotonic Deque (Decreasing)
- Time Complexity:  O(n) - each element enters and leaves the deque at most once
- Space Complexity: O(k) - deque never holds more than k elements
"""

from collections import deque
from typing import List, Optional


def max_sliding_window(nums: List[int], k: int) -> Optional[List[int]]:
    """
    Return the maximum element in each sliding window of size k.

    Uses a monotonic decreasing deque: the front always holds the
    index of the largest element in the current window.

    Args:
        nums: List of integers representing the input array.
        k:    Size of the sliding window.

    Returns:
        List[int]: Maximum of each window. Returns None if input
                   is empty or window size exceeds array length.
    """
    # Edge case: invalid input — not enough elements for even one window
    if not nums or k <= 0 or k > len(nums):
        return None

    # Monotonic deque storing INDICES (not values) in decreasing order
    dq = deque()

    # Stores the maximum of each window position
    result = []

    # Total number of elements
    n = len(nums)

    # Slide through every element in the array
    for i in range(n):

        # STEP 1 — EXPIRE: Remove front index if it's outside the window
        # Window boundary: valid indices are [i - k + 1, i]
        # e.g. at i=5, k=3 → valid window is [3, 4, 5], so index 2 expires
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # STEP 2 — CLEAN: Remove all back indices with smaller values
        # These elements can NEVER be the max while nums[i] is in the window
        # e.g. deque has [5, 3, 2] and nums[i]=4 → remove 3 and 2 → [5, 4]
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # STEP 3 — ADD: Append current index to the back of deque
        dq.append(i)

        # STEP 4 — COLLECT: Once window is full, front = index of window max
        # Window becomes full at i = k - 1 (0-indexed)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


## Test Cases
def test_max_sliding_window():
    """Test cases for max_sliding_window function."""

    # Test 1: Main example — standard sliding window
    result = max_sliding_window([1, 2, 1, 0, 4, 2, 6], 3)
    assert result == [2, 2, 4, 4, 6], f"Expected [2, 2, 4, 4, 6], got {result}"
    print("✓ Test 1 passed: Standard window — [2, 2, 4, 4, 6]")

    # Test 2: Second example — repeated maximums
    result = max_sliding_window([2, 6, 8, 3, 5, 4], 3)
    assert result == [8, 8, 8, 5], f"Expected [8, 8, 8, 5], got {result}"
    print("✓ Test 2 passed: Repeated max — [8, 8, 8, 5]")

    # Test 3: Window size equals array length — single global max
    result = max_sliding_window([3, 1, 4, 1, 5], 5)
    assert result == [5], f"Expected [5], got {result}"
    print("✓ Test 3 passed: k = len(nums) — single max [5]")

    # Test 4: Window size is 1 — output equals input
    result = max_sliding_window([4, 2, 7, 1], 1)
    assert result == [4, 2, 7, 1], f"Expected [4, 2, 7, 1], got {result}"
    print("✓ Test 4 passed: k = 1 — output mirrors input")

    # Test 5: Decreasing array — max is always the leftmost in window
    result = max_sliding_window([9, 7, 5, 3, 1], 3)
    assert result == [9, 7, 5], f"Expected [9, 7, 5], got {result}"
    print("✓ Test 5 passed: Decreasing array — [9, 7, 5]")

    # Test 6: Increasing array — max is always the rightmost in window
    result = max_sliding_window([1, 3, 5, 7, 9], 3)
    assert result == [5, 7, 9], f"Expected [5, 7, 9], got {result}"
    print("✓ Test 6 passed: Increasing array — [5, 7, 9]")

    # Test 7: All same elements
    result = max_sliding_window([4, 4, 4, 4], 2)
    assert result == [4, 4, 4], f"Expected [4, 4, 4], got {result}"
    print("✓ Test 7 passed: All same elements — [4, 4, 4]")

    # Test 8: Negative numbers
    result = max_sliding_window([-1, -3, -5, -2, -4], 3)
    assert result == [-1, -2, -2], f"Expected [-1, -2, -2], got {result}"
    print("✓ Test 8 passed: Negative numbers — [-1, -2, -2]")

    # Test 9: Edge case — empty array
    result = max_sliding_window([], 3)
    assert result is None, f"Expected None, got {result}"
    print("✓ Test 9 passed: Empty array — None")

    # Test 10: Edge case — k larger than array
    result = max_sliding_window([1, 2], 5)
    assert result is None, f"Expected None, got {result}"
    print("✓ Test 10 passed: k > len(nums) — None")

    # Test 11: LeetCode classic example
    result = max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert result == [3, 3, 5, 5, 6, 7], f"Expected [3, 3, 5, 5, 6, 7], got {result}"
    print("✓ Test 11 passed: LeetCode 239 classic — [3, 3, 5, 5, 6, 7]")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_max_sliding_window()


print(max_sliding_window([1, 2, 1, 0, 4, 2, 6], 3))
# Output: [2, 2, 4, 4, 6]

print(max_sliding_window([2, 6, 8, 3, 5, 4], 3))
# Output: [8, 8, 8, 5]
