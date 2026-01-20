"""
Problem: 01_Valid Palindrome
Pattern: Two Pointers
Approach:
- Two pointers moving from both ends toward center
- Skip non-alphanumeric characters
- Compare characters case-insensitively
- Return False on first mismatch
Time: O(n) - Iterate through the entire string. 
Space: O(1) - constant extra space. 
"""

def is_palindrome(s: str) -> bool:
    """
    Determine if the string is a palindrome, considering only alphanumeric
    characters and ignoring case, spaces, and punctuation.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare case-insensitively
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
def main() -> None:
    """
    Run manual test cases for the is_palindrome function.
    """
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "1A@2!3 23!2@a1",
        "No 'x' in Nixon",
        "12321",
    ]

    for s in test_cases:
        print(f"Input : {s}")
        print(f"Output: {is_palindrome(s)}")
        print("-" * 50)


if __name__ == "__main__":
    main()
