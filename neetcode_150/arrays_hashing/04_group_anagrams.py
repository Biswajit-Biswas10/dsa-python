"""
Problem Name: Group Anagrams

Problem Description:
Given an array of strings 'strs', group all anagrams together into sublists.
and return the output in any order.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

Example 2:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 3:
Input: strs = ["listen", "silent", "enlist", "tinsel"]
Output: [["listen", "silent", "enlist", "tinsel"]]

Approach:

Algorithm:
1. Handle edge case: if the input list is empty, return an empty list []
2. Use a hash map to store {sorted_string: [original_words]} as we iterate
3. For each word in the list, sort its characters to create a key
   - If the key exists in the hash map, append the original word to that list
   - Otherwise, create a new list with the original word 
4. Return all values from the hash map as a list of lists

Solution: Hash Map (Sorted String as Key)
- Time Complexity: O(n * k log k) - n strings, each sorted in k log k
- Space Complexity: O(n * k) - hash map storing all n strings of max length k
"""


from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group all anagrams together into sublists.

    Args:
        strs: List of strings to group

    Returns:
        List[List[str]]: List of grouped anagrams
        []: If input list is empty
    """
    # Handle edge case
    # Need at least 1 element to form a group
    if len(strs) < 1:
        return []

    # Use a hash map to store {sorted_key: [original_words]}
    hash_map = {}

    # Iterate through each word in the list
    for word in strs:
        # Sort the characters of the word to create a key
        # e.g., "cat" -> "act", "pots" -> "opst"
        sorted_key = "".join(sorted(word))

        # If the sorted key already exists, append word to that group
        if sorted_key in hash_map:
            hash_map[sorted_key].append(word)
        # Otherwise, create a new group with the current word
        else:
            hash_map[sorted_key] = [word]

    # Return all grouped anagram lists
    return list(hash_map.values())


## Test Cases
def test_group_anagrams():
    """Test cases for group_anagrams function."""

    # Test 1: Edge case - empty list
    assert group_anagrams([]) == [], "Empty list should return []"
    print("✓ Test 1 passed: Empty list")

    # Test 2: Edge case - single element
    assert group_anagrams(["a"]) == [["a"]], "Single element should return [['a']]"
    print("✓ Test 2 passed: Single element")

    # Test 3: Multiple anagram groups
    result = group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    # Sort inner lists and outer list for consistent comparison
    result_sorted = sorted([sorted(group) for group in result])
    expected_sorted = sorted([sorted(group) for group in [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]])
    assert result_sorted == expected_sorted, "Should group anagrams correctly"
    print("✓ Test 3 passed: Multiple anagram groups")

    # Test 4: Mixed lengths
    result = group_anagrams(["race", "care", "acre", "dog", "god", "z"])
    result_sorted = sorted([sorted(group) for group in result])
    expected_sorted = sorted([sorted(group) for group in [["race", "care", "acre"], ["dog", "god"], ["z"]]])
    assert result_sorted == expected_sorted, "Mixed lengths should group correctly"
    print("✓ Test 7 passed: Mixed lengths")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_group_anagrams()


print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
# [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(group_anagrams(["listen", "silent", "enlist", "tinsel"]))
# [["listen", "silent", "enlist", "tinsel"]]
