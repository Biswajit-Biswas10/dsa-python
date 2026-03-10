"""
Problem Name: Daily Temperatures

Problem Description:
You are given an array of integers "temperatures" where temperatures[i]
represents the daily temperature on the ith day.

Return an array "result" where result[i] is the number of days after the
ith day before a warmer temperature appears on a future day. If there is
no day in the future where a warmer temperature will appear for the ith
day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30, 38, 30, 36, 35, 40, 28]
Output: [1, 4, 1, 2, 1, 0, 0]
Explanation:
    Day 0 (30) → Day 1 (38) is warmer → 1 day wait
    Day 1 (38) → Day 5 (40) is warmer → 4 days wait
    Day 2 (30) → Day 3 (36) is warmer → 1 day wait
    Day 3 (36) → Day 5 (40) is warmer → 2 days wait
    Day 4 (35) → Day 5 (40) is warmer → 1 day wait
    Day 5 (40) → No warmer day exists → 0
    Day 6 (28) → No warmer day exists → 0

Example 2:
Input: temperatures = [22, 22, 22]
Output: [0, 0, 0]
Explanation: No day has a strictly warmer future day.

Example 3:
Input: temperatures = [25, 30, 35, 40]
Output: [1, 1, 1, 0]
Explanation: Each day's next day is warmer, except the last.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

Approach:

Algorithm (Monotonic Stack — One Pass):
1. If the temperatures list is empty, return an empty list.
2. Create a result array of size n filled with 0s and an empty stack
   to store indices of days waiting for a warmer temperature.
3. Loop through each day (index) in the array, handling two cases:
   - STACK TOP IS COOLER: If the current day's temperature is greater
     than the temperature at the index on top of the stack:
       a. Pop the top index from the stack.
       b. Compute: result[popped] = current index - popped index.
       c. Repeat until the stack is empty or the top is no longer cooler.
   - PUSH CURRENT DAY: Push the current index onto the stack so it can
     wait for its own future warmer day.
4. After the loop, return the result array. Any index that was never
   popped from the stack will naturally have 0 in the result.

Why this is a Monotonic Decreasing Stack:
- We only push onto the stack when the current temperature is NOT greater
  than the stack top. This means the stack always stays in decreasing
  order from bottom to top.
- When a warmer day arrives, it pops all cooler days off the top,
  maintaining the decreasing property.

Why Stack works here:
- This is a "Next Greater Element" problem — for each element, find the
  next element to the right that is strictly greater.
- The stack holds indices of days still waiting for a warmer day.
- Each element is pushed once and popped at most once → O(n) total.
- Instead of storing the greater value, we store the distance (index
  difference), which gives the number of days waited.

Solution: Monotonic Stack (One Pass)
- Time Complexity:  O(n) - each element is pushed once and popped at most once
- Space Complexity: O(n) - stack can grow up to n in worst case (decreasing temps)
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    # base case: empty temperatures list
    if not temperatures:
        return []

    # result array filled with 0s and stack to store indices
    n = len(temperatures)
    result = [0] * n
    stack = []

    # process each day in the list
    for i in range(n):
        # check: is today warmer than the day at stack top?
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # pop the waiting day — today is its warmer day
            popped = stack.pop()
            # calculate the number of days waited
            result[popped] = i - popped

        # push current day onto stack to wait for its warmer day
        stack.append(i)

    # return the result (unpopped days naturally stay 0)
    return result


## Test Cases
def test_daily_temperatures():
    """Test cases for daily_temperatures function."""

    # Test 1: General case — mixed temperatures
    result = daily_temperatures([30, 38, 30, 36, 35, 40, 28])
    assert result == [1, 4, 1, 2, 1, 0, 0], f"Expected [1, 4, 1, 2, 1, 0, 0], got {result}"
    print("✓ Test 1 passed: Mixed temperatures — [30,38,30,36,35,40,28] → [1,4,1,2,1,0,0]")

    # Test 2: All same temperatures — no warmer day exists
    result = daily_temperatures([22, 22, 22])
    assert result == [0, 0, 0], f"Expected [0, 0, 0], got {result}"
    print("✓ Test 2 passed: All same — [22,22,22] → [0,0,0]")

    # Test 3: Strictly decreasing — no warmer day for anyone
    result = daily_temperatures([40, 35, 30, 25])
    assert result == [0, 0, 0, 0], f"Expected [0, 0, 0, 0], got {result}"
    print("✓ Test 3 passed: Strictly decreasing — [40,35,30,25] → [0,0,0,0]")

    # Test 4: Strictly increasing — each day waits exactly 1 day
    result = daily_temperatures([25, 30, 35, 40])
    assert result == [1, 1, 1, 0], f"Expected [1, 1, 1, 0], got {result}"
    print("✓ Test 4 passed: Strictly increasing — [25,30,35,40] → [1,1,1,0]")

    # Test 5: Single element — no future day exists
    result = daily_temperatures([50])
    assert result == [0], f"Expected [0], got {result}"
    print("✓ Test 5 passed: Single element — [50] → [0]")

    # Test 6: Two elements — warmer day exists
    result = daily_temperatures([30, 40])
    assert result == [1, 0], f"Expected [1, 0], got {result}"
    print("✓ Test 6 passed: Two elements (warmer) — [30,40] → [1,0]")

    # Test 7: Two elements — no warmer day
    result = daily_temperatures([40, 30])
    assert result == [0, 0], f"Expected [0, 0], got {result}"
    print("✓ Test 7 passed: Two elements (cooler) — [40,30] → [0,0]")

    # Test 8: Empty list — edge case
    result = daily_temperatures([])
    assert result == [], f"Expected [], got {result}"
    print("✓ Test 8 passed: Empty list — [] → []")

    # Test 9: Valley pattern — dip then rise
    result = daily_temperatures([40, 30, 35, 45])
    assert result == [3, 1, 1, 0], f"Expected [3, 1, 1, 0], got {result}"
    print("✓ Test 9 passed: Valley pattern — [40,30,35,45] → [3,1,1,0]")

    # Test 10: Long wait for last element
    result = daily_temperatures([30, 30, 30, 30, 31])
    assert result == [4, 3, 2, 1, 0], f"Expected [4, 3, 2, 1, 0], got {result}"
    print("✓ Test 10 passed: Long wait — [30,30,30,30,31] → [4,3,2,1,0]")

    # Test 11: Alternating temperatures
    result = daily_temperatures([30, 40, 30, 40, 30])
    assert result == [1, 0, 1, 0, 0], f"Expected [1, 0, 1, 0, 0], got {result}"
    print("✓ Test 11 passed: Alternating — [30,40,30,40,30] → [1,0,1,0,0]")

    # Test 12: LeetCode example — [73,74,75,71,69,72,76,73]
    result = daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    assert result == [1, 1, 4, 2, 1, 1, 0, 0], f"Expected [1,1,4,2,1,1,0,0], got {result}"
    print("✓ Test 12 passed: LeetCode example — [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_daily_temperatures()


print(daily_temperatures([30, 38, 30, 36, 35, 40, 28]))
# Output: [1, 4, 1, 2, 1, 0, 0]

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
