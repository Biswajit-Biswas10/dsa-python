"""
Problem Name: Two Sum

Problem Description:
Given an array of integers 'nums' and an integer 'target', return indices 
of the two numbers such that they add up to target.
Return the smaller index first. Each input has exactly one solution, 
and you may not use the same element twice.

Example 1:
Input: nums = [3, 4, 5, 6], target = 7
Output: [0, 1]  (because nums[0] + nums[1] = 3 + 4 = 7)

Example 2:
Input: nums = [4, 5, 6], target = 10
Output: [0, 2]  (because nums[0] + nums[2] = 4 + 6 = 10)

Example 3:
Input: nums = [2, 5, 7, 8], target = 13
Output: [1, 3]  (because nums[1] + nums[3] = 5 + 8 = 13)

Approach:

Algorithm:
1. Handle edge case: if array length is less than 2, return None
2. Use a hash map to store {value: index} as we iterate
3. For each element of i, compute the difference (target - current number)
   - If the difference exists in the hash map, we found our pair, return both indices
   - Otherwise, store the current value and its index in the hash map
4. If no pair found after full iteration, return None

Solution: Hash Map (Complement Lookup)
- Time Complexity: O(n) - single pass through the array
- Space Complexity: O(n) - hash map storing up to n elements
"""


from typing import List, Optional


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find two numbers in the array that add up to the target.

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List[int]: Indices of the two numbers, smaller index first
        None: If no valid pair exists or array length < 2
    """
    # Handle edge case
    # Need at least 2 elements to form a pair
    if len(nums) < 2:
        return None

    # Use a hash map to store {value: index}
    hash_map = {}

    # Iterate through the array to find a valid pair
    for i in range(len(nums)):
        # Compute the difference needed to reach the target
        diff = target - nums[i]

        # If the difference exists in the hash map, we found our pair
        if diff in hash_map:
            return [hash_map[diff], i]
        # Otherwise, store the current value and its index
        else:
            hash_map[nums[i]] = i

    # No valid pair found after full iteration
    return None


## Test Cases
def test_two_sum():
    """Test cases for two_sum function."""

    # Test 1: Edge case - empty array
    assert two_sum([], 5) == None, "Empty array should return None"
    print("✓ Test 1 passed: Empty array")

    # Test 2: Edge case - single element
    assert two_sum([1], 5) == None, "Single element should return None"
    print("✓ Test 2 passed: Single element")

    # Test 3: Valid pair - first two elements
    assert two_sum([3, 4, 5, 6], 7) == [0, 1], "3+4=7 should return [0, 1]"
    print("✓ Test 3 passed: Valid pair - first two elements")

    # Test 4: Valid pair - first and last elements
    assert two_sum([4, 5, 6], 10) == [0, 2], "4+6=10 should return [0, 2]"
    print("✓ Test 4 passed: Valid pair - first and last elements")

    # Test 5: Valid pair - middle and last elements
    assert two_sum([2, 5, 7, 8], 13) == [1, 3], "5+8=13 should return [1, 3]"
    print("✓ Test 5 passed: Valid pair - middle and last elements")

    # Test 6: Valid pair - duplicate values
    assert two_sum([3, 3], 6) == [0, 1], "3+3=6 should return [0, 1]"
    print("✓ Test 6 passed: Valid pair - duplicate values")

    # Test 7: No valid pair found
    assert two_sum([1, 2, 3], 10) == None, "No valid pair should return None"
    print("✓ Test 7 passed: No valid pair found")

    # Additional test cases
    assert two_sum([0, 4, 3, 0], 0) == [0, 3], "0+0=0 should return [0, 3]"
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3], "-2+-4=-6 should return [1, 3]"
    assert two_sum([1, 5, 8, 3, 9], 4) == [0, 3], "1+3=4 should return [0, 3]"

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_two_sum()


print(two_sum([3, 4, 5, 6], 7))    # [0, 1]
print(two_sum([4, 5, 6], 10))      # [0, 2]
print(two_sum([2, 5, 7, 8], 13))   # [1, 3]
