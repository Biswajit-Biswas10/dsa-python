"""
Problem Name: Car Fleet

Problem Description:
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers "position" and "speed", both of length n.
- position[i] is the position of the ith car (in miles)
- speed[i] is the speed of the ith car (in miles per hour)

The destination is at position "target" miles.

A car can not pass another car ahead of it. It can only catch up to another
car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same
speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the
destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1
Explanation:
    The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet,
    meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3
Explanation:
    The cars starting at 4 and 7 become a fleet at position 10.
    The cars starting at 1 and 0 never catch up to the car ahead of them.
    Thus, there are 3 car fleets that will arrive at the destination.

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- 0 < speed[i] <= 10^6
- All the values of position are unique.

Approach:

Algorithm (Monotonic Stack — Sort + One Pass):
1. If the position or speed list is empty, return 0.
2. Pair each car's position with its speed and sort by position in
   descending order (nearest to target first).
3. Initialise an empty stack to store arrival times of fleet leaders.
4. Loop through each car (from nearest to farthest from target):
   - Calculate: time = (target - position) / speed
   - SLOWER THAN FLEET AHEAD (time > stack top): Push time onto the
     stack — this car cannot catch the fleet ahead, so it becomes a
     new fleet leader.
   - FASTER OR EQUAL (time <= stack top): Skip — this car catches up
     to the fleet ahead and merges into it.
5. After the loop, return the length of the stack. Each element in
   the stack represents one distinct fleet.

Why Stack works here:
- Sorting by position descending lets us process cars from nearest to
  target first, simulating the "no overtaking" rule naturally.
- The stack holds arrival times of fleet leaders. A car with a greater
  arrival time is slower and will never be caught — it starts a new fleet.
- A car with a smaller or equal arrival time is faster — it will catch
  the fleet ahead and merge, so we skip it.
- Each car is processed exactly once → O(n) for the loop.
- The sort dominates the time complexity → O(n log n) overall.

Solution: Monotonic Stack (Sort + One Pass)
- Time Complexity:  O(n log n) - dominated by sorting the position-speed pairs
- Space Complexity: O(n) - stack can grow up to n in worst case (all separate fleets)
"""

from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    # Step 1: Handle empty input
    if not position or not speed:
        return 0

    # Step 2: Pair and sort by position descending
    pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

    # Step 3: Initialise empty stack
    stack = []

    # Step 4, 5, 6: Walk through each car
    for pos, spd in pairs:
        time = (target - pos) / spd

        if not stack or time > stack[-1]:
            stack.append(time)  # new fleet leader

    # Step 7: Return fleet count
    return len(stack)


## Test Cases
def test_car_fleet():
    """Test cases for car_fleet function."""

    # Test 1: Two cars forming one fleet at destination
    result = car_fleet(10, [1, 4], [3, 2])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 1 passed: Two cars merge at destination — target=10, pos=[1,4], spd=[3,2] → 1")

    # Test 2: Multiple fleets — some cars never catch up
    result = car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 2 passed: Three separate fleets — target=10, pos=[4,1,0,7], spd=[2,2,1,1] → 3")

    # Test 3: Single car — always one fleet
    result = car_fleet(10, [5], [1])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 3 passed: Single car — target=10, pos=[5], spd=[1] → 1")

    # Test 4: Empty input — no cars
    result = car_fleet(10, [], [])
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 4 passed: Empty input — target=10, pos=[], spd=[] → 0")

    # Test 5: All cars at different positions with same speed — no merging
    result = car_fleet(100, [0, 2, 4], [4, 2, 1])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 5 passed: All merge into one fleet — target=100, pos=[0,2,4], spd=[4,2,1] → 1")

    # Test 6: Cars already sorted by position — all separate fleets
    result = car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 6 passed: Mixed fleet merges — target=12, pos=[10,8,0,5,3], spd=[2,4,1,1,3] → 3")

    # Test 7: All cars same speed — every car is its own fleet
    result = car_fleet(10, [6, 2, 4], [3, 3, 3])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 7 passed: Same speed, different positions — target=10, pos=[6,2,4], spd=[3,3,3] → 3")

    # Test 8: Fastest car is farthest — all merge into one
    result = car_fleet(20, [5, 10, 15], [5, 3, 1])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 8 passed: Fastest car farthest back — target=20, pos=[5,10,15], spd=[5,3,1] → 1")

    # Test 9: Two cars same arrival time — count as one fleet
    result = car_fleet(10, [0, 5], [2, 1])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 9 passed: Same arrival time — target=10, pos=[0,5], spd=[2,1] → 1")

    # Test 10: Two fleets — car at 1 catches car at 3 but not car at 8
    result = car_fleet(10, [8, 3, 1], [1, 3, 4])
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Test 10 passed: Two fleets form — target=10, pos=[8,3,1], spd=[1,3,4] → 2")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_car_fleet()


print(car_fleet(10, [1, 4], [3, 2]))
# Output: 1

print(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))
# Output: 3
