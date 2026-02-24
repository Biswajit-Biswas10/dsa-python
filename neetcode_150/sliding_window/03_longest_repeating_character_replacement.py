"""
Problem Name: Longest Repeating Character Replacement

Problem Description:
You are given a string "s" consisting of only uppercase English letters and
an integer "k". You may choose any character in the string and change it to
any other uppercase English letter at most "k" times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.

Example 1:
Input: s = "AAABABB", k = 1
Output: 5
Explanation: Replace the 'B' at index 3 with 'A' to get "AAAAABB".
The longest repeating substring is "AAAAA" with length 5.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the 'B' at index 3 with 'A' to get "AAABBA".
The longest repeating substring is "AAAB" → treated as "AAAA" with length 4.

Constraints:
- 1 <= s.length <= 1000
- s consists of only uppercase English letters
- 0 <= k <= s.length

Approach:

Algorithm: (Sliding Window with Frequency Map):
1. Initialise variables:
   - left       = 0     (left boundary of the sliding window)
   - max_length = 0     (longest valid substring found so far)
   - freq_map   = {}    (character frequency count within the window)
2. Expand the window by moving right pointer from 0 to n-1:
   a. Add s[right] to freq_map (increment its count)
   b. Find max_freq = highest frequency among characters in the window
   c. Calculate replacements_needed = window_size - max_freq
   d. If replacements_needed > k:
      - Window is INVALID → shrink from left
      - Decrement freq_map[s[left]], move left += 1
   e. Update max_length with the current valid window size
3. Return max_length.

Why Sliding Window works here:
- The key insight is: for any window, we only need to replace the
  NON-majority characters. So replacements_needed = window_size - max_freq.
- If replacements_needed <= k, the window is valid (we CAN make all chars same).
- If replacements_needed > k, we shrink from the left to restore validity.
- The window never shrinks below its maximum valid size, ensuring we
  capture the longest valid substring.

Solution: Sliding Window with Frequency Map
- Time Complexity:  O(n) - single pass, each pointer moves at most n times
- Space Complexity: O(1) - freq_map holds at most 26 keys (uppercase A-Z)
"""


def character_replacement(s: str, k: int) -> int:
    """
    Return the length of the longest substring with same letters after
    at most k replacements.

    Uses a sliding window approach: track character frequencies within
    the window and check if the window is valid using the formula:
    replacements_needed = window_size - max_frequency.

    Args:
        s: String consisting of only uppercase English letters.
        k: Maximum number of character replacements allowed.

    Returns:
        int: Length of the longest valid substring.
    """
    # Edge case: empty string has no substring
    if not s:
        return 0

    # Left boundary of our sliding window
    left = 0

    # Track the longest valid substring found so far
    max_length = 0

    # Frequency map: counts each character inside the current window
    freq_map = {}

    # Total length of the string
    n = len(s)

    # Expand the window by moving right pointer through the string
    for right in range(n):

        # EXPAND: Add the new character to our frequency map
        # e.g. "AAAB" → freq_map = {A: 3, B: 1}
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1

        # Find the most frequent character count in the current window
        # This is the character we want to KEEP (replace everything else)
        max_freq = max(freq_map.values())

        # Current window size
        window_size = right - left + 1

        # How many characters we need to replace to make the window all same?
        # e.g. window "AAAB" → size=4, max_freq=3(A), need to replace 1(B)
        replacement_needed = window_size - max_freq

        # SHRINK: If we need more replacements than allowed, window is invalid
        # Remove the leftmost character and slide the window forward
        if replacement_needed > k:
            freq_map[s[left]] -= 1
            left += 1

        # UPDATE: Track the best valid window size seen so far
        max_length = max(max_length, right - left + 1)

    # Return the longest valid substring length
    return max_length


## Test Cases
def test_character_replacement():
    """Test cases for character_replacement function."""

    # Test 1: Main example — replace 1 'B' to get "AAAAA"
    result = character_replacement("AAABABB", 1)
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 1 passed: Replace 1 char — longest = 5")

    # Test 2: Replace 1 char in mixed string
    result = character_replacement("AABABBA", 1)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 2 passed: Mixed string — longest = 4")

    # Test 3: No replacements needed — already all same
    result = character_replacement("AAAA", 2)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 3 passed: All same chars — longest = 4")

    # Test 4: k = 0, no replacements allowed
    result = character_replacement("AABBA", 0)
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Test 4 passed: k=0, no replacements — longest = 2")

    # Test 5: k large enough to replace entire string
    result = character_replacement("ABCD", 3)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test 5 passed: Replace all chars — longest = 4")

    # Test 6: Single character string
    result = character_replacement("A", 0)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 6 passed: Single char — longest = 1")

    # Test 7: Two distinct characters with k=1
    result = character_replacement("ABAB", 1)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 7 passed: Alternating chars — longest = 3")

    # Test 8: Empty string
    result = character_replacement("", 1)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 8 passed: Empty string — longest = 0")

    # Test 9: All different characters with sufficient k
    result = character_replacement("ABCDE", 4)
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 9 passed: All different, k covers all — longest = 5")

    # Test 10: Replacement window spans full string
    result = character_replacement("BAAAB", 2)
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 10 passed: Window spans full string — longest = 5")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_character_replacement()


print(character_replacement("AAABABB", 1))
# Output: 5

print(character_replacement("AABABBA", 1))
# Output: 4
