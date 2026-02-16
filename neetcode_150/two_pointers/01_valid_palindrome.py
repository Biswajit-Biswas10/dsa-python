"""
Problem Name: Valid Palindrome

Problem Description:
Given a string s, return True if it is a palindrome, otherwise return False.

A palindrome is a string that reads the same forward and backward. It is also
case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: True
Explanation: After considering only alphanumeric characters we have
"wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: False
Explanation: "tabacat" is not a palindrome.

Approach:

Algorithm (Two Pointers):
1. Initialise two pointers:
   - left  = 0              (start of the string)
   - right = len(s) - 1     (end of the string)
2. Loop while left < right, handling three cases:
   - SKIP LEFT:   s[left] is NOT alphanumeric  → advance left (left += 1)
   - SKIP RIGHT:  s[right] is NOT alphanumeric → advance right (right -= 1)
   - COMPARE:     both are alphanumeric        → compare lowercase versions
       - MISMATCH: s[left].lower() != s[right].lower() → return False
       - MATCH:    move both pointers inward (left += 1, right -= 1)
3. If the loop completes without mismatch, return True.

Why skip non-alphanumeric?
- Input "Was it a car or a cat I saw?" contains spaces and '?'
- These are not part of the palindrome check.
- Without skipping, we'd compare 'W' with '?' and wrongly return False.

Solution: Two Pointers (Inward Scan)
- Time Complexity:  O(n) - each character is visited at most once by each pointer
- Space Complexity: O(1) - only two pointer variables, no extra data structures
"""


def valid_palindrome(s: str) -> bool:
    """
    Return True if the string is a palindrome, ignoring non-alphanumeric
    characters and case differences.

    Uses two pointers moving inward from both ends, skipping non-alphanumeric
    characters and comparing lowercase versions.

    Args:
        s: Input string (may contain spaces, punctuation, mixed case)

    Returns:
        bool: True if s is a valid palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1

    # Move pointers inward until they meet or cross
    while left < right:

        # Skip non-alphanumeric characters from the left
        # e.g. " Was..." → skip space, land on 'W'
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        # e.g. "...saw?" → skip '?', land on 'w'
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        # e.g. 'W' vs 'w' → both become 'w' → match
        if s[left].lower() != s[right].lower():
            return False

        # Both characters match, move pointers inward
        left += 1
        right -= 1

    # All characters matched — it's a palindrome
    return True


## Test Cases
def test_valid_palindrome():
    """Test cases for valid_palindrome function."""

    # Test 1: Main example with spaces and punctuation
    result = valid_palindrome("Was it a car or a cat I saw?")
    assert result is True, "Should return True for classic palindrome sentence"
    print("✓ Test 1 passed: Palindrome with spaces and punctuation")

    # Test 2: Non-palindrome
    result = valid_palindrome("tab a cat")
    assert result is False, "Should return False for non-palindrome"
    print("✓ Test 2 passed: Non-palindrome string")

    # Test 3: Empty string
    result = valid_palindrome("")
    assert result is True, "Should return True for empty string"
    print("✓ Test 3 passed: Empty string")

    # Test 4: Single character
    result = valid_palindrome("a")
    assert result is True, "Should return True for single character"
    print("✓ Test 4 passed: Single character")

    # Test 5: Only non-alphanumeric characters
    result = valid_palindrome("!@#$%")
    assert result is True, "Should return True when no alphanumeric characters"
    print("✓ Test 5 passed: Only special characters")

    # Test 6: Mixed case palindrome
    result = valid_palindrome("RaceCar")
    assert result is True, "Should return True for case-insensitive palindrome"
    print("✓ Test 6 passed: Mixed case palindrome")

    # Test 7: Numeric palindrome
    result = valid_palindrome("12321")
    assert result is True, "Should return True for numeric palindrome"
    print("✓ Test 7 passed: Numeric palindrome")

    # Test 8: Alphanumeric mix
    result = valid_palindrome("A man, a plan, a canal: Panama")
    assert result is True, "Should return True for classic palindrome phrase"
    print("✓ Test 8 passed: Classic palindrome phrase")

    # Test 9: Two characters — palindrome
    result = valid_palindrome("aa")
    assert result is True, "Should return True for two same characters"
    print("✓ Test 9 passed: Two same characters")

    # Test 10: Two characters — not palindrome
    result = valid_palindrome("ab")
    assert result is False, "Should return False for two different characters"
    print("✓ Test 10 passed: Two different characters")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_valid_palindrome()


print(valid_palindrome("Was it a car or a cat I saw?"))
# Output: True

print(valid_palindrome("tab a cat"))
# Output: False

print(valid_palindrome(""))
# Output: True
