"""
Problem Name: Evaluate Reverse Polish Notation

Problem Description:
You are given an array of strings "tokens" that represents a valid
arithmetic expression in Reverse Polish Notation (RPN).

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include '+', '-', '*', and '/'.
- Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1", "2", "+", "3", "*", "4", "-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5

Example 2:
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: 4 + (13 / 5) = 4 + 2 = 6

Example 3:
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator (+, -, *, /) or an integer in range [-200, 200]

Approach:

Algorithm (Stack — One Pass):
1. If the tokens list is empty, return None (nothing to evaluate).
2. Create an empty stack to store operands and intermediate results.
3. Loop through each token in the list, handling two cases:
   - NUMBER: Convert to integer and push it onto the stack.
   - OPERATOR (+, -, *, /): Pop two values from the stack:
       a. First pop  → right operand  (last pushed, sits on top)
       b. Second pop → left operand   (first pushed, sits deeper)
       c. Compute: left <operator> right
       d. Push the result back onto the stack
4. After the loop, the stack contains exactly one element — the final result.
   Pop and return it.

Why pop order matters (right first, then left):
- In RPN, "9 4 -" means 9 - 4, not 4 - 9.
- 9 is pushed first (deeper), 4 is pushed second (top).
- Stack is LIFO → first pop gives 4 (right), second pop gives 9 (left).
- For + and * order doesn't matter (commutative).
- For - and / order is critical (non-commutative).

Why Stack works here:
- RPN eliminates the need for parentheses and operator precedence rules.
- Each operator acts on the two most recent operands — exactly what
  a stack provides via its LIFO (Last In, First Out) property.
- Intermediate results get pushed back, becoming operands for later operators.

Solution: Stack (One Pass)
- Time Complexity:  O(n) - single pass through the tokens list
- Space Complexity: O(n) - stack can grow up to n/2 in worst case
"""

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    # base case: empty tokens list
    if not tokens:
        return None

    # stack to store operands and intermediate results
    stack = []

    # process each token in the list
    for token in tokens:
        if token not in ('+', '-', '*', '/'):
            # operand → convert to integer and push onto stack
            stack.append(int(token))
        else:
            # operator → pop two operands (right first, then left)
            right = stack.pop()
            left = stack.pop()

            # perform the operation based on the operator
            if token == '+':
                compute = left + right
            elif token == '-':
                compute = left - right
            elif token == '*':
                compute = left * right
            elif token == '/':
                # truncate toward zero (not floor division)
                compute = int(left / right)

            # push the result back onto the stack
            stack.append(compute)

    # the final result is the only element left on the stack
    return stack.pop()


## Test Cases
def test_eval_rpn():
    """Test cases for eval_rpn function."""

    # Test 1: Simple addition
    result = eval_rpn(["1", "2", "+"])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 1 passed: Simple addition — 1 + 2 = 3")

    # Test 2: Simple subtraction
    result = eval_rpn(["5", "3", "-"])
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Test 2 passed: Simple subtraction — 5 - 3 = 2")

    # Test 3: Simple multiplication
    result = eval_rpn(["4", "3", "*"])
    assert result == 12, f"Expected 12, got {result}"
    print("✓ Test 3 passed: Simple multiplication — 4 * 3 = 12")

    # Test 4: Simple division (truncates toward zero)
    result = eval_rpn(["7", "2", "/"])
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 4 passed: Simple division — 7 / 2 = 3")

    # Test 5: Chained operations — ((1 + 2) * 3) - 4 = 5
    result = eval_rpn(["1", "2", "+", "3", "*", "4", "-"])
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 5 passed: Chained operations — ((1 + 2) * 3) - 4 = 5")

    # Test 6: Division with addition — 4 + (13 / 5) = 6
    result = eval_rpn(["4", "13", "5", "/", "+"])
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Test 6 passed: Division with addition — 4 + (13 / 5) = 6")

    # Test 7: Complex expression — evaluates to 22
    result = eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    assert result == 22, f"Expected 22, got {result}"
    print("✓ Test 7 passed: Complex expression — result = 22")

    # Test 8: Negative division truncates toward zero — -7 / 2 = -3
    result = eval_rpn(["7", "-2", "/"])
    assert result == -3, f"Expected -3, got {result}"
    print("✓ Test 8 passed: Negative division — 7 / (-2) = -3")

    # Test 9: Single operand — returns itself
    result = eval_rpn(["42"])
    assert result == 42, f"Expected 42, got {result}"
    print("✓ Test 9 passed: Single operand — 42")

    # Test 10: Negative numbers as operands
    result = eval_rpn(["-3", "4", "+"])
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 10 passed: Negative operand — (-3) + 4 = 1")

    # Test 11: Empty tokens list
    result = eval_rpn([])
    assert result is None, f"Expected None, got {result}"
    print("✓ Test 11 passed: Empty tokens — None")

    # Test 12: All four operators
    result = eval_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"])
    assert result == 14, f"Expected 14, got {result}"
    print("✓ Test 12 passed: All four operators — 5 + ((1 + 2) * 4) - 3 = 14")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_eval_rpn()


print(eval_rpn(["1", "2", "+", "3", "*", "4", "-"]))
# Output: 5

print(eval_rpn(["4", "13", "5", "/", "+"]))
# Output: 6
