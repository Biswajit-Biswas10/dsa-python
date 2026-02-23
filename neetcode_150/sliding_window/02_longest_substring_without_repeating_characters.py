"""
Problem Name: Longest Substring Without Repeating Characters

Problem Description:
Given a string "s", find the length of the longest substring without
duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
- 0 <= s.length <= 1000
- s may consist of printable ASCII characters.

Approach:

Algorithm (Sliding Window with HashSet):
1. Edge case: if the string is empty, return 0.
2. Initialise three variables:
   - left       = 0      (left boundary of the window)
   - max_length = 0      (longest valid window seen so far)
   - seen       = set()  (characters currently in the window)
3. Expand the window by moving right from 0 to n-1:
   - SHRINK WINDOW: while s[right] is already in seen,
     remove s[left] from seen and increment left.
   - EXPAND WINDOW: add s[right] to seen.
   - UPDATE RESULT: max_length = max(max_length, right - left + 1).
4. Return max_length.

Why Sliding Window works here:
- I maintain a window [left, right] that ALWAYS contains unique characters.
- When a duplicate is found, I shrink from the left until the duplicate
  is removed — no need to restart from scratch.
- Every character is added and removed from the set at most once,
  so the total work across all iterations is O(n).

Solution: Sliding Window with HashSet
- Time Complexity:  O(n) - each character is visited at most twice
                           (once by right, once by left)
- Space Complexity: O(min(n, 128)) - set stores at most 128 ASCII characters,
                                      effectively O(1) for fixed character set
"""


def longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.

    Uses a sliding window approach: expand the window by moving right,
    and shrink from the left whenever a duplicate is found.

    Args:
        s: Input string consisting of printable ASCII characters.

    Returns:
        int: Length of the longest substring with all unique characters.
             Returns 0 if the string is empty.
    """
    # Edge case: empty string has no substring
    if len(s) == 0:
        return 0

    # Left boundary of our sliding window
    left = 0

    # Track the longest valid window seen so far
    max_length = 0

    # Set of characters currently inside the window [left, right]
    chars_in_window = set()

    # Move right pointer to expand the window
    for right in range(len(s)):

        # SHRINK WINDOW: duplicate found — remove from left until it's gone
        # e.g. s = "abcb" → when right hits 'b', remove 'a' then 'b' from left
        # If the character is seen, shrink window
        while s[right] in chars_in_window:
            chars_in_window.remove(s[left])
            left += 1

        # EXPAND WINDOW: add the current character (now guaranteed unique)
        chars_in_window.add(s[right])

        # UPDATE RESULT: check if this window is the longest so far
        # Window size = right - left + 1
        max_length = max(max_length, right - left + 1)

    # Return the longest substring length found
    return max_length


## Test Cases
def test_longest_substring():
    """Test cases for longest_substring function."""

    # Test 1: Main example — "xyz" is the longest unique substring
    result = longest_substring("zxyzxyz")
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 1 passed: 'zxyzxyz' — longest = 'xyz', length = 3")

    # Test 2: All same characters — only 1 unique at a time
    result = longest_substring("xxxx")
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 2 passed: 'xxxx' — longest = 'x', length = 1")

    # Test 3: Empty string — no substring possible
    result = longest_substring("")
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 3 passed: '' — empty string, length = 0")

    # Test 4: All unique characters — entire string is the answer
    result = longest_substring("abcdef")
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Test 4 passed: 'abcdef' — all unique, length = 6")

    # Test 5: Single character
    result = longest_substring("a")
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 5 passed: 'a' — single char, length = 1")

    # Test 6: Duplicate at the end
    result = longest_substring("abcdb")
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 6 passed: 'abcdb' — longest = 'abcd', length = 4")

    # Test 7: Repeating pattern
    result = longest_substring("abab")
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Test 7 passed: 'abab' — longest = 'ab', length = 2")

    # Test 8: Duplicate in the middle requiring multiple shrinks
    result = longest_substring("abcdba")
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 8 passed: 'abcdba' — longest = 'abcd' or 'cdba', length = 4")

    # Test 9: String with spaces and special characters
    result = longest_substring("ab cd")
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 9 passed: 'ab cd' — includes space, length = 5")

    # Test 10: Long repeating pattern
    result = longest_substring("abcabcbb")
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 10 passed: 'abcabcbb' — longest = 'abc', length = 3")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_longest_substring()


print(longest_substring("zxyzxyz"))
# Output: 3

print(longest_substring("xxxx"))
# Output: 1
