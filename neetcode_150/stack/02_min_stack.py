"""
Problem Name: Min Stack

Problem Description:
Design a stack class that supports the push, pop, top, and getMin operations.

- MinStack()        initializes the stack object.
- void push(val)    pushes the element val onto the stack.
- void pop()        removes the element on the top of the stack.
- int top()         gets the top element of the stack.
- int getMin()      retrieves the minimum element in the stack.

Each function must run in O(1) time.

Example 1:
Input:  ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null, null, null, null, 0, null, 2, 1]

Explanation:
    MinStack minStack = new MinStack()
    minStack.push(1)    → stack: [1]
    minStack.push(2)    → stack: [1, 2]
    minStack.push(0)    → stack: [1, 2, 0]
    minStack.getMin()   → return 0
    minStack.pop()      → stack: [1, 2]
    minStack.top()      → return 2
    minStack.getMin()   → return 1

Constraints:
    - -2^31 <= val <= 2^31 - 1
    - pop(), top(), and getMin() operations will always be called on non-empty stacks
    - At most 3 * 10^4 calls will be made to push, pop, top, and getMin

Approach:

Key Insight:
    The challenge is getMin() in O(1) time.
    A simple loop to find the minimum would be O(n) — not allowed.
    When we pop the current minimum, we need to instantly know the previous minimum.
    This means we need to REMEMBER the history of minimums.

Algorithm (Two Stack Approach):
    1. Maintain TWO stacks side by side:
         - mainStack  → stores all pushed values normally
         - minStack   → stores the minimum value at each point in time

    2. push(val):
         - Append val to mainStack
         - If minStack is empty, append val to minStack
         - Otherwise, append min(val, current_min) to minStack
           (this records what the minimum is AFTER this push)

    3. pop():
         - Pop from BOTH stacks simultaneously
         - This restores the minimum to what it was before the last push

    4. top():
         - Return the last element of mainStack (index -1)

    5. getMin():
         - Return the last element of minStack (index -1)
         - The top of minStack always holds the current minimum

Why Two Stacks Work:
    Every element in minStack answers the question:
    "What is the minimum in mainStack up to this point?"

    When we pop from mainStack, we also pop from minStack,
    which restores the minimum to its previous value — instantly.

    MAIN STACK       MIN STACK        EVENT
    ──────────       ─────────        ──────────────────────────
    [1]              [1]              push(1) → min(1, ∞) = 1
    [1, 2]           [1, 1]          push(2) → min(2, 1) = 1
    [1, 2, 0]        [1, 1, 0]       push(0) → min(0, 1) = 0
    [1, 2]           [1, 1]          pop()   → 0 removed, min back to 1
    [1]              [1]             pop()   → 2 removed, min back to 1

Solution: Two Stack Approach
    - Time Complexity:  O(1) for all four operations
    - Space Complexity: O(n) — minStack grows at the same rate as mainStack
"""


class MinStack:

    def __init__(self):
        self.mainStack = []   # stores all values
        self.minStack  = []   # stores minimum at each state

    def push(self, val: int) -> None:
        self.mainStack.append(val)

        if not self.minStack:
            self.minStack.append(val)                          # first element
        else:
            currentMin = self.minStack[-1]
            self.minStack.append(min(val, currentMin))         # track new minimum

    def pop(self) -> None:
        if not self.mainStack:
            return
        self.mainStack.pop()   # pop both stacks together
        self.minStack.pop()    # restores previous minimum

    def top(self) -> int:
        if not self.mainStack:
            return -1
        return self.mainStack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return -1
        return self.minStack[-1]   # top of minStack = current minimum


## Test Cases
def test_min_stack():
    """Test cases for MinStack class."""

    # Test 1: Basic push and getMin
    s = MinStack()
    s.push(1)
    result = s.getMin()
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 1 passed: Single push — getMin() = 1")

    # Test 2: Push larger value, min should not change
    s = MinStack()
    s.push(1)
    s.push(2)
    result = s.getMin()
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 2 passed: Push larger value — getMin() still 1")

    # Test 3: Push smaller value, min should update
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    result = s.getMin()
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test 3 passed: Push smaller value — getMin() = 0")

    # Test 4: Pop restores previous minimum
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    s.pop()                        # removes 0
    result = s.getMin()
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 4 passed: After pop — getMin() restored to 1")

    # Test 5: Full example from problem statement
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    assert s.getMin() == 0, f"Expected 0, got {s.getMin()}"
    s.pop()
    assert s.top()    == 2, f"Expected 2, got {s.top()}"
    assert s.getMin() == 1, f"Expected 1, got {s.getMin()}"
    print("✓ Test 5 passed: Full example — getMin=0, top=2, getMin=1")

    # Test 6: Push duplicate minimum values
    s = MinStack()
    s.push(3)
    s.push(3)
    assert s.getMin() == 3, f"Expected 3, got {s.getMin()}"
    s.pop()
    result = s.getMin()
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test 6 passed: Duplicate min values — getMin() = 3 after pop")

    # Test 7: Push negative values
    s = MinStack()
    s.push(-1)
    s.push(-2)
    s.push(-3)
    result = s.getMin()
    assert result == -3, f"Expected -3, got {result}"
    s.pop()
    result = s.getMin()
    assert result == -2, f"Expected -2, got {result}"
    print("✓ Test 7 passed: Negative values — getMin() tracks correctly")

    # Test 8: top() returns correct value
    s = MinStack()
    s.push(5)
    s.push(10)
    result = s.top()
    assert result == 10, f"Expected 10, got {result}"
    print("✓ Test 8 passed: top() returns 10")

    # Test 9: top() after pop
    s = MinStack()
    s.push(5)
    s.push(10)
    s.pop()
    result = s.top()
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Test 9 passed: top() after pop returns 5")

    # Test 10: pop on empty stack does not crash
    s = MinStack()
    s.pop()   # should not raise an error
    print("✓ Test 10 passed: pop() on empty stack is safe")

    # Test 11: getMin on empty stack returns -1 (guard)
    s = MinStack()
    result = s.getMin()
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 11 passed: getMin() on empty stack returns -1")

    # Test 12: top on empty stack returns -1 (guard)
    s = MinStack()
    result = s.top()
    assert result == -1, f"Expected -1, got {result}"
    print("✓ Test 12 passed: top() on empty stack returns -1")

    # Test 13: Large push sequence
    s = MinStack()
    for i in range(100, 0, -1):   # push 100 down to 1
        s.push(i)
    result = s.getMin()
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Test 13 passed: Large sequence — getMin() = 1")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_min_stack()

# Quick demo
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())   # Output: 0
minStack.pop()
print(minStack.top())      # Output: 2
print(minStack.getMin())   # Output: 1
