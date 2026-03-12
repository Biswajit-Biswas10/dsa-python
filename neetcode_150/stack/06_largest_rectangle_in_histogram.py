"""
Problem Name: Largest Rectangle in Histogram

Problem Description:
You are given an array of integers "heights" where heights[i] represents
the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.

Example 1:
Input: heights = [7, 1, 7, 2, 2, 4]
Output: 8
Explanation:
    The largest rectangle spans bars at index 2 to 5.
    The shortest bar in this range has height 2.
    Rectangle area = min(7, 2, 2, 4) × 4 = 2 × 4 = 8

Example 2:
Input: heights = [1, 3, 7]
Output: 7
Explanation:
    Bar at index 2 alone gives the largest rectangle.
    Rectangle area = 7 × 1 = 7

Example 3:
Input: heights = [2, 4, 3]
Output: 6
Explanation:
    Bars at index 1 and 2: min(4, 3) × 2 = 3 × 2 = 6
    Also, all three bars: min(2, 4, 3) × 3 = 2 × 3 = 6

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

Approach:

Core Idea:
    For each bar, find how far it can extend LEFT and RIGHT before
    hitting a SHORTER bar. This gives the widest rectangle possible
    at that bar's height.

    For any group of consecutive bars:
        rectangle area = (shortest height in group) × (number of bars)

    The answer is the maximum area among all possible groups.

Algorithm (Monotonic Stack — One Pass + Cleanup):
1. If the heights list is empty, return 0.
2. Create a stack to store indices and initialise maxArea = 0.
3. Loop through each bar (index) in the array, handling two cases:
   - STACK TOP IS TALLER: If the current bar's height is less than
     the height at the index on top of the stack:
       a. Pop the top index from the stack.
       b. That popped bar found its RIGHT boundary (current index).
       c. Its LEFT boundary is the new stack top (or start of array).
       d. Compute: area = popped height × width.
       e. Update maxArea if this area is bigger.
       f. Repeat until the stack is empty or the top is no longer taller.
   - PUSH CURRENT BAR: Push the current index onto the stack.
4. After the loop, handle remaining bars in the stack (cleanup phase).
   Their right boundary is the END of the array. Pop each one and
   calculate its area the same way.
5. Return maxArea.

Why this is a Monotonic Increasing Stack:
- We only push onto the stack when the current height is NOT less
  than the stack top. This means the stack always stays in increasing
  order from bottom to top.
- When a shorter bar arrives, it pops all taller bars off the top,
  maintaining the increasing property.

Why Stack works here:
- This is a "Next Smaller Element" problem — for each bar, find the
  next bar to the left and right that is strictly shorter.
- The stack holds indices of bars still waiting for their right boundary.
- Each element is pushed once and popped at most once → O(n) total.
- On POP, we calculate the area because the popped bar has now found
  both its left boundary (new stack top) and right boundary (current bar).

Solution: Monotonic Stack (One Pass + Cleanup)
- Time Complexity:  O(n) - each element is pushed once and popped at most once
- Space Complexity: O(n) - stack can grow up to n in worst case (increasing heights)
"""

from typing import List


def largest_rectangle(heights: List[int]) -> int:
    # base case: empty heights list
    if not heights:
        return 0

    # stack to store indices and variable to track max area
    stack = []
    max_area = 0
    n = len(heights)

    # STEP 1: process each bar in the histogram
    for i in range(n):
        # check: is current bar SHORTER than the bar at stack top?
        while stack and heights[i] < heights[stack[-1]]:
            # pop the bar — current bar is its right boundary
            popped_height = heights[stack.pop()]

            # calculate width using left and right boundaries
            if not stack:
                width = i           # stretches from index 0 to i-1
            else:
                width = i - stack[-1] - 1

            # calculate area and update max
            area = popped_height * width
            max_area = max(max_area, area)

        # push current bar's index to wait for its right boundary
        stack.append(i)

    # STEP 2: cleanup — handle bars remaining in stack
    # their right boundary is the END of the array
    while stack:
        popped_height = heights[stack.pop()]

        if not stack:
            width = n               # stretches entire array
        else:
            width = n - stack[-1] - 1

        area = popped_height * width
        max_area = max(max_area, area)

    # return the largest rectangle area
    return max_area


## Test Cases
def test_largest_rectangle():
    """Test cases for largest_rectangle function."""

    # Test 1: General case — mixed heights
    result = largest_rectangle([7, 1, 7, 2, 2, 4])
    assert result == 8, f"Expected 8, got {result}"
    print("✓ Test 1 passed: Mixed heights — [7,1,7,2,2,4] → 8")

    # Test 2: Single tall bar is the answer
    result = largest_rectangle([1, 3, 7])
    assert result == 7, f"Expected 7, got {result}"
    print("✓ Test 2 passed: Single tall bar — [1,3,7] → 7")

    # Test 3: Wide rectangle beats tall bar
    result = largest_rectangle([2, 4, 3])
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Test 3 passed: Wide rectangle — [2,4,3] → 6")

    # Test 4: All same heights — entire array is the rectangle
    result = largest_rectangle([3, 3, 3, 3])
    assert result == 12, f"Expected 12, got {result}"
    print("✓ Test 4 passed: All same — [3,3,3,3] → 12")

    # Test 5: Strictly increasing — stack cleanup handles all
    result = largest_rectangle([1, 2, 3, 4, 5])
    assert result == 9, f"Expected 9, got {result}"
    print("✓ Test 5 passed: Strictly increasing — [1,2,3,4,5] → 9")

    # Test 6: Strictly decreasing — each bar pops immediately
    result = largest_rectangle([5, 4, 3, 2, 1])
    assert result == 9, f"Expected 9, got {result}"
    print("✓ Test 6 passed: Strictly decreasing — [5,4,3,2,1] → 9")

    # Test 7: Single element
    result = largest_rectangle([5])
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 7 passed: Single element — [5] → 5")

    # Test 8: Two elements — shorter limits the pair
    result = largest_rectangle([2, 4])
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 8 passed: Two elements — [2,4] → 4")

    # Test 9: Empty list — edge case
    result = largest_rectangle([])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 9 passed: Empty list — [] → 0")

    # Test 10: Valley pattern — dip in the middle
    result = largest_rectangle([6, 2, 5, 4, 5, 1, 6])
    assert result == 12, f"Expected 12, got {result}"
    print("✓ Test 10 passed: Valley pattern — [6,2,5,4,5,1,6] → 12")

    # Test 11: Mountain pattern — peak in the middle
    result = largest_rectangle([2, 1, 5, 6, 2, 3])
    assert result == 10, f"Expected 10, got {result}"
    print("✓ Test 11 passed: Mountain pattern — [2,1,5,6,2,3] → 10")

    # Test 12: All zeros
    result = largest_rectangle([0, 0, 0])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 12 passed: All zeros — [0,0,0] → 0")

    # Test 13: LeetCode classic — [2,1,5,6,2,3]
    result = largest_rectangle([2, 1, 5, 6, 2, 3])
    assert result == 10, f"Expected 10, got {result}"
    print("✓ Test 13 passed: LeetCode classic — [2,1,5,6,2,3] → 10")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_largest_rectangle()


print(largest_rectangle([7, 1, 7, 2, 2, 4]))
# Output: 8

print(largest_rectangle([2, 1, 5, 6, 2, 3]))
# Output: 10
