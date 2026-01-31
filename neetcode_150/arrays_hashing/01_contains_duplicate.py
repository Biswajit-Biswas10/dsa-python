
"""
Problem Name: Contains Duplicate

Problem Description:
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Approach

Algorithm:
1. Handle edge cases: arrays with 0 or 1 elements cannot have duplicates
2. Use a hash set to track elements we've seen
3. Iterate through the array:
   - If current element exists in the set, return `true` (duplicate found)
   - Otherwise, add the element to the set
4. If we complete the iteration without finding duplicates, return `false`

Solution: Hash Set
- Time Complexity: O(n) - where n is the length of the array
- Space Complexity: O(n) - for storing elements in the set
"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicate values.
    
    Args:
        nums: List of integers
        
    Returns:
        bool: True if duplicates exist, False otherwise
    """
    # Handle edge case
    # empty array and single element do not have duplicate values
    if len(nums) <= 1:
        return False

    # Use a set to track elements we've seen
    seen = set()

    # Iterate through the array
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


## Test Cases
def test_containsDuplicate():
    """Test cases for containsDuplicate function."""

    # Test 1: Empty array
    assert containsDuplicate([]) == False, "Empty array should return False"
    print("✓ Test 1 passed: Empty array")

    # Test 2: Single element
    assert containsDuplicate([1]) == False, "Single element should return False"
    print("✓ Test 2 passed: Single element")

    # Test 3: Contains duplicate (TRUE case)
    assert containsDuplicate([1, 2, 3, 1]) == True, "Array with duplicates should return True"
    print("✓ Test 3 passed: Contains duplicate")

    # Test 4: No duplicates (FALSE case)
    assert containsDuplicate([1, 2, 3, 4]) == False, "Array without duplicates should return False"
    print("✓ Test 4 passed: No duplicates")

    # Additional test cases
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert containsDuplicate([1, 5, -2, 4]) == False

    print("\n✅ All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_containsDuplicate()
