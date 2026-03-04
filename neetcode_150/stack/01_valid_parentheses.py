"""
Problem Name: Valid Parentheses

Problem Description:
Given a string "s" containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "([{}])"
Output: True
Explanation: Each bracket is closed in the correct nested order.

Example 2:
Input: s = "[(])"
Output: False
Explanation: The brackets are interleaved — '[' is closed by ')' instead of ']'.

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

Approach:

Algorithm (Stack — One Pass):
1. If the string is empty, return True (valid by definition).
2. If the length is odd, return False (odd-length can never be balanced).
3. Create an empty stack and a mapping of closing → opening brackets.
4. Loop through each character in the string, handling two cases:
   - OPENER (  ( [ {  ): Push it onto the stack.
   - CLOSER (  ) ] }  ): Check three failure conditions:
       a. Stack is empty       → no matching opener exists → return False
       b. Pop the top element  → if it doesn't match the expected opener → return False
       c. If it matches        → continue (pair is valid)
5. After the loop, return True only if the stack is empty.
   If the stack still has elements, some openers were never closed.

Why Stack works here:
- Brackets must follow LIFO (Last In, First Out) nesting order.
- The most recent unmatched opener must be closed first — exactly
  what a stack tracks.
- Three failure cases are exhaustive: empty stack on closer,
  mismatch after pop, leftover openers after loop.

Solution: Stack (One Pass with Bracket Mapping)
- Time Complexity:  O(n) - single pass through the string
- Space Complexity: O(n) - stack can grow up to n/2 in worst case
"""

from typing import List

def valid_parenthesis(s: str) -> bool:
    # base case: empty string is valid
    if not s:
        return True

    # odd-length string can never be balanced
    if len(s) % 2 != 0:
        return False

    # stack to track unmatched opening brackets
    stack = []

    # maps each closing bracket to its matching opener
    mapping = {')': '(', ']': '[', '}': '{'}

    # process each character in the string
    for char in s:
        if char in '([{':
            # opening bracket → push onto stack
            stack.append(char)
        else:
            # closing bracket → need a matching opener
            if not stack:
                # stack empty → no opener to match → invalid
                return False

            # pop the most recent opener
            top = stack.pop()

            # check if popped opener matches this closer
            if top != mapping[char]:
                # mismatch → invalid
                return False

    # if stack is empty, all brackets matched
    # if stack has leftovers, some openers were never closed
    return len(stack) == 0


## Test Cases
def test_valid_parenthesis():
    """Test cases for valid_parenthesis function."""

    # Test 1: Simple valid pair
    result = valid_parenthesis("()")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 1 passed: Simple valid pair — ()")

    # Test 2: Multiple valid pairs side by side
    result = valid_parenthesis("()[]{}")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 2 passed: Side by side pairs — ()[]{}")

    # Test 3: Nested mixed brackets
    result = valid_parenthesis("([{}])")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 3 passed: Nested mixed — ([{}])")

    # Test 4: Deep nesting
    result = valid_parenthesis("{([])}")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 4 passed: Deep nesting — {([])}")

    # Test 5: Side by side with nesting inside
    result = valid_parenthesis("([]){()}")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 5 passed: Mixed nesting — ([]){()}")

    # Test 6: Mismatched pair
    result = valid_parenthesis("(]")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 6 passed: Mismatched pair — (]")

    # Test 7: Interleaved brackets (arcs cross)
    result = valid_parenthesis("[(])")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 7 passed: Interleaved brackets — [(])")

    # Test 8: Crossed arcs with three types
    result = valid_parenthesis("({[}])")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 8 passed: Crossed arcs — ({[}])")

    # Test 9: All closers, no openers (empty stack case)
    result = valid_parenthesis("))))")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 9 passed: All closers — ))))")

    # Test 10: All openers, no closers (leftover openers case)
    result = valid_parenthesis("(((")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 10 passed: All openers — (((")

    # Test 11: Empty string — valid by definition
    result = valid_parenthesis("")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 11 passed: Empty string — valid")

    # Test 12: Single opener (odd length early return)
    result = valid_parenthesis("(")
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 12 passed: Single opener — odd length")

    # Test 13: Complex valid expression
    result = valid_parenthesis("{[]()()}")
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 13 passed: Complex valid — {[]()()}")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_valid_parenthesis()


print(valid_parenthesis("([{}])"))
# Output: True

print(valid_parenthesis("[(])"))
# Output: False
