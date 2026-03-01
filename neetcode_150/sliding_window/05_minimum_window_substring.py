"""
Problem Name: Minimum Window Substring

Problem Description:
Given two strings "s" and "t", return the shortest substring of "s" such
that every character in "t" (including duplicates) is present in the substring.
If no such substring exists, return an empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: "BANC" is the shortest substring containing 'A', 'B', and 'C'.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's are required, but s only has one 'a'.

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of uppercase and lowercase English letters.

Approach:

Algorithm (Sliding Window — Two Pointers):
1. Build a frequency map of characters in t (t_freq).
2. Initialise two pointers (left, right) both at 0 — they define my window.
3. Track two counters:
   - required = number of unique characters in 't' that must be satisfied
   - have     = number of unique characters currently satisfied in the window
4. Expand the window by moving right:
   - Add s[right] to window_freq.
   - If this character's count now matches t_freq, increment have.
5. When have == required (valid window found), shrink from the left:
   - Update result if current window is smaller.
   - Remove s[left] from window_freq.
   - If this breaks a character's required count, decrement have.
   - Move left forward.
6. Return the smallest valid window found, or "" if none exists.

Why Sliding Window works here:
- We need a contiguous substring — perfect for a window approach.
- Expanding right explores new candidates; shrinking left finds the minimum.
- The "have vs required" check lets us know EXACTLY when the window is valid
  without re-scanning all character counts each time → O(1) per step.

Solution: Sliding Window (Two Pointers with Frequency Maps)
- Time Complexity:  O(n + m) — n = len(s), m = len(t), each pointer moves at most n times
- Space Complexity: O(m) — frequency maps store at most all unique characters in t
"""

from typing import List


def min_window_substring(s: str, t: str) -> str:
    """
    Return the minimum window substring of s that contains all characters of t.

    Uses a sliding window approach: expand right to find valid windows,
    shrink left to find the minimum valid window.

    Args:
        s: The source string to search within.
        t: The target string whose characters must all be present.

    Returns:
        str: The shortest substring of s containing all characters of t.
             Returns "" if no such substring exists.
    """
    # Edge case: t is empty or longer than s — no valid window possible
    if not t or len(t) > len(s):
        return ""

    # Step 1: Build frequency map for target string t
    # e.g. t = "ABC" → t_freq = {'A': 1, 'B': 1, 'C': 1}
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    # Frequency map for characters in our current window
    window_freq = {}

    # Left pointer of the sliding window
    left = 0

    # have: how many unique chars in t are fully satisfied in the window
    # required: total unique chars in t that need to be satisfied
    have = 0
    required = len(t_freq)

    # Track the best (smallest) valid window found so far
    result_len = float("inf")
    result = ""

    # Step 2: Expand the window by moving right pointer
    for right in range(len(s)):
        char = s[right]

        # Add the right character to our window's frequency map
        window_freq[char] = window_freq.get(char, 0) + 1

        # Check: did adding this character satisfy a required character?
        # e.g. t_freq['A'] = 1, window_freq['A'] just became 1 → match!
        if char in t_freq and window_freq[char] == t_freq[char]:
            have += 1

        # Step 3: Window is valid (contains all of t) — try to shrink it
        while have == required:

            # Update result if this window is smaller than our best
            current_len = right - left + 1
            if current_len < result_len:
                result_len = current_len
                result = s[left : right + 1]

            # Shrink window: remove the leftmost character
            left_char = s[left]
            window_freq[left_char] -= 1

            # Check: did removing this character break a requirement?
            # e.g. window_freq['A'] dropped below t_freq['A'] → no longer satisfied
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                have -= 1

            # Move left pointer forward (shrink window)
            left += 1

    # Return the smallest valid window, or "" if none was found
    if result_len == float("inf"):
        return ""
    return result


## Test Cases
def test_min_window_substring():
    """Test cases for min_window_substring function."""

    # Test 1: Main example — "BANC" contains A, B, C
    result = min_window_substring("ADOBECODEBANC", "ABC")
    assert result == "BANC", f'Expected "BANC", got "{result}"'
    print('✓ Test 1 passed: Classic example — window = "BANC"')

    # Test 2: Entire string is the window
    result = min_window_substring("a", "a")
    assert result == "a", f'Expected "a", got "{result}"'
    print('✓ Test 2 passed: Single char match — window = "a"')

    # Test 3: Target has duplicate chars not satisfiable
    result = min_window_substring("a", "aa")
    assert result == "", f'Expected "", got "{result}"'
    print('✓ Test 3 passed: Not enough chars — no window')

    # Test 4: Empty target string
    result = min_window_substring("abc", "")
    assert result == "", f'Expected "", got "{result}"'
    print('✓ Test 4 passed: Empty target — no window')

    # Test 5: Target longer than source
    result = min_window_substring("ab", "abc")
    assert result == "", f'Expected "", got "{result}"'
    print('✓ Test 5 passed: Target longer than source — no window')

    # Test 6: Window at the very start
    result = min_window_substring("ABCD", "AB")
    assert result == "AB", f'Expected "AB", got "{result}"'
    print('✓ Test 6 passed: Window at start — window = "AB"')

    # Test 7: Window at the very end
    result = min_window_substring("XYZAB", "AB")
    assert result == "AB", f'Expected "AB", got "{result}"'
    print('✓ Test 7 passed: Window at end — window = "AB"')

    # Test 8: Duplicate characters in target
    result = min_window_substring("ADOBECODEBANNC", "AABC")
    assert result == "ADOBECODEBA", f'Expected "ADOBECODEBA", got "{result}"'
    print(f'✓ Test 8 passed: Duplicate target chars — window = "{result}"')

    # Test 9: Source equals target exactly
    result = min_window_substring("ABC", "ABC")
    assert result == "ABC", f'Expected "ABC", got "{result}"'
    print('✓ Test 9 passed: Exact match — window = "ABC"')

    # Test 10: Multiple valid windows — should return smallest
    result = min_window_substring("AABCBCA", "ABC")
    assert len(result) == 3, f'Expected length 3, got "{result}" (length {len(result)})'
    print(f'✓ Test 10 passed: Multiple windows — smallest = "{result}"')

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_min_window_substring()


print(min_window_substring("ADOBECODEBANC", "ABC"))
# Output: "BANC"

print(min_window_substring("a", "aa"))
# Output: ""
