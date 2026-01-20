"""
Problem: 02_Reverse String
Pattern: Two Pointers
Approach:
- Two pointers moving from both ends toward center
- Swap characters at left and right pointers
- Move pointers inward until they meet
- Modify array in-place
Time: O(n) - Iterate through half the array, Where n is the length of the
array.
Space: O(1) - Constant extra space (in-place modification). No additional
data structure required regardless of the input size.
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Reverse the input array of characters in-place using two pointers.

    Args:
        s (List[str]): Input list of characters to reverse

    Returns:
        None: Modifies the input list in-place
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]

        # Move pointers toward center. Increase the left pointer index by
        # one and decrease the right pointer index by one.
        left += 1
        right -= 1


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
def main() -> None:
    """
    Run manual test cases for the reverse_string function.
    """
    test_cases = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
        ["a"],
        ["a", "b"],
        ["r", "a", "c", "e", "c", "a", "r"],
    ]

    for s in test_cases:
        original = s.copy()
        reverse_string(s)
        print(f"Input : {original}")
        print(f"Output: {s}")
        print("-" * 50)


if __name__ == "__main__":
    main() 