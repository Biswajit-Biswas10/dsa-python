"""
Problem Name: Permutation in String

Problem Description:
Given two strings s1 and s2, return True if s2 contains a permutation of s1,
or False otherwise.

In other words, return True if one of s1's permutations is a substring of s2.
A permutation means same characters with same frequency, order doesn't matter.

Example 1:
Input: s1 = "abc", s2 = "lacabee"
Output: True
Explanation: "cab" is a permutation of "abc" and is a substring of s2.

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: False
Explanation: No contiguous substring of size 3 in s2 has the same character
frequency as "abc".

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Approach:

Algorithm (Sliding Window + Frequency Counter):
1. Calculate the length of s1, call it k.
2. Build a frequency counter (hashmap) for s1.
3. Build a frequency counter (hashmap) for the first window of size k from s2.
4. Compare both frequency counters — if they match, return True.
5. Slide the window one position to the right:
   - Remove the outgoing (leftmost) character from the window counter.
   - Add the incoming (new rightmost) character to the window counter.
6. After each slide, compare both counters — if they match, return True.
7. Repeat steps 5-6 until the window reaches the end of s2.
8. If no window matched after scanning all of s2, return False.

Why Sliding Window works here:
- We need to check every contiguous substring of size k in s2.
- Instead of rebuilding the frequency counter from scratch for each window,
  I slide: remove one character out, add one character in — O(1) per slide.
- This avoids the brute force O(n * k) approach and gives us O(n).

Solution: Sliding Window with Frequency Counter
- Time Complexity:  O(n) - single pass through s2, each character added/removed once
- Space Complexity: O(k) - frequency counters store at most k unique characters
"""

from collections import Counter


def string_permutation(s1: str, s2: str) -> bool:
    """
    Return True if any permutation of s1 exists as a contiguous substring in s2.

    Uses a sliding window approach: maintain a frequency counter for the
    current window and compare it with s1's frequency counter at each step.

    Args:
        s1: The pattern string whose permutation we are looking for.
        s2: The string in which we search for the permutation.

    Returns:
        bool: True if a permutation of s1 is found in s2, False otherwise.
    """
    # Calculate window size (length of s1)
    k = len(s1)

    # Edge case: s1 is longer than s2, no permutation possible
    if k > len(s2):
        return False

    # Build frequency counter for s1
    # e.g. "abc" → {a:1, b:1, c:1}
    counter_s1 = Counter(s1)

    # Build frequency counter for the first window of size k from s2
    # e.g. s2 = "lacabee", k = 3 → "lac" → {l:1, a:1, c:1}
    counter_window = Counter(s2[0:k])

    # Initialize left pointer at start of window
    left = 0

    # Initialize right pointer at end of window
    right = k - 1

    # Slide the window across s2 until it reaches the end
    while right < len(s2):

        # COMPARE: Do both frequency counters match?
        # If yes, we found a permutation of s1 in s2
        if counter_s1 == counter_window:
            return True

        # REMOVE: Subtract the outgoing (leftmost) character from window counter
        # e.g. window "lac" sliding right → remove 'l'
        counter_window[s2[left]] -= 1

        # CLEANUP: If character count becomes 0, delete the key
        # This ensures accurate comparison with counter_s1
        if counter_window[s2[left]] == 0:
            del counter_window[s2[left]]

        # SLIDE: Move both pointers one position to the right
        left += 1
        right += 1

        # ADD: If right pointer is still within bounds, add the incoming
        # (new rightmost) character to window counter
        # e.g. window sliding right → add new character entering the window
        if right < len(s2):
            counter_window[s2[right]] += 1

    # No permutation found after scanning all of s2
    return False


## Test Cases
def test_string_permutation():
    """Test cases for string_permutation function."""

    # Test 1: Main example — "cab" is a permutation of "abc" in s2
    result = string_permutation("abc", "lacabee")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 1 passed: 'cab' found in 'lacabee' — True")

    # Test 2: No permutation exists — no window of size 3 matches
    result = string_permutation("abc", "lecaabee")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 2 passed: No permutation in 'lecaabee' — False")

    # Test 3: Exact match — s1 itself is in s2
    result = string_permutation("abc", "abc")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 3 passed: Exact match — True")

    # Test 4: s1 longer than s2 — impossible
    result = string_permutation("abcd", "ab")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 4 passed: s1 longer than s2 — False")

    # Test 5: Permutation at the end of s2
    result = string_permutation("abc", "xyzzbac")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 5 passed: 'bac' found at end — True")

    # Test 6: Single character match
    result = string_permutation("a", "bca")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 6 passed: Single character found — True")

    # Test 7: Single character no match
    result = string_permutation("a", "bcd")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 7 passed: Single character not found — False")

    # Test 8: Repeated characters in s1
    result = string_permutation("aab", "cbdaabt")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 8 passed: 'aab' with repeated chars — True")

    # Test 9: Permutation at the start of s2
    result = string_permutation("abc", "bacxyz")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 9 passed: 'bac' found at start — True")

    # Test 10: All same characters — match
    result = string_permutation("aaa", "baaab")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 10 passed: All same characters — True")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_string_permutation()


print(string_permutation("abc", "lacabee"))
# Output: True

print(string_permutation("abc", "lecaabee"))
# Output: False
