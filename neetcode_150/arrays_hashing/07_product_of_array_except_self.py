"""
Problem Name: Product of Array Except Self

Problem Description:
Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].

You must solve it without using division and in O(n) time.

Example 1:
Input: [3, 5, -1, 5]
Output: [-25, -15, 75, -15]

Example 2:
Input: [0, 2, -1, -2, 8]
Output: [32, 0, 0, 0, 0]

Example 3:
Input: [1, 2]
Output: [2, 1]

Approach:

Algorithm (Prefix & Suffix Product):
1. Edge case: if array has less than 2 elements, return as-is
2. Build Prefix array (left to right):
   - Set prefix[0] = 1 (nothing before first element)
   - For each position i, multiply previous prefix with previous element
   - prefix[i] = prefix[i-1] * nums[i-1]
3. Build Suffix array (right to left):
   - Set suffix[n-1] = 1 (nothing after last element)
   - For each position i, multiply next suffix with next element
   - suffix[i] = suffix[i+1] * nums[i+1]
4. Build Result array:
   - For each position i, multiply prefix[i] * suffix[i]
   - This gives product of all elements except nums[i]
5. Return result

Solution: Prefix and Suffix Product
- Time Complexity: O(n) - three passes through the array
- Space Complexity: O(n) - storing prefix, suffix, and result arrays
"""

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Return an array where each element is the product of all
    other elements except the one at that index.

    Uses prefix (product of all elements to the left) and
    suffix (product of all elements to the right) arrays.
    e.g. [3, 5, -1, 5] -> [-25, -15, 75, -15]

    Args:
        nums: List of integers

    Returns:
        List[int]: Array of products except self
    """
    # Edge case: if array has less than 2 elements
    if len(nums) < 2:
        return nums

    n = len(nums)

    # Step-1: Build Prefix array (left to right →)
    # prefix[i] holds product of all elements BEFORE index i
    # e.g. [3, 5, -1, 5] -> prefix = [1, 3, 15, -15]
    prefix = [0] * n
    prefix[0] = 1
    for i in range(1, n):
        # Multiply previous prefix with previous element
        # e.g. prefix[2] = prefix[1] * nums[1] = 3 * 5 = 15
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Step-2: Build Suffix array (← right to left)
    # suffix[i] holds product of all elements AFTER index i
    # e.g. [3, 5, -1, 5] -> suffix = [-25, -5, 5, 1]
    suffix = [0] * n
    suffix[n - 1] = 1
    for i in range(n - 2, -1, -1):
        # Multiply next suffix with next element
        # e.g. suffix[2] = suffix[3] * nums[3] = 1 * 5 = 5
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Step-3: Build Result array
    # result[i] = prefix[i] * suffix[i]
    # prefix gives everything to the left, suffix gives everything to the right
    # Together they give product of everything EXCEPT nums[i]
    result = [0] * n
    for i in range(0, n):
        # e.g. result[0] = prefix[0] * suffix[0] = 1 * (-25) = -25
        result[i] = prefix[i] * suffix[i]

    return result


## Test Cases
def test_product_except_self():
    """Test cases for productExceptSelf function."""

    # Test 1: Edge case - single element
    assert productExceptSelf([1]) == [1], "Single element should return [1]"
    print("✓ Test 1 passed: Single element")

    # Test 2: Two elements
    result = productExceptSelf([1, 2])
    assert result == [2, 1], "Should return [2, 1]"
    print("✓ Test 2 passed: Two elements")

    # Test 3: Basic case with positive and negative numbers
    result = productExceptSelf([3, 5, -1, 5])
    assert result == [-25, -15, 75, -15], "Should return [-25, -15, 75, -15]"
    print("✓ Test 3 passed: Positive and negative numbers")

    # Test 4: Array containing zero
    result = productExceptSelf([0, 2, -1, -2, 8])
    assert result == [32, 0, 0, 0, 0], "Should return [32, 0, 0, 0, 0]"
    print("✓ Test 4 passed: Array containing zero")

    # Test 5: Array with multiple zeros
    result = productExceptSelf([0, 0, 3])
    assert result == [0, 0, 0], "Should return [0, 0, 0]"
    print("✓ Test 5 passed: Multiple zeros")

    # Test 6: All ones
    result = productExceptSelf([1, 1, 1, 1])
    assert result == [1, 1, 1, 1], "Should return [1, 1, 1, 1]"
    print("✓ Test 6 passed: All ones")

    # Test 7: Negative numbers
    result = productExceptSelf([-1, -2, -3])
    assert result == [6, 3, 2], "Should return [6, 3, 2]"
    print("✓ Test 7 passed: Negative numbers")

    # Test 8: Large numbers
    result = productExceptSelf([1, 2, 3, 4, 5])
    assert result == [120, 60, 40, 30, 24], "Should return [120, 60, 40, 30, 24]"
    print("✓ Test 8 passed: Large product values")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_product_except_self()


print(productExceptSelf([3, 5, -1, 5]))
# [-25, -15, 75, -15]

print(productExceptSelf([0, 2, -1, -2, 8]))
# [32, 0, 0, 0, 0]

print(productExceptSelf([1, 2]))
# [2, 1]