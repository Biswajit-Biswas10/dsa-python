"""
Problem Name: Top K Frequent Elements

Problem Description:
Given an integer array 'nums' and an integer 'k', return the 'k' most frequent
elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [3, 2]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Example 3:
Input: nums = [1,2,3,4,4,7,7,9,9,9], k = 3
Output: [9, 7, 4]

Approach:

Algorithm:
1. Handle edge case: if the input array is empty, return None
2. Use a hash map to store {number: frequency} {key: value} as we iterate
3. For each number in the array, count its frequency
   - If the number exists in the hash map, increment the count
   - Otherwise, add it with a count of 1
4. Sort the hash map keys by their frequency values in descending order
5. Return the first k keys from the sorted result

Solution: Hash Map + Sorting
- Time Complexity: O(n log n) - Hash map building is O(n), sorting is O(n log n)
- Space Complexity: O(n) - hash map storing all n elements
"""


from typing import List, Optional


def top_k_freq_element(nums: List[int], k: int) -> Optional[List[int]]:
    """
    Return the k most frequent elements from the given array.

    Args:
        nums: List of integers
        k: Number of top frequent elements to return

    Returns:
        List[int]: List of k most frequent elements
        None: If input array is empty
    """
    # Handle edge case
    # Need at least 1 element to find frequent elements
    if len(nums) < 1:
        return None

    # Use a hash map to store {number: frequency}
    hash_map = {}

    # Iterate through each number in the array
    for num in nums:
        # If the number already exists, increment its count
        # e.g., {1: 1, 2: 2, 3: 3}
        if num in hash_map:
            hash_map[num] += 1
        # Otherwise, add the number with a count of 1
        else:
            hash_map[num] = 1

    # Sort keys by their frequency values in descending order
    # e.g., {1:1, 2:2, 3:3} -> [3, 2, 1]
    sort_key = sorted(hash_map, key=hash_map.get, reverse=True)

    # Return the first k elements
    return sort_key[:k]


## Test Cases
def test_top_k_freq_element():
    """Test cases for top_k_freq_element function."""

    # Test 1: Edge case - empty array
    assert top_k_freq_element([], 1) is None, "Empty array should return None"
    print("✓ Test 1 passed: Empty array")

    # Test 2: Edge case - single element
    assert top_k_freq_element([42], 1) == [42], "Single element should return [42]"
    print("✓ Test 2 passed: Single element")

    # Test 3: Multiple frequencies
    result = top_k_freq_element([1, 2, 2, 3, 3, 3], 2)
    assert sorted(result) == sorted([3, 2]), "Should return top 2 frequent elements"
    print("✓ Test 3 passed: Multiple frequencies")

    # Test 4: Single element repeated
    result = top_k_freq_element([7, 7], 1)
    assert result == [7], "Should return [7]"
    print("✓ Test 4 passed: Single element repeated")

    # Test 5: Larger array
    result = top_k_freq_element([1, 2, 3, 4, 4, 7, 7, 9, 9, 9], 3)
    assert sorted(result) == sorted([9, 7, 4]), "Should return top 3 frequent elements"
    print("✓ Test 5 passed: Larger array")

    # Test 6: All same elements
    result = top_k_freq_element([5, 5, 5, 5], 1)
    assert result == [5], "All same elements should return [5]"
    print("✓ Test 6 passed: All same elements")

    # Test 7: Negative numbers
    result = top_k_freq_element([-1, -1, -2, -2, -2, 3], 2)
    assert sorted(result) == sorted([-2, -1]), "Should handle negative numbers"
    print("✓ Test 7 passed: Negative numbers")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_top_k_freq_element()


print(top_k_freq_element([1, 2, 2, 3, 3, 3], 2))
# [3, 2]

print(top_k_freq_element([7, 7], 1))
# [7]

print(top_k_freq_element([1, 2, 3, 4, 4, 7, 7, 9, 9, 9], 3))
# [9, 7, 4]
